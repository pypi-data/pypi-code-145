import os
import sys
import select
import os.path as osp

__all__ = ["str2bool", "yn2bool", "yes_or_no", "maybe_mkdir", "timeout_input"]


def str2bool(s):
    if s.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif s.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise ValueError('str2bool is undefined for: "{}".'.format(s))


def yn2bool(s):
    if s.lower() in ("yes", "y"):
        return True
    elif s.lower() in ("no", "n"):
        return False
    else:
        raise ValueError('yn2bool is undefined for: "{}".'.format(s))


def yes_or_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
    It must be "yes" (the default), "no" or None (meaning that
    an answer is required from the user).
    The "answer" return value is True for "yes" or False for "no".
    """

    valid = {
        "yes": True,
        "y": True,
        "ye": True,
        "no": False,
        "n": False,
        "default": None,
        "def": None,
        "d": None,
    }

    quiet = os.getenv("JAM_QUIET", "")
    if quiet != "":
        quiet = quiet.lower()
        assert quiet in valid, "Invalid JAM_QUIET environ: {}.".format(quiet)
        choice = valid[quiet]
        sys.stdout.write(
            "Jam Quiet run:\n\tQuestion: {}\n\tChoice: {}\n".format(
                question, "Default" if choice is None else "Yes" if choice else "No"
            )
        )
        return choice if choice is not None else default

    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("Invalid default answer: '%s'." % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def maybe_mkdir(dirname):
    if osp.isdir(dirname):
        return
    if osp.isfile(dirname):
        return

    import jammy.io as io

    if yes_or_no('Creating directory "{}"?'.format(dirname)):
        io.mkdir(dirname)


def timeout_input(prompt, timeout=10, default="", strict=False):
    print(prompt, end=": ", flush=True)
    inputs, outputs, errors = select.select([sys.stdin], [], [], timeout)
    print()
    if not inputs and strict:
        raise RuntimeError
    return sys.stdin.readline().strip()
