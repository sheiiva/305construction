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
            print("{} must begin".format(task._id))
        #
        print()
        for task in self._tasks:
            print("{}\t(0)\t".format(task._id), end='')
            print("{}{}".format("", task._duration*'='))

    def isSorted(self) -> bool:

        for i in range(len(self._tasks)):
            for j in range(len(self._tasks)):
                if self._tasks[j]._id ==  self._tasks[i]._id:
                    break
                if self._tasks[i]._id in self._tasks[j]._prerequisites:
                    return False
        return True

    def sortTasks(self):

        while self.isSorted() is False:
            for i in range(len(self._tasks)):
                for j in range(len(self._tasks)):
                    if self._tasks[j]._id ==  self._tasks[i]._id:
                        break
                    if self._tasks[i]._id in self._tasks[j]._prerequisites:
                        tmp = self._tasks[i]
                        self._tasks.pop(i)
                        self._tasks.insert(0, tmp)
        return

    def run(self, filename: str) -> None:

        """
        Run computations and process output printing.
        """

        # Setup
        if self.setTasks(filename) == 84:
            exit(84)
        # Compute
        self.setDependencies()
        self.sortTasks()
        # # Print
        self.printOutput()
