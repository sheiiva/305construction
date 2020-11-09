############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################

from sources.Task import Task, KO


class Construction():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._tasks = []

    def setTasks(self, filename: str) -> int:

        with open(filename, 'r') as f:
            for line in f:
                task = Task(line)
                if (task._status == KO):
                    self._tasks.clear()
                    return 84
                self._tasks.append(task)
        return 0

    def run(self, filename: str) -> None:

        """
        Run computations and process output printing.
        """

        # Setup
        if self.setTasks(filename) == 84:
            exit(84)
        # # Compute
        # self.computeDijkstra(pacMap, 0, self._ghost._x, self._ghost._y)
        # # Print
        # self.printOutput()
