############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################


class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
