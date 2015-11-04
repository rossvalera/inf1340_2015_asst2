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
    vowel = ["a","e","i","o","u","y"]
    index = 0
    found_letter = -1
# y is always a vowel
    if len(original) > 0 and original.isalpha():
        for i in original:
            if i in vowel:
                found_letter = index
                break
            index +=1

        if found_letter == -1:
            no_vowel = original + pig[1:]
            print no_vowel
        elif found_letter == 0:
            first_vowel = original + pig
            print first_vowel
        else:
            first_consonant = original[found_letter:] + original[0:found_letter] + pig[1:]
            print first_consonant

    else:
        print("try again")
    return original

pig_latinify("helicopter")
# input word in between quotation marks

# print (word)


    # :param :
    # :return:
    # :raises:

    # result = ""

    # return result