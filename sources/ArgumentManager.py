############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

import os


class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        def isValidFile(filename: str) -> bool:

            """Check if filename is an existing file."""

            try:
                f = open(filename)
            except IOError:
                print("{} is not a valid file.".format(filename))
                return False
            else:
                f.close()
                if os.stat(filename).st_size == 0:
                    print("{} is empty.".format(filename))
                    return False
                return True

        if len(argv) != 4:
            print("Wrong number of arguments.")
            return 84
        if isValidFile(argv[1]) is False:
            return 84
        if argv[2] == argv[3]:
            print("Please enter different values for `c1` and `c2`.")
            return 84
        return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
