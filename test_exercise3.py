#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

ADMIN = [["Number", "Surname", "Age"],
            [9297, "Rodriguez", 56],
            [7432, "O'Mealy", 39],
            [9824, "Darkes", 38]]

VENDORS = [["Numero", "Nombre", "Edad"],
            [9297, "Rodri uez", 56],
            [7432, "O'M", 39],
            [9824, "Darkes", 38]]




#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    result1 = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38],
              [9297, "Rodriguez", 56],
              [7432, "O'Mealy", 39]]


    assert is_equal(result1, union(GRADUATES, ADMIN))




def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

    result1 = [["Number", "Surname", "Age"],
              [9824, "Darkes", 38]]

    assert is_equal(result1, intersection(GRADUATES, ADMIN))

def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))
