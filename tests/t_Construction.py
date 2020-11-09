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


def test_normal_case(capsys):

    ction = Construction()
    
    assert ction.setTasks("tests/deps/example") == 0
    assert len(ction._tasks) == 9


def test_wrong_elem(capsys):

    ction = Construction()
    
    assert ction.setTasks("tests/deps/wrongElem") == 84
    assert len(ction._tasks) == 0
