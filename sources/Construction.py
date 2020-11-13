############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################

from copy import deepcopy

from sources.Task import Task, KO
from sources.utils import removeDup

class Construction():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._tasks = []
        self._totalDuration = 0

    def setTasks(self, filename: str) -> int:

        with open(filename, 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                task = Task(line)
                if (task._status == KO):
                    self._tasks.clear()
                    return 84
                self._tasks.append(task)
        return 0

    def getPrerequisites(self, taskName: str) -> list:

        for task in self._tasks:
            if task._id == taskName:
                return deepcopy(task._prerequisites)
        return []

    def getFullPrerequisites(self, prerequisites: list) -> list:

        newPrerequisites = deepcopy(prerequisites)

        for prerequisite in prerequisites:
            newPrerequisites += self.getPrerequisites(prerequisite)
        newPrerequisites = removeDup(newPrerequisites)
        return newPrerequisites

    def setDependencies(self) -> None:

        for task in self._tasks:
            task._prerequisites = self.getFullPrerequisites(task._prerequisites)

    def printOutput(self) -> None:

        print("Total duration of construction: {} week{}".format(
            self._totalDuration, 's' if self._totalDuration > 1 else ''
        ))
        print()
        #
        for task in self._tasks:
            print("{} must begin".format(task._id), end='')
            if len(task._date) > 1:
                print(" between t={} and t={}".format(task._date[0], task._date[-1]))
            else:
                print(" at t={}".format(task._date[0]))
        #
        print()
        for task in self._tasks:
            print("{}\t(0)\t".format(task._id), end='')
            print("{}{}".format(" "*task._date[0], task._duration*'='))


    def sortByDependencies(self) -> None:

        def isSorted() -> bool:

            for i in range(len(self._tasks)):
                for j in range(len(self._tasks)):
                    if self._tasks[j]._id ==  self._tasks[i]._id:
                        break
                    if self._tasks[i]._id in self._tasks[j]._prerequisites:
                        return False
            return True

        while isSorted() is False:
            for i in range(len(self._tasks)):
                for j in range(len(self._tasks)):
                    if self._tasks[j]._id ==  self._tasks[i]._id:
                        break
                    if self._tasks[i]._id in self._tasks[j]._prerequisites:
                        self._tasks[i], self._tasks[j] = self._tasks[j], self._tasks[i]
        return

    def computeStartDate(self) -> None:

        for i in range(1, len(self._tasks)):
            if self._tasks[i-1]._id in self._tasks[i]._prerequisites:
                self._tasks[i]._date[0] = self._tasks[i-1]._date[0] + self._tasks[i-1]._duration
            else:
                tmp = 0
                for j in range(len(self._tasks)):
                    if i == j:
                        break
                    if self._tasks[j]._id in self._tasks[i]._prerequisites:
                        tmp = self._tasks[j]._date[0] + self._tasks[j]._duration
                self._tasks[i]._date[0] = tmp

    def sortByStartDate(self) -> None:

        def isSorted() -> bool:
            for i in range(1, len(self._tasks)):
                if self._tasks[i]._date[0] < self._tasks[i-1]._date[0]:
                    return False
            return True

        while isSorted() is False :
            for i in range(1, len(self._tasks)):
                if self._tasks[i]._date[0] < self._tasks[i-1]._date[0]:
                    self._tasks[i], self._tasks[i-1] = self._tasks[i-1], self._tasks[i]

    def computeTotalDuration(self) -> None:

        self._totalDuration = self._tasks[-1]._date[0] + self._tasks[-1]._duration

    def run(self, filename: str) -> None:

        """
        Run computations and process output printing.
        """

        # Setup
        if self.setTasks(filename) == 84:
            exit(84)
        self.setDependencies()
        # Compute
        self.sortByDependencies()
        self.computeStartDate()
        self.sortByStartDate()
        self.computeTotalDuration()
        # # Print
        self.printOutput()
