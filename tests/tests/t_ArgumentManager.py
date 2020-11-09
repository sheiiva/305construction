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


def test_needHelp_h_case():

    argman = ArgumentManager()

    argv = ['binary', '-h']

    assert argman.needHelp(argv) is True


def test_needHelp_help_case():

    argman = ArgumentManager()

    argv = ['binary', '--help']

    assert argman.needHelp(argv) is True


def test_needHelp_wrong_case():

    argman = ArgumentManager()

    argv = ['binary', 'no']

    assert argman.needHelp(argv) is False


def test_normal_case():

    argManager = ArgumentManager()
    argv = ['./305construction', 'tests/deps/example', ]

    assert argManager.checkArgs(argv) == 0


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
