############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

class Usage():

    def __init__(self):
        self.show()

    def show(self) -> None:

        """
        Show usage of the program.
        """

        print(
            "./304pacman file c1 c2\n"
            "\tfile\tfile describing the board, using the following characters:\n"
            "\t\t\t‘0’ for an empty square,\n"
            "\t\t\t‘1’ for a wall,\n"
            "\t\t\t‘F’ for the ghost’s position,\n"
            "\t\t\t‘P’ for Pacman’s position.\n"
            "\tc1\tcharacter to display for a wall\n"
            "\tc2\tcharacter to display for an empty space."
            )
