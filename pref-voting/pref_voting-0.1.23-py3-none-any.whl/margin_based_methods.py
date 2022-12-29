'''
    File: margin_based_methods.py
    Author: Eric Pacuit (epacuit@umd.edu)
    Date: January 10, 2022
    Update: July 31, 2022
    
    Implementations of voting methods that work on both profiles and margin graphs.
'''

from pref_voting.voting_method import  *
from pref_voting.helper import get_mg
import math
from itertools import product, permutations, combinations, chain

import networkx as nx
import matplotlib.pyplot as plt


@vm(name = "Minimax")
def minimax(edata, curr_cands = None, strength_function = None):   
    """
    The Minimax winners are the candidates with the smallest maximum pairwise defeat.  That is, for each candidate :math:`a` find the biggest margin of a candidate :math:`b` over :math:`a`, then elect the candidate(s) with the smallest such loss. Also known as the Simpson-Kramer Rule.
    
    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``

    Returns: 
        A sorted list of candidates

    .. seealso::

        :meth:`pref_voting.margin_based_methods.minimax_scores`

    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_minimax.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import minimax

        minimax.display(prof)


    .. exec_code:: 
        :hide_code:

        from pref_voting.profiles import Profile
        from pref_voting.margin_based_methods import minimax
        
        prof = Profile([[3, 0, 1, 2], [1, 3, 2, 0], [1, 3, 0, 2], [1, 2, 0, 3], [3, 2, 0, 1], [0, 2, 1, 3]], [1, 1, 1, 1, 2, 1])

        minimax.display(prof)

    """

    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function

    scores = {c: max([strength_function(_c, c) for _c in edata.dominators(c)]) if len(edata.dominators(c)) > 0 else 0 
              for c in candidates}
    min_score = min(scores.values())
    return sorted([c for c in candidates if scores[c] == min_score])

def minimax_scores(edata, curr_cands = None, score_method="margins"):
    """Return the minimax scores for each candidate, where the minimax score for :math:`c` is -1 * the maximum pairwise majority loss. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        score_method (str, optional): Options include "margins" (the default), "winning" assings to each candidate :math:`c` the maximum support of a candidate majority preferred to :math:`c`,  and "pairwise_opposition" assings to each candidate :math:`c` the maximum support of any candidate over :math:`c`.   These scores only lead to different results on non-linear profiles. 

    Returns: 
        A dictionary associating each candidate with its minimax score.

    .. seealso::

        :meth:`pref_voting.margin_based_methods.minimax`

    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_minimax.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import minimax_scores, minimax

        minimax.display(prof)
        print(minimax_scores(prof))


    .. exec_code:: 
        :hide_code:

        from pref_voting.profiles import Profile
        from pref_voting.margin_based_methods import minimax, minimax_scores
        
        prof = Profile([[3, 0, 1, 2], [1, 3, 2, 0], [1, 3, 0, 2], [1, 2, 0, 3], [3, 2, 0, 1], [0, 2, 1, 3]], [1, 1, 1, 1, 2, 1])

        minimax.display(prof)
        print(minimax_scores(prof))

    """
    
    candidates = edata.candidates if curr_cands is None else curr_cands

    if len(candidates) == 1:
        return {c: 0 for c in candidates}
    
    # there are different scoring functions that can be used to measure the worse loss for each 
    # candidate. These all produce the same set of winners when voters submit linear orders. 
    score_functions = {
        "winning": lambda cs, c: max([edata.support(_c,c) for _c in cs]) if len(cs) > 0 else 0,
        "margins": lambda cs, c: max([edata.margin(_c,c) for _c in cs]) if len(cs) > 0 else 0,
        "pairwise_opposition": lambda cs, c: max([edata.support(_c,c) for _c in cs])
    } 
    
    cands = {
        "winning": lambda c: edata.dominators(c, curr_cands = curr_cands),
        "margins": lambda c: edata.dominators(c, curr_cands = curr_cands),
        "pairwise_opposition": lambda c: [_c for _c in candidates if _c != c]
    } 

    return {c: -1 * score_functions[score_method](cands[score_method](c), c) for c in candidates}


def maximal_elements(g): 
    """return the nodes in g with no incoming arrows."""
    return [n for n in g.nodes if g.in_degree(n) == 0]


@vm(name="Beat Path")
def beat_path(edata, curr_cands = None, strength_function = None):   
    """For candidates :math:`a` and :math:`b`, a **path** from :math:`a` to :math:`b` is a sequence 
    :math:`x_1, \ldots, x_n` of distinct candidates  with  :math:`x_1=a` and :math:`x_n=b` such that 
    for :math:`1\leq k\leq n-1`, :math:`x_k` is majority preferred to :math:`x_{k+1}`.  The **strength of a path**
    is the minimal margin along that path.  Say that :math:`a` defeats :math:`b` according to Beat Path if the the strength of the strongest path from :math:`a` to :math:`b` is greater than the strength of the strongest path from :math:`b` to :math:`a`. Then, the candidates that are undefeated according to Beat Path are the winners.  Also known as the Schulze Rule. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.beat_path_faster`, :meth:`pref_voting.margin_based_methods.beat_path_defeat`


    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_bp_rp.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import beat_path

        beat_path.display(mg)


    .. exec_code:: 
        :hide_code:

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import beat_path
        
        mg = MarginGraph([0, 1, 2, 3], [(0, 2, 3), (1, 0, 5), (2, 1, 5), (2, 3, 1), (3, 0, 3), (3, 1, 1)])
        
        beat_path.display(mg)


    """

    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function
    
    mg = get_mg(edata, curr_cands = curr_cands)
    
    beat_paths_weights = {c: {c2:0 for c2 in candidates if c2 != c} for c in candidates}
    for c in candidates: 
        for other_c in beat_paths_weights[c].keys():
            all_paths =  list(nx.all_simple_paths(mg, c, other_c))
            if len(all_paths) > 0:
                beat_paths_weights[c][other_c] = max([min([strength_function(p[i], p[i+1]) 
                for i in range(0,len(p)-1)]) 
                for p in all_paths])
    
    winners = list()
    for c in candidates: 
        if all([beat_paths_weights[c][c2] >= beat_paths_weights[c2][c] for c2 in candidates  if c2 != c]):
            winners.append(c)
    return sorted(list(winners))


@vm(name="Beat Path")
def beat_path_faster(edata, curr_cands = None, strength_function = None):   
    """An implementation of Beat Path using a variation of the Floyd Warshall-Algorithm
    See https://en.wikipedia.org/wiki/Schulze_method#Implementation)
 
    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.beat_path`, :meth:`pref_voting.margin_based_methods.beat_path_defeat`


    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_bp_rp.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import beat_path_faster

        beat_path.display(mg)
        beat_path_faster.display(mg)


    .. exec_code:: 
        :hide_code:

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import beat_path, beat_path_faster
        
        mg = MarginGraph([0, 1, 2, 3], [(0, 2, 3), (1, 0, 5), (2, 1, 5), (2, 3, 1), (3, 0, 3), (3, 1, 1)])

        beat_path.display(mg)
        beat_path_faster.display(mg)

    """

    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function
        
    s_matrix = [[-np.inf for _ in candidates] for _ in candidates]
    for c1_idx, c1 in enumerate(candidates):
        for c2_idx, c2 in enumerate(candidates):
            if (edata.majority_prefers(c1, c2) or c1 == c2):
                s_matrix[c1_idx][c2_idx] = strength_function(c1, c2) 
    strength = list(map(lambda i : list(map(lambda j : j , i)) , s_matrix))
    for i_idx, i in enumerate(candidates):         
        for j_idx, j in enumerate(candidates): 
            if i!= j:
                for k_idx, k in enumerate(candidates): 
                    if i!= k and j != k:
                        strength[j_idx][k_idx] = max(strength[j_idx][k_idx], min(strength[j_idx][i_idx],strength[i_idx][k_idx]))
    winners = {i:True for i in candidates}
    for i_idx, i in enumerate(candidates): 
        for j_idx, j in enumerate(candidates):
            if i!=j:
                if strength[j_idx][i_idx] > strength[i_idx][j_idx]:
                    winners[i] = False
    return sorted([c for c in candidates if winners[c]])

def beat_path_defeat(edata, curr_cands = None, strength_function = None):   
    """Returns the defeat relation for Beat Path. 
    
    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A networkx DiGraph representing the Beat Path defeat relation. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.beat_path`, :meth:`pref_voting.margin_based_methods.beat_path_faster`

    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_bp_defeat.py
        :context: reset  
        :include-source: True

    """

    defeat = nx.DiGraph()
    
    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function
    
    mg = get_mg(edata, curr_cands = curr_cands)
    
    beat_paths_weights = {c: {c2:0 for c2 in candidates if c2 != c} for c in candidates}
    for c in candidates: 
        for other_c in beat_paths_weights[c].keys():
            all_paths = list(nx.all_simple_paths(mg, c, other_c))
            if len(all_paths) > 0:
                beat_paths_weights[c][other_c] = max([min([strength_function(p[i], p[i+1]) for i in range(0,len(p)-1)]) for p in all_paths])
        
    defeat.add_nodes_from(candidates)
    edges = list()
    for c1 in candidates: 
        for c2 in candidates: 
            if c1 != c2: 
                if beat_paths_weights[c1][c2] > beat_paths_weights[c2][c1]: 
                    edges.append((c1, c2))

    defeat.add_edges_from(edges)
    return defeat
    
@vm(name="Split Cycle")
def split_cycle(edata, curr_cands = None, strength_function = None):
    """A **majority cycle** is a sequence :math:`x_1, \ldots ,x_n` of distinct candidates with :math:`x_1=x_n` such that for :math:`1 \leq k \leq n-1`,  :math:`x_k` is majority preferred to :math:`x_{k+1}`.  The Split Cycle winners are determined as follows:  
    
    1. In each cycle, identify the head-to-head win(s) with the smallest margin of victory in that cycle.
    2. After completing step 1 for all cycles, discard the identified wins. All remaining wins count as defeats of the losing candidates.

    The candidates that are undefeated are the Split Cycle winners. 

    See https://github.com/epacuit/splitcycle and the paper https://arxiv.org/abs/2004.02350 for more information. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.split_cycle_faster`, :meth:`pref_voting.margin_based_methods.split_cycle_defeat`


    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_bp_rp.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import split_cycle

        split_cycle.display(mg)


    .. exec_code:: 
        :hide_code:

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import split_cycle
        
        mg = MarginGraph([0, 1, 2, 3], [(0, 2, 3), (1, 0, 5), (2, 1, 5), (2, 3, 1), (3, 0, 3), (3, 1, 1)])
        
        split_cycle.display(mg)


    """

    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function 
    
    # create the majority graph
    mg = get_mg(edata, curr_cands = curr_cands) 
    
    # find the cycle number for each candidate
    cycle_number = {cs:0 for cs in permutations(candidates,2)}
    for cycle in nx.simple_cycles(mg): # for each cycle in the margin graph
        
        # get all the margins (i.e., the weights) of the edges in the cycle
        strengths = list() 
        for idx,c1 in enumerate(cycle): 
            next_idx = idx + 1 if (idx + 1) < len(cycle) else 0
            c2 = cycle[next_idx]
            strengths.append(strength_function(c1, c2))
            
        split_number = min(strengths) # the split number of the cycle is the minimal margin
        
        for c1,c2 in cycle_number.keys():
            c1_index = cycle.index(c1) if c1 in cycle else -1
            c2_index = cycle.index(c2) if c2 in cycle else -1

            # only need to check cycles with an edge from c1 to c2
            if (c1_index != -1 and c2_index != -1) and ((c2_index == c1_index + 1) or (c1_index == len(cycle)-1 and c2_index == 0)):
                cycle_number[(c1,c2)] = split_number if split_number > cycle_number[(c1,c2)] else cycle_number[(c1,c2)]        
    
    # construct the defeat relation, where a defeats b if margin(a,b) > cycle_number(a,b) (see Lemma 3.13)
    defeat = nx.DiGraph()
    defeat.add_nodes_from(candidates)
    defeat.add_edges_from([(c1,c2)  
           for c1 in candidates 
           for c2 in candidates if c1 != c2 if edata.majority_prefers(c1, c2) and strength_function(c1,c2) > cycle_number[(c1,c2)]])
   
    # the winners are candidates not defeated by any other candidate
    winners = maximal_elements(defeat)
    
    return sorted(list(set(winners)))


@vm(name="Split Cycle")
def split_cycle_faster(edata, curr_cands = None, strength_function = None):   
    """An implementation of Split Cycle based on the Floyd-Warshall Algorithm. 

    See https://github.com/epacuit/splitcycle and the paper https://arxiv.org/abs/2004.02350 for more information. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.split_cycle`, :meth:`pref_voting.margin_based_methods.split_cycle_defeat`


    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_bp_rp.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import split_cycle, split_cycle_faster

        split_cycle.display(mg)
        split_cycle_faster.display(mg)


    .. exec_code:: 
        :hide_code:

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import split_cycle, split_cycle_faster
        
        mg = MarginGraph([0, 1, 2, 3], [(0, 2, 3), (1, 0, 5), (2, 1, 5), (2, 3, 1), (3, 0, 3), (3, 1, 1)])
        
        split_cycle.display(mg)
        split_cycle_faster.display(mg)


    """

    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function 
 
    weak_condorcet_winners = {c:True for c in candidates}
    s_matrix = [[-np.inf for _ in candidates] for _ in candidates]
    
    # initialize the s_matrix
    for c1_idx, c1 in enumerate(candidates):
        for c2_idx, c2 in enumerate(candidates):
            if (edata.majority_prefers(c1, c2) or c1 == c2):
                s_matrix[c1_idx][c2_idx] = strength_function(c1, c2) 
                weak_condorcet_winners[c2] = weak_condorcet_winners[c2] and (c1 == c2) # Weak Condorcet winners are Split Cycle winners
    
    strength = list(map(lambda i : list(map(lambda j : j , i)) , s_matrix))
    for i_idx, i in enumerate(candidates): 
        for j_idx, j in enumerate(candidates):
            if i!= j:
                if not weak_condorcet_winners[j]: # weak Condorcet winners are Split Cycle winners
                    for k_idx, k in enumerate(candidates): 
                        if i != k and j != k:
                            strength[j_idx][k_idx] = max(strength[j_idx][k_idx], min(strength[j_idx][i_idx],strength[i_idx][k_idx]))
    winners = {i:True for i in candidates}
    for i_idx, i in enumerate(candidates):
        for j_idx, j in enumerate(candidates):
            if i != j:
                if s_matrix[j_idx][i_idx] > strength[i_idx][j_idx]: # the main difference with Beat Path
                    winners[i] = False
    return sorted([c for c in candidates if winners[c]])


def split_cycle_defeat(edata, curr_cands = None):
    """
    Returns the Split Cycle defeat relation. 

    See https://arxiv.org/abs/2008.08451 for an extended discussion of this notion of defeat in an election. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A networkx DiGraph representing the Beat Path defeat relation. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.split_cycle`, :meth:`pref_voting.margin_based_methods.split_cycle_faster`

    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_sc_defeat.py
        :context: reset  
        :include-source: True

    """
    
    candidates = edata.candidates if curr_cands is None else curr_cands
    
    # create the margin graph
    mg = get_mg(edata, curr_cands = curr_cands)
    
    # find the cycle number for each candidate
    cycle_number = {cs:0 for cs in permutations(candidates,2)}
    for cycle in nx.simple_cycles(mg): # for each cycle in the margin graph

        # get all the margins (i.e., the weights) of the edges in the cycle
        margins = list() 
        for idx,c1 in enumerate(cycle): 
            next_idx = idx + 1 if (idx + 1) < len(cycle) else 0
            c2 = cycle[next_idx]
            margins.append(edata.margin(c1, c2))
            
        split_number = min(margins) # the split number of the cycle is the minimal margin
        for c1,c2 in cycle_number.keys():
            c1_index = cycle.index(c1) if c1 in cycle else -1
            c2_index = cycle.index(c2) if c2 in cycle else -1

            # only need to check cycles with an edge from c1 to c2
            if (c1_index != -1 and c2_index != -1) and ((c2_index == c1_index + 1) or (c1_index == len(cycle)-1 and c2_index == 0)):
                cycle_number[(c1,c2)] = split_number if split_number > cycle_number[(c1,c2)] else cycle_number[(c1,c2)]        

    # construct the defeat relation, where a defeats b if margin(a,b) > cycle_number(a,b) (see Lemma 3.13)
    defeat = nx.DiGraph()
    defeat.add_nodes_from(candidates)
    defeat.add_weighted_edges_from([(c1,c2, edata.margin(c1, c2))  
           for c1 in candidates 
           for c2 in candidates if c1 != c2 if edata.margin(c1,c2) > cycle_number[(c1,c2)]])

    return defeat



# flatten a 2d list - turn a 2d list into a single list of items
flatten = lambda l: [item for sublist in l for item in sublist]

def does_create_cycle(g, edge):
    '''return True if adding the edge to g create a cycle.
    it is assumed that edge is already in g'''
    source = edge[0]
    target = edge[1]
    for n in g.predecessors(source):
        if nx.has_path(g, target, n): 
            return True
    return False

@vm(name="Ranked Pairs")
def ranked_pairs(edata, curr_cands = None, strength_function = None):   
    """
    Order the edges in the margin graph from largest to smallest and lock them in in that order, skipping edges that create a cycle.  If there are ties in the margins, break the ties using a tie-breaking rule: a linear ordering over the edges.   A candidate is a Ranked Pairs winner if it wins according to some tie-breaking rule. Also known as Tideman's Rule.

    .. warning:: 
        This method can take a very long time to find winners. 
        
    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.ranked_pairs_with_test`, :meth:`pref_voting.margin_based_methods.ranked_pairs_zt`, :meth:`pref_voting.margin_based_methods.ranked_pairs_defeats`

    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_bp_rp.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import ranked_pairs

        ranked_pairs.display(mg)


    .. exec_code:: 
        :hide_code:

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import ranked_pairs
        
        mg = MarginGraph([0, 1, 2, 3], [(0, 2, 3), (1, 0, 5), (2, 1, 5), (2, 3, 1), (3, 0, 3), (3, 1, 1)])
        
        ranked_pairs.display(mg)

    """
    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function    

    cw = edata.condorcet_winner()
    # Ranked Pairs is Condorcet consistent, so simply return the Condorcet winner if exists
    if cw is not None: 
        winners = [cw]
    else:
        w_edges = [(c1, c2, strength_function(c1, c2)) for c1 in candidates for c2 in candidates 
                   if c1 != c2 and (edata.majority_prefers(c1, c2) or edata.is_tied(c1, c2))]
        winners = list()   
        if len(w_edges) > 0:          
            strengths = sorted(list(set([e[2] for e in w_edges])), reverse=True)
            sorted_edges = [[e for e in w_edges if e[2] == s] for s in strengths]
            tbs = product(*[permutations(edges) for edges in sorted_edges])
            for tb in tbs:
                edges = flatten(tb)
                rp_defeat = nx.DiGraph() 
                for e in edges: 
                    rp_defeat.add_edge(e[0], e[1], weight=e[2])
                    if does_create_cycle(rp_defeat, e):
                        rp_defeat.remove_edge(e[0], e[1])
                winners.append(maximal_elements(rp_defeat)[0])
        else: 
            winners = candidates
    return sorted(list(set(winners)))

@vm(name="Ranked Pairs")
def ranked_pairs_with_test(edata, curr_cands = None, strength_function = None):   
    """Find the Ranked Pairs winners, but include a test to determined if it will take too long to compute the Ranked Pairs winners. If the calculation of the winners will take too long, return None.

    .. important::
        This voting method that might return None rather than a list of candidates.  

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.ranked_pairs_with_test`, :meth:`pref_voting.margin_based_methods.ranked_pairs_zt`, :meth:`pref_voting.margin_based_methods.ranked_pairs_defeats`

    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_rp_with_test.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import ranked_pairs_with_test

        ranked_pairs_with_test.display(mg)


    .. exec_code:: 
        :hide_code:

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import ranked_pairs_with_test
        
        mg = MarginGraph([0, 1, 2, 3], [(1, 2, 2), (1, 3, 2), (2, 0, 2)])
        
        ranked_pairs_with_test.display(mg)


    """    
    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function   

    cw = edata.condorcet_winner()
    # Ranked Pairs is Condorcet consistent, so simply return the Condorcet winner if exists
    if cw is not None: 
        winners = [cw]
    else:
        w_edges = [(c1, c2, strength_function(c1, c2)) for c1 in candidates for c2 in candidates 
                   if c1 != c2 and (edata.majority_prefers(c1, c2) or edata.is_tied(c1, c2))]
        winners = list()            
        strengths = sorted(list(set([e[2] for e in w_edges])), reverse=True)
        sorted_edges = [[e for e in w_edges if e[2] == s] for s in strengths]
        if np.prod([math.factorial(len(es)) for es in sorted_edges]) > 3000: 
            return None
        else: 
            tbs = product(*[permutations(edges) for edges in sorted_edges])
            for tb in tbs:
                edges = flatten(tb)
                rp_defeat = nx.DiGraph() 
                for e in edges: 
                    rp_defeat.add_edge(e[0], e[1], weight=e[2])
                    if does_create_cycle(rp_defeat, e):
                        rp_defeat.remove_edge(e[0], e[1])
                winners.append(maximal_elements(rp_defeat)[0])
    return sorted(list(set(winners)))

def ranked_pairs_defeats(edata, curr_cands = None, strength_function = None):   
    """
    Returns the Ranked Pairs defeat relations produced by the Ranked Pairs algorithm. 

    .. important::
        Unlike the other functions that return a single defeat relation, this returns a list of defeat relations. 
        
    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A networkx DiGraph representing the Beat Path defeat relation. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.ranked_pairs`, :meth:`pref_voting.margin_based_methods.ranked_pairs_with_test`

    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_rp_defeats.py
        :context: reset  
        :include-source: True

    .. exec_code::


        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import ranked_pairs_defeats

        mg = MarginGraph([0, 1, 2, 3], [(0, 1, 10), (0, 2, 2), (1, 3, 4), (2, 1, 6), (2, 3, 8), (3, 0, 4)])
        rp_defeats = ranked_pairs_defeats(mg)

        for rpd in rp_defeats: 
            print(rpd.edges)

    """
    
    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function    

    w_edges = [(c1, c2, strength_function(c1, c2)) for c1 in candidates for c2 in candidates if c1 != c2 and (edata.majority_prefers(c1, c2) or edata.is_tied(c1, c2))]
    winners = list()            
    strengths = sorted(list(set([e[2] for e in w_edges])), reverse=True)
    sorted_edges = [[e for e in w_edges if e[2] == s] for s in strengths]
    tbs = product(*[permutations(edges) for edges in sorted_edges])
    rp_defeats = list()
    for tb in tbs:
        edges = flatten(tb)
        rp_defeat = nx.DiGraph() 
        for e in edges: 
            rp_defeat.add_edge(e[0], e[1], weight=e[2])
            if does_create_cycle(rp_defeat, e):
                rp_defeat.remove_edge(e[0], e[1])
        rp_defeats.append(rp_defeat)
        winners.append(maximal_elements(rp_defeat)[0])
    return rp_defeats

def powerset(iterable):
    """
    Return the powerset of ``iterable``

    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def is_stack(edata, cand_list, curr_cands=None): 
    """
    A **stack** is a linear order :math:`L` on the candidate such that for all candidates :math:`a` and :math:`b`, if :math:`aLb`, then there are distinct candidates :math:`x_1,\dots,x_n` with :math:`x_1=a` and :math:`x_n=b` such that :math:`x_i L x_{i+1}` and for all :math:`i\in \{1,\dots, n-1\}`, the margin of :math:`x_1` over :math:`x_{i+1}` is greater than or equal to the margin of :math:`b` over :math:`a`.

    This definition is due to Zavist and Tideman 1989, and is used as an alternative characterization of Ranked Pairs: :math:`a` is a Ranked Pairs winner if and only if :math:`a` is the maximum element of some stack. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        cand_list (list): The list of candidates that may be a stack
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``

    Returns: 
        True if ``cand_list`` is a stack and False otherwise

    :Example: 
    
    .. plot::  margin_graphs_examples/mg_ex_rp_stacks.py
        :context: reset  
        :include-source: True


    .. exec_code::
        
        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import is_stack
        from itertools import permutations
        
        mg = MarginGraph([0, 1, 2], [(0, 1, 2), (1, 2, 4), (2, 0, 2)])
        
        for clist in permutations(mg.candidates): 
            print(f"{clist} {'is' if is_stack(mg, clist) else 'is not'} a stack")
            
    """
    
    candidates = curr_cands if curr_cands is not None else edata.candidates
    cand_pairs = [(a, b) if cand_list.index(a) < cand_list.index(b) else (b, a) for a, b in combinations(candidates, 2)]
        
    for a, b in cand_pairs:
        other_cands = [c for c in candidates if c != a and c != b]
        found_path = False
        
        sublist = cand_list[cand_list.index(a) + 1:cand_list.index(b)]
        
        for indices in powerset(range(len(sublist))): 
            
            path = [a] + [sublist[i] for i in sorted(indices)] + [b]
            margins = [edata.margin(xi, path[i + 1]) for i, xi in enumerate(path[0:-1])]
            if all([cand_list.index(xi) < cand_list.index(path[i+1]) for i, xi in enumerate(path[0:-1])]) and all([m >= edata.margin(b, a) for m in margins]): 
                found_path = True
                break
        if not found_path: 
            return False
    return True

@vm(name="Ranked Pairs")
def ranked_pairs_from_stacks(edata, curr_cands = None): 
    """Find the Ranked Pairs winners by iterating over all permutations of candidates (restricted to ``curr_cands`` if not None), and checking if the list is a stack. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.ranked_pairs`, :meth:`pref_voting.margin_based_methods.is_stack`

    :Example: 

    .. plot::  margin_graphs_examples/mg_ex_bp_rp.py
        :context: reset  
        :include-source: True


    .. code-block:: 

        from pref_voting.margin_based_methods import ranked_pairs, ranked_pairs_from_stacks

        ranked_pairs.display(mg)
        ranked_pairs_from_stacks.display(mg)


    .. exec_code:: 
        :hide_code:

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import ranked_pairs, ranked_pairs_from_stacks
        
        mg = MarginGraph([0, 1, 2, 3], [(0, 2, 3), (1, 0, 5), (2, 1, 5), (2, 3, 1), (3, 0, 3), (3, 1, 1)])

        ranked_pairs.display(mg)
        ranked_pairs_from_stacks.display(mg)

    """    

    candidates = curr_cands if curr_cands is not None else edata.candidates
    winners = list()
    for clist in permutations(candidates): 
        isstack = is_stack(edata, clist, curr_cands = curr_cands)
        if isstack: 
            winners.append(clist[0])
            
    return sorted(list(set(winners)))

@vm(name="Ranked Pairs T")
def ranked_pairs_tb(edata, curr_cands = None, tie_breaker = None, strength_function = None):   
    """
    Ranked Pairs with a fixed linear order on the candidates to break any ties in the margins.   
    Since the tie_breaker is a linear order, this method is resolute.   

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.ranked_pairs`, :meth:`pref_voting.margin_based_methods.ranked_pairs_with_test`, :meth:`pref_voting.margin_based_methods.ranked_pairs_from_stacks`

    .. exec_code::

        from pref_voting.profiles import Profile
        from pref_voting.margin_based_methods import ranked_pairs_from_stacks, ranked_pairs_tb, ranked_pairs_zt

        prof = Profile([[2, 3, 1, 0], [0, 3, 1, 2], [1, 3, 2, 0], [2, 1, 3, 0]], [1, 1, 1, 1])

        prof.display()

        ranked_pairs_from_stacks.display(prof)
        ranked_pairs_tb.display(prof)
        ranked_pairs_tb.display(prof, tie_breaker = [3, 2, 1, 0])
        ranked_pairs_zt.display(prof)

    """

    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function
    
    tb_ranking = tie_breaker if tie_breaker is not None else sorted(list(candidates))

    cw = edata.condorcet_winner()
    # Ranked Pairs is Condorcet consistent, so simply return the Condorcet winner if exists
    if cw is not None: 
        winners = [cw]
    else:
        w_edges = [(c1, c2, strength_function(c1, c2)) for c1 in candidates for c2 in candidates 
                   if edata.majority_prefers(c1, c2) or edata.is_tied(c1, c2)]
        winners = list()            
        strengths = sorted(list(set([e[2] for e in w_edges])), reverse=True)
        
        rp_defeat = nx.DiGraph() 
        for s in strengths: 
            edges = [e for e in w_edges if e[2] == s]
            
            # break ties using the lexicographic ordering on tuples given tb_ranking
            sorted_edges = sorted(edges, key = lambda e: (tb_ranking.index(e[0]), tb_ranking.index(e[1])), reverse=False)
            for e in sorted_edges: 
                rp_defeat.add_edge(e[0], e[1], weight=e[2])
                if does_create_cycle(rp_defeat, e):
                    rp_defeat.remove_edge(e[0], e[1])
        winners.append(maximal_elements(rp_defeat)[0])

    return sorted(list(set(winners)))


@vm(name="Ranked Pairs ZT")
def ranked_pairs_zt(profile, curr_cands = None, strength_function = None):   
    """Ranked pairs where a fixed voter breaks any ties in the margins.  It is always the voter in position 0 that breaks the ties.  Since voters have strict preferences, this method is resolute.  This is known as Ranked Pairs ZT, for Zavist Tideman.

    Args:
        edata (Profile): A profile of linear orders
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.ranked_pairs`, :meth:`pref_voting.margin_based_methods.ranked_pairs_with_test`, :meth:`pref_voting.margin_based_methods.ranked_pairs_from_stacks`

    .. exec_code::

        from pref_voting.profiles import Profile
        from pref_voting.margin_based_methods import ranked_pairs_from_stacks, ranked_pairs_tb, ranked_pairs_zt

        prof = Profile([[2, 3, 1, 0], [0, 3, 1, 2], [1, 3, 2, 0], [2, 1, 3, 0]], [1, 1, 1, 1])

        prof.display()

        ranked_pairs_from_stacks.display(prof)
        ranked_pairs_tb.display(prof)
        ranked_pairs_tb.display(prof, tie_breaker = [3, 2, 1, 0])
        ranked_pairs_zt.display(prof)

    
    """
    candidates = profile.candidates if curr_cands is None else curr_cands    
    
    # the tie-breaker is always the first voter. 
    tb_ranking = tuple([c for c in list(profile._rankings[0]) if c in candidates])
    
    return ranked_pairs_tb(profile, curr_cands = curr_cands, tie_breaker = tb_ranking, strength_function = strength_function)



@vm(name="River")
def river(edata, curr_cands = None, strength_function = None):   
    """
    Order the edges in the weak margin graph from largest to smallest and lock them in in that order, skipping edges that create a cycle *and edges in which there is already an edge pointing to the target*.  Break ties using a tie-breaking  linear ordering over the edges.  A candidate is a River winner if it wins according to some tie-breaking rule. See https://electowiki.org/wiki/River.

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    :Example: 

    .. exec_code:: 

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import river, ranked_pairs
        
        mg = MarginGraph([0, 1, 2, 3], [(0, 2, 2), (0, 3, 8), (1, 0, 12), (2, 3, 12), (3, 1, 6)])

        ranked_pairs.display(mg)
        river.display(mg)

    """
    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function    

    cw = edata.condorcet_winner()
    # Ranked Pairs is Condorcet consistent, so simply return the Condorcet winner if exists
    if cw is not None: 
        winners = [cw]
    else:
        w_edges = [(c1, c2, strength_function(c1, c2)) for c1 in candidates for c2 in candidates 
                   if c1 != c2 and (edata.majority_prefers(c1, c2) or edata.is_tied(c1, c2))]
        winners = list()            
        strengths = sorted(list(set([e[2] for e in w_edges])), reverse=True)
        sorted_edges = [[e for e in w_edges if e[2] == s] for s in strengths]
        tbs = product(*[permutations(edges) for edges in sorted_edges])
        for tb in tbs:
            edges = flatten(tb)
            river_defeat = nx.DiGraph() 
            for e in edges: 
                if e[1] not in river_defeat.nodes or len(list(river_defeat.in_edges(e[1]))) == 0:
                    river_defeat.add_edge(e[0], e[1], weight=e[2])
                    if does_create_cycle(river_defeat, e):
                        river_defeat.remove_edge(e[0], e[1])
            winners.append(maximal_elements(river_defeat)[0])
    return sorted(list(set(winners)))


@vm(name="River")
def river_with_test(edata, curr_cands = None, strength_function = None):   
    """Find the River winners with a test to determined if it will take too long to compute the River winners. If the calculation of the winners will take too long, return None. 
        
    .. important::
        This voting method that might return None rather than a list of candidates.  

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.ranked_pairs_with_test`, :meth:`pref_voting.margin_based_methods.river`


    """
    candidates = edata.candidates if curr_cands is None else curr_cands    
    strength_function = edata.margin if strength_function is None else strength_function    

    cw = edata.condorcet_winner()
    # Ranked Pairs is Condorcet consistent, so simply return the Condorcet winner if exists
    if cw is not None: 
        winners = [cw]
    else:
        w_edges = [(c1, c2, strength_function(c1, c2)) for c1 in candidates for c2 in candidates 
                   if c1 != c2 and (edata.majority_prefers(c1, c2) or edata.is_tied(c1, c2))]
        winners = list()            
        strengths = sorted(list(set([e[2] for e in w_edges])), reverse=True)
        sorted_edges = [[e for e in w_edges if e[2] == s] for s in strengths]
        if np.prod([math.factorial(len(es)) for es in sorted_edges]) > 3000: 
            return None
        else: 
            tbs = product(*[permutations(edges) for edges in sorted_edges])
            for tb in tbs:
                edges = flatten(tb)
                river_defeat = nx.DiGraph() 
                for e in edges: 
                    if e[1] not in river_defeat.nodes or len(list(river_defeat.in_edges(e[1]))) == 0:
                        river_defeat.add_edge(e[0], e[1], weight=e[2])
                        if does_create_cycle(river_defeat, e):
                            river_defeat.remove_edge(e[0], e[1])
                winners.append(maximal_elements(river_defeat)[0])
    return sorted(list(set(winners)))

# Simple Stable Voting 
def _simple_stable_voting(edata, curr_cands = None, mem_sv_winners = {}, strength_function = None): 
    '''
    Determine the Simple Stable Voting winners while keeping track 
    of the winners in any subprofiles checked during computation. 
    '''
    
    # curr_cands is the set of candidates who have not been removed
    curr_cands = edata.candidates if curr_cands is None else curr_cands
    strength_function = edata.margin if strength_function is None else strength_function  
    
    sv_winners = list()

    matches = [(a, b) for a in curr_cands for b in curr_cands if a != b]
    strengths = list(set([strength_function(a, b) for a,b in matches]))
    
    if len(curr_cands) == 1: 
        mem_sv_winners[tuple(curr_cands)] = curr_cands
        return curr_cands, mem_sv_winners
    for s in sorted(strengths, reverse=True):
        for a, b in [ab_match for ab_match in matches 
                     if strength_function(ab_match[0], ab_match[1]) == s]:
            if a not in sv_winners: 
                cands_minus_b = [c for c in curr_cands if c!= b]
                cands_minus_b_key = tuple(sorted(cands_minus_b))
                if cands_minus_b_key not in mem_sv_winners.keys(): 
                    ws, mem_sv_winners = _simple_stable_voting(edata, 
                                                               curr_cands = cands_minus_b,
                                                               mem_sv_winners = mem_sv_winners,
                                                               strength_function = strength_function)
                    mem_sv_winners[cands_minus_b_key] = ws
                else: 
                    ws = mem_sv_winners[cands_minus_b_key]
                if a in ws:
                    sv_winners.append(a)
        if len(sv_winners) > 0: 
            return sv_winners, mem_sv_winners

          
@vm(name = "Simple Stable Voting")
def simple_stable_voting(edata, curr_cands = None, strength_function = None): 
    """Implementation of  Simple Stable Voting from https://arxiv.org/abs/2108.00542. 

    Simple Stable Voting is a recursive voting method defined as follows: 

    1.  If there is only one candidate in the profile, then that candidate is the winner. 
    2. Order the pairs :math:`(a,b)` of candidates from largest to smallest value of the margin of :math:`a` over :math:`b`, and declare as Simple Stable Voting winners the candidate(s) :math:`a` from the earliest pair(s) :math:`(a,b)` such that :math:`a` is a Simple Stable Voting winner in the election without :math:`b`. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.simple_stable_voting_faster`, :meth:`pref_voting.margin_based_methods.stable_voting`


    :Example: 

    .. exec_code::

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import simple_stable_voting

        mg = MarginGraph([0, 1, 2, 3], [(0, 3, 8), (1, 0, 10), (2, 0, 4), (2, 1, 8), (3, 1, 8)])

        simple_stable_voting.display(mg)

    """
    
    return sorted(_simple_stable_voting(edata, curr_cands = curr_cands, mem_sv_winners = {}, strength_function = strength_function)[0])


@vm(name = "Simple Stable Voting")
def simple_stable_voting_faster(edata, curr_cands = None, strength_function = None): 
    """Simple Stable Voting is Condorcet consistent.   It is faster to skip executing the recursive algorithm when there is a Condorcet winnerFirst check if there is a Condorcet winner.  If so, return the Condorcet winner, otherwise find the Simple Stable Voting winnner using _simple_stable_voting

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.simple_stable_voting`, :meth:`pref_voting.margin_based_methods.stable_voting`


    :Example: 

    .. exec_code::

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import simple_stable_voting, simple_stable_voting_faster

        mg = MarginGraph([0, 1, 2, 3], [(0, 3, 8), (1, 0, 10), (2, 0, 4), (2, 1, 8), (3, 1, 8)])

        simple_stable_voting_faster.display(mg)
        simple_stable_voting.display(mg)

    """
    
    cw = edata.condorcet_winner(curr_cands = None)
    if cw is not None: 
        return [cw]
    else: 
        return sorted(_simple_stable_voting(edata, curr_cands = curr_cands, mem_sv_winners = {}, strength_function = strength_function)[0])

    
def _stable_voting(edata, curr_cands = None, mem_sv_winners = {}, strength_function = None): 
    '''
    Determine the Stable Voting winners for the profile while keeping track of the winners in any subprofiles checked during computation. 
    '''
    
    # curr_cands is the set of candidates who have not been removed
    curr_cands = edata.candidates if curr_cands is None else curr_cands
    strength_function = edata.margin if strength_function is None else strength_function  

    sv_winners = list()
    
    undefeated_candidates = split_cycle_faster(edata, curr_cands = curr_cands)
    matches = [(a, b) for a in curr_cands for b in curr_cands if a != b if a in undefeated_candidates]
    strengths = list(set([strength_function(a, b) for a,b in matches]))
        
    if len(curr_cands) == 1: 
        mem_sv_winners[tuple(curr_cands)] = curr_cands
        return curr_cands, mem_sv_winners
    for s in sorted(strengths, reverse=True):
        for a, b in [ab_match for ab_match in matches 
                     if strength_function(ab_match[0], ab_match[1])  == s]:
            if a not in sv_winners: 
                cands_minus_b = [c for c in curr_cands if c!= b]
                cands_minus_b_key = tuple(sorted(cands_minus_b))
                if cands_minus_b_key not in mem_sv_winners.keys(): 
                    ws, mem_sv_winners = _stable_voting(edata, 
                                                        curr_cands = cands_minus_b, 
                                                        mem_sv_winners = mem_sv_winners, 
                                                        strength_function = strength_function)
                    mem_sv_winners[cands_minus_b_key] = ws
                else: 
                    ws = mem_sv_winners[cands_minus_b_key]
                if a in ws:
                    sv_winners.append(a)
        if len(sv_winners) > 0: 
            return sv_winners, mem_sv_winners
        
@vm(name = "Stable Voting")
def stable_voting(edata, curr_cands = None, strength_function = None): 
    """Implementation of  Stable Voting from https://arxiv.org/abs/2108.00542. 

    Stable Voting is a recursive voting method defined as follows: 

    1.  If there is only one candidate in the profile, then that candidate is the winner. 
    2. Order the pairs :math:`(a,b)` of candidates from largest to smallest value of the margin of :math:`a` over :math:`b` such that :math:`a` is undefeated according to Split Cycle, and declare as Stable Voting winners the candidate(s) :math:`a` from the earliest pair(s) :math:`(a,b)` such that :math:`a` is a Simple Stable Voting winner in the election without :math:`b`. 

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.simple_stable_faster`, :meth:`pref_voting.margin_based_methods.simple_stable_voting`


    :Example: 

    .. exec_code::

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import stable_voting

        mg = MarginGraph([0, 1, 2, 3], [(0, 3, 8), (1, 0, 10), (2, 0, 4), (2, 1, 8), (3, 1, 8)])

        stable_voting.display(mg)

    """
    return sorted(_stable_voting(edata, curr_cands = curr_cands, mem_sv_winners = {}, strength_function = strength_function)[0])


@vm(name = "Stable Voting")
def stable_voting_faster(edata, curr_cands = None, strength_function = None): 
    """
    Stable Voting is Condorcet consistent.   It is faster to skip executing the recursive algorithm when there is a Condorcet winner.  

    Args:
        edata (Profile, ProfileWithTies, MarginGraph): Any election data that has a `margin` method. 
        curr_cands (List[int], optional): If set, then find the winners for the profile restricted to the candidates in ``curr_cands``
        strength_function (function, optional): The strength function to be used to calculate the strength of a path.   The default is the margin method of ``edata``.   This only matters when the ballots are not linear orders. 

    Returns: 
        A sorted list of candidates. 

    .. seealso::

        :meth:`pref_voting.margin_based_methods.simple_stable_voting`, :meth:`pref_voting.margin_based_methods.stable_voting`


    :Example: 

    .. exec_code::

        from pref_voting.weighted_majority_graphs import MarginGraph
        from pref_voting.margin_based_methods import stable_voting, stable_voting_faster

        mg = MarginGraph([0, 1, 2, 3], [(0, 3, 8), (1, 0, 10), (2, 0, 4), (2, 1, 8), (3, 1, 8)])

        stable_voting_faster.display(mg)
        stable_voting.display(mg)


    """
    cw = edata.condorcet_winner(curr_cands = curr_cands)
    if cw is not None: 
        return [cw]
    else: 
        return sorted(_stable_voting(edata, curr_cands = curr_cands, mem_sv_winners = {}, strength_function = strength_function)[0])






mg_vms = [
    minimax, 
    split_cycle,
    split_cycle_faster,
    beat_path,
    beat_path_faster,
    #ranked_pairs,
    #ranked_pairs_with_test,
    ranked_pairs_zt,
    ranked_pairs_tb,
    #river,
    #river_with_test, 
    simple_stable_voting,
    simple_stable_voting_faster,
    stable_voting,
    stable_voting_faster,
]


mg_vms_all = [
    minimax, 
    split_cycle,
    split_cycle_faster,
    beat_path,
    beat_path_faster,
    ranked_pairs,
    ranked_pairs_with_test,
    ranked_pairs_zt,
    ranked_pairs_tb,
    river,
    river_with_test, 
    simple_stable_voting,
    simple_stable_voting_faster,
    stable_voting,
    stable_voting_faster,
]
