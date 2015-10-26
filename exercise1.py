#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Describe your function


def pig_latinify(word):

    word = raw_input("Enter word:")

if len(word) > 0 and word.isalpha():
    print word
word = original.lower() or original.upper() or original.lower[1:]
pig = "yay"
first_letter = word[0]
vowels = list("aeiou")

pig_latin_word = word[1 : len(original)] + first_letter + pig
if first_letter in word[0] == vowels:
    pig_latin_word = word + pig[1:]

else: print "try again"




    # :param :
    # :return:
    # :raises:

    # result = ""

    # return result