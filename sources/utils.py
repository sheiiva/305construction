############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################


def isInt(item) -> bool:

    """Define if item is an integer or not.

    Args:
        item (?): Variable to check.

    Returns:
        bool: True if item is an integer, False otherwise.
    """

    try:
        int(item)
    except ValueError:
        return False
    else:
        return True


def removeDup(myList: list) -> list:

    res = []

    [res.append(x) for x in myList if x not in res]
    return res
