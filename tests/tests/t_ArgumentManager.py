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

from sources.ArgumentManager import ArgumentManager


def test_wrong_number_arg(capsys):

    argManager = ArgumentManager()
    argv = ['./305construction', 'file', 'file']

    assert argManager.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR: wrong number of arguments.\n"


def test_wrong_filename(capsys):

    argManager = ArgumentManager()
    argv = ['./305construction', 'file']

    assert argManager.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == f"ERROR: file: no such file.\n"


def test_empty_file(capsys):

    argManager = ArgumentManager()
    file = 'tests/deps/emptyFile'
    argv = ['./305construction', file]

    assert argManager.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == f"ERROR: {file}: empty file.\n"
