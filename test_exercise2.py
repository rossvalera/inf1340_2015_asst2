#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Sinisa Savic', 'Marcos Armstrong', 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    # Test cases added that also check for wrong input and output
    assert find("Hello World", "Wo",0,14) == 6
    # Test case shows when substring not found, -1 returned
    assert find("Welcome to Python", "help",0,18) == -1
    assert find("This is an ex-parrot", "parrot",20,30) == -1


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    # Test Cases added to check other correct and incorrect input/output
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0, 4, 8, 12"
    assert multi_find("HI HI HI HI","HI",0,12) == "0, 3, 6, 9"
    # Test case shows when substring not found, -1 returned
    assert multi_find("Helololololololo", "Ni", 0, 20) == -1
