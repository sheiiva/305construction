############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################

from os import stat
from os.path import isfile

class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        if len(argv) != 2:
            print("ERROR: wrong number of arguments.")
            return 84
        if isfile(argv[1]) is False:
            print(f"ERROR: {argv[1]}: no such file.")
            return 84
        if stat(argv[1]).st_size == 0:
            print(f"ERROR: {argv[1]}: empty file.")
            return 84
        return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
