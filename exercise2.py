#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#def find(input_string, substring, start, end):

#range function?
def find(input_string, substring, start, end):
    # Get the DNA substring
    print('This program searches for a DNA substring within a DNA string')
    input_string = raw_input('Please enter a DNA string: ')
    substring = raw_input('Please enter a DNA substring: ')

# substring = DNA sequence that we want to locate
# input_string = complete DNA sequence that is searched.
# how is the vey lengthy input_string input?

    for substring in input_string:
        start = substring[0]
        end = (len(substring))

find()


"""
Describe your function

:param :
:return:
:raises:

"""
    #return -1


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result

