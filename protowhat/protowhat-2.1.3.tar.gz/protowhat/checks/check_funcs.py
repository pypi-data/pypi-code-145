import re

from functools import partial, wraps

from protowhat.Feedback import Feedback

MSG_CHECK_FALLBACK = "Your submission is incorrect. Try again!"
DEFAULT_MISSING_MSG = "Could not find the {index}{node_name}."
DEFAULT_APPEND_MSG = "Check the {index}{node_name}. "


def requires_ast(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        state = kwargs.get("state", args[0] if len(args) else None)
        state_ast = [state.student_ast, state.solution_ast]

        # fail if no ast parser in use
        if any(ast is None for ast in state_ast):
            raise TypeError(
                "Trying to use ast, but it is None. Are you using a parser? {} {}".format(
                    args, kwargs
                )
            )

        # check whether the parser passed or failed for some code
        # if safe_parsing is enabled in the Dispatcher (otherwise an exception would be raised earlier)
        ParseError = state.ast_dispatcher.ParseError

        parse_fail = any(isinstance(ast, ParseError) for ast in state_ast)

        if parse_fail:
            return state  # skip test
        else:
            return f(*args, **kwargs)  # proceed with test

    return wrapper


@requires_ast
def check_node(
    state, name, index=0, missing_msg=None, priority=None
):
    """Select a node from abstract syntax tree (AST), using its name and index position.

    Args:
        state: State instance describing student and solution code. Can be omitted if used with Ex().
        name : the name of the abstract syntax tree node to find.
        index: the position of that node (see below for details).
        missing_msg: feedback message if node is not in student AST.
        priority: the priority level of the node being searched for. This determines whether to
                  descend into other AST nodes during the search. Higher priority nodes descend
                  into lower priority. Currently, the only important part of priority is that
                  setting a very high priority (e.g. 99) will search every node.

    :Example:
        If both the student and solution code are.. ::

            SELECT a FROM b; SELECT x FROM y;

        then we can focus on the first select with::

            # approach 1: with manually created State instance
            state = State(*args, **kwargs)
            new_state = check_node(state, 'SelectStmt', 0)

            # approach 2:  with Ex and chaining
            new_state = Ex().check_node('SelectStmt', 0)

    """
    has_custom_message = bool(missing_msg)
    if missing_msg is None:
        missing_msg = DEFAULT_MISSING_MSG
    df = partial(state.ast_dispatcher.find, name, priority=priority)

    sol_stmt_list = df(state.solution_ast)
    try:
        sol_stmt = sol_stmt_list[index]
    except IndexError:
        raise IndexError("Can't get %s statement at index %s" % (name, index))

    stu_stmt_list = df(state.student_ast)
    try:
        stu_stmt = stu_stmt_list[index]
    except IndexError:
        # use speaker on ast dialect module to get message, or fall back to generic
        ast_path = state.get_ast_path() or "highlighted code"
        msg = state.ast_dispatcher.describe(
            sol_stmt, missing_msg, index=index, ast_path=ast_path
        )
        if msg is None:
            msg = MSG_CHECK_FALLBACK
        if has_custom_message:
            state.report(msg, append=False)
        state.report(msg)

    append_message = state.ast_dispatcher.describe(
        sol_stmt, DEFAULT_APPEND_MSG, index=index
    )
    return state.to_child(
        student_ast=stu_stmt, solution_ast=sol_stmt, append_message=append_message
    )


@requires_ast
def check_edge(state, name, index=0, missing_msg=None):
    """Select an attribute from an abstract syntax tree (AST) node, using the attribute name.

    Args:
        state: State instance describing student and solution code. Can be omitted if used with Ex().
        name: the name of the attribute to select from current AST node.
        index: entry to get from a list field. If too few entires, will fail with missing_msg.
        missing_msg: feedback message if attribute is not in student AST.

    :Example:
        If both the student and solution code are.. ::

            SELECT a FROM b; SELECT x FROM y;

        then we can get the from_clause using ::

            # approach 1: with manually created State instance -----
            state = State(*args, **kwargs)
            select = check_node(state, 'SelectStmt', 0)
            clause = check_edge(select, 'from_clause')

            # approach 2: with Ex and chaining ---------------------
            select = Ex().check_node('SelectStmt', 0)           # get first select statement
            clause =  select.check_edge('from_clause', None)    # get from_clause (a list)
            clause2 = select.check_edge('from_clause', 0)       # get first entry in from_clause
    """
    has_custom_message = bool(missing_msg)
    if missing_msg is None:
        missing_msg = DEFAULT_MISSING_MSG

    def select(node_name, node):
        attr = state.ast_dispatcher.select(node_name, node)
        if attr and isinstance(attr, list) and index is not None:
            attr = attr[index]
        return attr

    try:
        sol_attr = select(name, state.solution_ast)
    except IndexError:
        raise IndexError("Can't get %s attribute" % name)

    # use speaker on ast dialect module to get message, or fall back to generic
    ast_path = state.get_ast_path() or "highlighted code"
    _msg = state.ast_dispatcher.describe(
        state.student_ast, missing_msg, field=name, index=index, ast_path=ast_path
    )
    if _msg is None:
        _msg = MSG_CHECK_FALLBACK

    try:
        stu_attr = select(name, state.student_ast)
    except:
        if has_custom_message:
            state.report(_msg, append=False)
        state.report(_msg)

    # fail if attribute exists, but is none only for student
    if stu_attr is None and sol_attr is not None:
        if has_custom_message:
            state.report(_msg, append=False)
        state.report(_msg)

    append_message = state.ast_dispatcher.describe(
        state.student_ast, "Check the {field_name}. ", index=index, field=name
    )
    return state.to_child(
        student_ast=stu_attr, solution_ast=sol_attr, append_message=append_message
    )


def has_code(
    state,
    text,
    incorrect_msg="Check the {ast_path}. The checker expected to find {text}.",
    fixed=False,
):
    """Test whether the student code contains text.

    Args:
        state: State instance describing student and solution code. Can be omitted if used with Ex().
        text : text that student code must contain. Can be a regex pattern or a simple string.
        incorrect_msg: feedback message if text is not in student code.
        fixed: whether to match text exactly, rather than using regular expressions.

    Note:
        Functions like ``check_node`` focus on certain parts of code.
        Using these functions followed by ``has_code`` will only look
        in the code being focused on.

    :Example:
        If the student code is.. ::

            SELECT a FROM b WHERE id < 100

        Then the first test below would (unfortunately) pass, but the second would fail..::

            # contained in student code
            Ex().has_code(text="id < 10")

            # the $ means that you are matching the end of a line
            Ex().has_code(text="id < 10$")

        By setting ``fixed = True``, you can search for fixed strings::

            # without fixed = True, '*' matches any character
            Ex().has_code(text="SELECT * FROM b")               # passes
            Ex().has_code(text="SELECT \\\\* FROM b")             # fails
            Ex().has_code(text="SELECT * FROM b", fixed=True)   # fails

        You can check only the code corresponding to the WHERE clause, using ::

            where = Ex().check_node('SelectStmt', 0).check_edge('where_clause')
            where.has_code(text = "id < 10)

    """
    stu_ast = state.student_ast
    stu_code = state.student_code

    # fallback on using complete student code if no ast
    ParseError = state.ast_dispatcher.ParseError

    def get_text(ast, code):
        if isinstance(ast, ParseError):
            return code
        try:
            return ast.get_text(code) or ""
        except:
            return code

    stu_text = get_text(stu_ast, stu_code)

    _msg = incorrect_msg.format(
        ast_path=state.get_ast_path() or "highlighted code", text=text
    )

    # either simple text matching or regex test
    res = text in stu_text if fixed else re.search(text, stu_text)

    if not res:
        state.report(_msg)

    return state


@requires_ast
def has_equal_ast(
    state,
    incorrect_msg=None,
    sql=None,
    start=["expression", "subquery", "sql_script"][0],
    exact=None,
    should_append_msg=False,
):
    """Test whether the student and solution code have identical AST representations

    Args:
        state: State instance describing student and solution code. Can be omitted if used with Ex().
        incorrect_msg: feedback message if student and solution ASTs don't match
        sql  : optional code to use instead of the solution ast that is zoomed in on.
        start: if ``sql`` arg is used, the parser rule to parse the sql code.
               One of 'expression' (the default), 'subquery', or 'sql_script'.
        exact: whether to require an exact match (True), or only that the
               student AST contains the solution AST. If not specified, this
               defaults to ``True`` if ``sql`` is not specified, and to ``False``
               if ``sql`` is specified. You can always specify it manually.
        should_append_msg: prepend the auto generated incorrect_msg with the previous append_messages.

    :Example:

        Example 1 - Suppose the solution code is ::

            SELECT * FROM cities

        and you want to verify whether the `FROM` part is correct: ::

            Ex().check_node('SelectStmt').from_clause().has_equal_ast()

        Example 2 - Suppose the solution code is ::

            SELECT * FROM b WHERE id > 1 AND name = 'filip'

        Then the following SCT makes sure ``id > 1`` was used somewhere in the WHERE clause.::

            Ex().check_node('SelectStmt') \\/
                .check_edge('where_clause') \\/
                .has_equal_ast(sql = 'id > 1')

    """
    has_custom_message = bool(incorrect_msg)
    if not has_custom_message:
        if should_append_msg:  # Remove the ast_path mention because we are prepending.
            incorrect_msg = "{extra}"
        else:
            incorrect_msg = "Check the {ast_path}. {extra}"

    ast = state.ast_dispatcher.ast_mod
    sol_ast = state.solution_ast if sql is None else ast.parse(sql, start)

    # if sql is set, exact defaults to False.
    # if sql not set, exact defaults to True.
    if exact is None:
        exact = sql is None

    stu_rep = repr(state.student_ast)
    sol_rep = repr(sol_ast)

    def get_str(ast, code, sql):
        if sql:
            return sql
        if isinstance(ast, str):
            return ast
        try:
            return ast.get_text(code)
        except:
            return None

    sol_str = get_str(state.solution_ast, state.solution_code, sql)
    _msg = incorrect_msg.format(
        ast_path=state.get_ast_path()
        or ("code" if state.highlighting_disabled else "highlighted code"),
        extra="The checker expected to find `{}` in there.".format(sol_str)
        if sol_str
        else "Something is missing.",
    )
    if (exact and (sol_rep != stu_rep)) or (not exact and (sol_rep not in stu_rep)):
        if should_append_msg:
            state.report(_msg)
        state.report(_msg, append=False)

    return state


def has_parsed_ast(state):
    asts = [state.student_ast, state.solution_ast]
    if any(isinstance(c, state.ast_dispatcher.ParseError) for c in asts):
        state.report("AST did not parse")

    return state
