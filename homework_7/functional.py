import sys


def sequential_map(*args):
    """
    Accepts any number of functions as positional arguments and a container (list/set/tuple) with values
    as the last positional argument.
    Returns a list of the results of sequentially applying the passed functions to the values in the container.
    """
    cont = args[len(args) - 1]
    funcs = args[: len(args) - 1]


# The code below served successfully to find the container among the passed arguments in case the container was not the
# last argument, and I was sorry to remove it. :)
# There was "inspect.isfunction" instead of "callable", but modules cannot be used.
#    for arg in args:
#        if not callable(arg):
#            cont = arg
#            funcs = [arg for arg in args if arg != cont]

    for func in funcs:
        cont = map(func, cont)
    return list(cont)


def consensus_filter(*args):
    """
    Accepts any number of functions that return only True/False as positional arguments and a container (list/set/tuple)
    with values as the last positional argument.
    Returns a list of values that give True when passed to all the functions.
    """
    cont = args[len(args) - 1]
    funcs = args[: len(args) - 1]
    for func in funcs:
        cont = filter(func, cont)
    return list(cont)


def conditional_reduce(func_1, func_2, cont):
    """
    Accepts two functions as positional arguments that return only True/False and a container (list/set/tuple)
    with values as the last positional argument.
    Returns a value which is the result of standard reduce function, skipping the values which give False when passed
    to the first function.
    """
    passed = list(filter(func_1, cont))
    if passed:
        res = passed[0]
    else:
        return
    for elem in passed[1:]:
        res = func_2(res, elem)
    return res


# This was a function that accepted any number of arguments, but I ony made it return a list and not its elements :(
# Then I found out that only one argument would be passed and implemented the function that remained in the
# working version (below).
#
#
# def func_chain(*funcs):
#    def res(*args):
#        for func in funcs:
#            args = list(map(func, args))
#        return args
#    return res


def func_chain(*funcs):
    """
    Accepts any number of functions as positional arguments.
    Returns a function that combines all passed functions by sequential execution (takes one positional argument).
    """
    def res(arg):
        for func in funcs:
            arg = func(arg)
        return arg
    return res


def my_print(*args, sep=' ', end='\n', file=sys.stdout):
    """
    A complete analogue of the print function without using it itself (without the flush argument).
    """
    for i in range(len(args)):
        file.write(str(args[i]))
        if i != len(args) - 1:
            file.write(sep)
        else:
            file.write(end)

