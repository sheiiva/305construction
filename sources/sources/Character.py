############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

class Character():

    def __init__(self, token: str):
        self._x = -1
        self._y = -1
        self._c = token

    def getPosInList(self, myList: list, elemType: str, token: str) -> None:
        """Look for in the `myList` list for the token value
        and set `_x` and `_y` Character's attributes.

        Args:
            myList (list): List to check.
            token (str): Token to look for.
        """

        found = False

        for j in range(len(myList)):
            for i in range(len(myList[j])):
                if myList[j][i] == token and found:
                    print("Too many {}s.".format(elemType))
                    exit(84)
                elif myList[j][i] == token:
                    self._x = i
                    self._y = j
                    found = True
