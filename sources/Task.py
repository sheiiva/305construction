############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################

from sources.utils import isInt

# STATUS
OK = 1
KO = 0


class Task():

    def __init__(self, token: str):
        self._id = ""
        self._description = ""
        self._duration = -1
        self._prerequisites = []
        self._date = [0]
        #
        self._status = KO
        #
        self.parse(token)

    def parse(self, token: str) -> None:

        items = token.split(';')
        if len(items) < 3:
            print("ERROR: wrong file format.")
            return
        if isInt(items[2]) is False:
            print("ERROR: wrong file format.")
            return
        self._id = items[0]
        self._description = items[1]
        self._duration = int(items[2])
        for i in range(3, len(items)):
            self._prerequisites.append(items[i])
        self._status = OK
