import time
import traceback
import sys

# this setting will differ depending on the interpreter settings.
# Make sure it will run with current example
sys.setrecursionlimit(10000)


def measure_time(function):
    """
    A decorator wrapper fucntion that will measure the process time
    recursive functions (as well single-call fucntions) take.
    :param function: the decorated function
    :return: funtion - the wrapper function
    """
    def wrapper(*args, **kwargs):
        """
        The wrapper function that encapsulates the source method
        :param args: default arguments which will be passed to the source function
        :param kwargs: default keyworkd arguments which will be passed to the source function
        :return: None
        """
        start = time.time()
        try:
            return function(*args, **kwargs)
        except:
            raise
        finally:
            # Print only one time if function is recursive
            if function.__name__ != traceback.extract_stack(limit=2)[-2][2]:
                end = time.time() - start
                print "Elapsed Time for %s: %.3f" % (function.__name__, end)
    return wrapper


@measure_time
def recursive_flatten(items, seqtypes=(list, tuple, set)):
    """
    A recursive algorithm that is simple but slow and
    could hit the max recursion limit very quickly.
    :param items: iterable object - a non-flattened list
    :param seqtypes: optional iterable types to consider
    :return: flattened list of items
    """
    if items == []:
        return items
    if isinstance(items[0], seqtypes):
        return recursive_flatten(items[0]) + recursive_flatten(items[1:])
    return items[:1] + recursive_flatten(items[1:])


@measure_time
def faster_flatten(items, seqtypes=(list, tuple, set)):
    """
    A faster, simpler, non-recursive function of flattering any iterable object
    :param items: a non-flattened iterable object
    :param seqtypes: optional iterable types to consider
    :return: flattened list of items
    """
    for i, x in enumerate(items):
        while i < len(items) and isinstance(items[i], seqtypes):
            items[i:i+1] = items[i]
    return items

if __name__ == "__main__":
    crazy_list = ["random", [[None], ], set(range(1500)),[], [1, set([2, 3]), [10, [0, [45, 25.6], u"unicode", (str)]]]]
    flatten_list1 = faster_flatten(crazy_list)
    flatten_list2 = recursive_flatten(crazy_list)

    # do you really want to print this?
    print flatten_list1
    print flatten_list2
