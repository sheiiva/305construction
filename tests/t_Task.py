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

from sources.Task import Task, OK, KO


def test_normal_case(capsys):

    task = Task("Fin;finishing touches;9;Cov;Ele;Mas;Plu")

    assert task._status == OK
    assert task._id == "Fin"
    assert task._description == "finishing touches"
    assert task._duration == 9
    assert task._prerequisites == ["Cov", "Ele", "Mas", "Plu"]


def test_wrong_item_number(capsys):

    task = Task("Car;carpenter")

    assert task._status == KO

    redir = capsys.readouterr()
    assert redir.out == "ERROR: wrong file format.\n"


def test_durantion_not_an_int(capsys):

    task = Task("Car;carpenter;INT;Fou")

    assert task._status == KO

    redir = capsys.readouterr()
    assert redir.out == "ERROR: wrong file format.\n"
