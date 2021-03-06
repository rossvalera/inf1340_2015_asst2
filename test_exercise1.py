#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Sinisa Savic', 'Marcos Armstrong', 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    # Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

    # Test cases to check various correct and incorrect inputs added
    assert pig_latinify("h4h4h") == "try again"
    assert pig_latinify("13131231") == "try again"
    assert pig_latinify("street") == "eetstray"
    assert pig_latinify("YELLOW") == "ellowyay"
    assert pig_latinify("") == "try again"
    assert pig_latinify("$%^&*") == "try again"
    assert pig_latinify("WhY") == "whyay"