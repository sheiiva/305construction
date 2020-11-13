############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################

import pytest

from sources.Construction import Construction
from tests.deps.expected import *


def test_normal_case(capsys):

    Construction().run("tests/deps/example")

    redir = capsys.readouterr()

    assert redir.out == NORMAL_CASE_OUTPUT


def test_wrong_elem(capsys):

    ction = Construction()
    
    assert ction.setTasks("tests/deps/wrongElem") == 84
    assert len(ction._tasks) == 0
