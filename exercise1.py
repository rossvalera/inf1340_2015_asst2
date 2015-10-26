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
    original = word.lower() or word.upper() or word.lower[1:]
    pig = "yay"
    first_letter = word[0]
    vowels = list("a,e,i,o,u,y")

    if len(word) > 0 and word.isalpha():
        print (word)
    else:
        print("Try again")

    pig_latin_consonant = word[1 : len(original)] + first_letter + pig[1:]
    pig_latin_vowel = word + pig

    if first_letter in word[0] == vowels:
        print(pig_latin_vowel)
    else:
        print("try again")




    # :param :
    # :return:
    # :raises:

    # result = ""

    # return result