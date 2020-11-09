############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

from sources.Character import Character
from sources.utils import *


class Pacman():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self, c1: str, c2: str):
        self._file = None
        self._outputMap = None
        self._c1 = c1
        self._c2 = c2
        self._ghost = Character('F')
        self._pacman = Character('P')

    def getMapFromFile(self, filename: str) -> list:
        """Read `filename` and return a list of its line.

        Args:
            filename (str): File to read.

        Returns:
            list: List of file's lines. (without '\n')
        """

        pacMap = []

        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                pacMap.append(line)
        return pacMap

    def createOutput(self, pacMap: list) -> list:
        """Create an output map filled of ' ' and setup its walls.

        Args:
            pacMap (list): input map

        Returns:
            list: output Map.
        """

        outputMap = []

        for j in range(len(pacMap)):
            tmp = []
            for i in range(len(pacMap[j])):
                if pacMap[j][i] == WALL:
                    tmp.append(self._c1)
                elif pacMap[j][i] == EMPTY_SQUARE:
                    tmp.append(self._c2)
                else:
                    tmp.append(pacMap[j][i])
            outputMap.append(tmp)
        return outputMap

    def printOutput(self, outputMap: list) -> None:

        for line in outputMap:
            for elem in line:
                if isDigit(elem):
                    elem = int(elem) % 10
                print(elem, end='')
            print()

    def setupElements(self, filename: str) -> list:

        # Setup maps
        pacMap = self.getMapFromFile(filename)
        self._outputMap = self.createOutput(pacMap)
        if len(pacMap) < 3:
            print("Wrong map format.")
            exit(84)
        # Setup ghost and pacman
        self._ghost.getPosInList(pacMap, "ghost", self._ghost._c)
        if self._ghost._x == -1 or self._ghost._y == -1:
            print("No ghost in map.")
            exit(84)
        self._pacman.getPosInList(pacMap, "pacman", self._pacman._c)
        if self._pacman._x == -1 or self._pacman._y == -1:
            print("No pacman in map.")
            exit(84)

        return pacMap

    def computeDijkstra(self, pacMap: list, mini: int, x: int, y: int) -> bool:

        checkedCells = []

        def isValidCell(x: int, y: int) -> bool:
            if y < 0 or y >= len(self._outputMap):
                return False
            if x < 0 or x >= len(self._outputMap[y]):
                return False
            return True

        def computeDirection(pacMap: list, direction: str, mini: int, x: int, y: int) -> bool:

            nextDirection = DIR[direction](x, y)
            if isValidCell(nextDirection[X], nextDirection[Y]):
                nextCharFromInput = GETDIR[direction](pacMap, x, y)
                nextCharFromOutput = GETDIR[direction](self._outputMap, x, y)
                if nextCharFromInput == self._pacman._c:
                    return True
                if nextCharFromOutput == self._c2:
                    self._outputMap[nextDirection[Y]][nextDirection[X]] = mini+1
                    checkedCells.append([nextDirection[X], nextDirection[Y],
                                        self._outputMap[nextDirection[Y]][nextDirection[X]]])
            return False

        for dir in DIR:
            if computeDirection(pacMap, dir, mini, x, y):
                return True

        for cell in checkedCells:
            for dir in DIR:
                if computeDirection(pacMap, dir, cell[2], cell[X], cell[Y]):
                    return True

    def run(self, filename: str) -> None:

        """
        Run computations and process output printing.
        """

        # Setup
        pacMap = self.setupElements(filename)
        # Compute
        self.computeDijkstra(pacMap, 0, self._ghost._x, self._ghost._y)
        # Print
        self.printOutput(self._outputMap)
