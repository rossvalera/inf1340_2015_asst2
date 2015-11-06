#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Sinisa Savic', 'Marcos Armstrong', 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    This function will responsible for finding the first instance of a substring within a string in a certain range
    :param input_string: Any length of characters
    :param substring: Characters that are being searched for
    :param start: Start of the range being looked at in the input_string
    :param end: End of the range being looked at in the input_string
    :return: The first location of the substring within the input_string or an error if it doesnt exist
    """
    # Define variables that will be used

    index = 0
    string_function = input_string[start:end]

    # Code to start checking each letter in given phrase until given word is found
    for ch in string_function:
        if ch == substring[0]:
            if string_function[index: index+len(substring)] == substring:
                return index
        index += 1
    # Given word is not in the range of the given phrase, error is given
    return - 1

# Function Commented out
# print(find("This is an ex-parrot", "parrot", 0, 20))


# Will return all instances of given word within phrase
def multi_find(input_string, substring, start, end):
    """
    Function to find all instances of the substring within the input_string
    :param input_string: Any length of characters
    :param substring: Characters that are being searched for
    :param start: Start of the range being looked at in the input_string
    :param end: End of the range being looked at in the input_string
    :return: Will return every instance of the substring within the input_string or an error if it doesnt exist
    """
    # Set variables that will be used
    new_string = ""
    new_index = 0
    index = find(input_string, substring, start, end)

    # Check if word is actually in the phrase if not gives back -1
    if index == -1:
        return -1

    # Word is in Phrase
    else:
        # Word is found in phrase and will count all instances of it
        new_string += (', ' + str(index))
        string_function = input_string[index+len(substring):]
        while len(string_function) > len(substring):
            index = find(string_function, substring, start, end)
            if index == -1:
                return new_string[2:]
            else:
                new_index += index + len(substring)
                string_function = string_function[index+len(substring):]
                new_string += ', ' + str(new_index)
        return new_string[2:]

# Function Commented out
# print(multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20))
