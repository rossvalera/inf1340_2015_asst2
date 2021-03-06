#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Sinisa Savic', 'Marcos Armstrong', 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    This function will translate any English word to Pig latin
    :param word: Any word using the alphabet
    :return: The word will get translated to Pig Latin
            If the first letter is a vowel will add "yay" to the end
            If the first letter is a consonant will take all consonants up until teh worst vowel and add them to the end
            with "ay" added
    """
    # variables defined and used within code
    original = word.lower()
    pig = "yay"
    # For this assignment we will consider y a vowel always

    vowel = ["a", "e", "i", "o", "u"]
    index = 0
    found_letter = -1

    # Makes sure that all inputs are actual letters and not numbers
    if len(original) > 0 and original.isalpha():
        # Checks each letter of a given word to until first vowel is found
        for i in original:
            if i in vowel:
                found_letter = index
                break
            index += 1

        # no vowel found thus will return given word with "ay" at the end
        if found_letter == -1:
            no_vowel = original + pig[1:]
            return no_vowel
        # When first letter in the given word is a vowel will return the word with "yay" at the end
        elif found_letter == 0:
            first_vowel = original + pig
            return first_vowel
        # Will take all consonants up until the vowel in a word
        # Will return the word starting with the vowel and will add the removed consonants and "ay" to the end
        else:
            first_consonant = original[found_letter:] + original[0:found_letter] + pig[1:]
            return first_consonant

    # Any word that doesnt only use alphabetical characters will return "try again"
    # No input will also return "try again"
    else:
        return "try again"

# Function Commented out
# print(pig_latinify(""))
