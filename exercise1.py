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
# variables defined and used within code
    original = word.lower() or word.upper() or word.lower[1:]
    pig = "yay"
# For this assignment we will consider y a vowel always
    vowel = ["a","e","i","o","u"]
    index = 0
    found_letter = -1
# Make sure that all inputs are actual letters and not numbers
    if len(original) > 0 and original.isalpha():
        for i in original:
            if i in vowel:
                found_letter = index
                break
            index +=1

        if found_letter == -1:
            no_vowel = original + pig[1:]
            return no_vowel
        elif found_letter == 0:
            first_vowel = original + pig
            return first_vowel
        else:
            first_consonant = original[found_letter:] + original[0:found_letter] + pig[1:]
            return first_consonant

    else:
        print("try again")
    return original

pig_latinify("helicopter")
