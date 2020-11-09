############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

import pytest

from sources.Usage import Usage
from tests.deps.expected import HELP_MESSAGE


def test_show(capsys):

    Usage()

    redir = capsys.readouterr()

    assert redir.out == HELP_MESSAGE
