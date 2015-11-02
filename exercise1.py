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

    original = word.lower() or word.upper() or word.lower[1:]
    pig = "yay"
    first_letter = original[0]
    pig_latin_consonant = original[1:len(original)] + first_letter + pig[1:]
    pig_latin_vowel = original + pig

    if len(original) > 0 and original.isalpha():
        if first_letter in ["a","e","i","o","u","y"]:
            print(pig_latin_vowel)
        else:
            print(pig_latin_consonant)
    else:
        print("try again")



pig_latinify()


# print (word)


    # :param :
    # :return:
    # :raises:

    # result = ""

    # return result