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
    index = 0
    string_function = input_string[start:end]

    for ch in string_function:
        if ch == substring[0]:
            if string_function[index: index+len(substring)] == substring:
                return index
        index +=1
    return - 1


print(find("This is an ex-parrot", "parrot", 0, 20))



def multi_find(input_string, substring, start, end):

    new_string = ""
    new_index = 0
    index = find(input_string,substring,start,end)

    if index == -1:
        return -1

    else:
        new_string += (', ' + str(index))
        string_function = input_string[index+len(substring):]
        while len(string_function) > len(substring):
            index = find(string_function, substring, start,end)
            if index == -1:
                return new_string[2:]
            else:
                new_index += index + len(substring)
                string_function = string_function[index+len(substring):]
                new_string += ', ' + str(new_index)
        return new_string[2:]

print(multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20))
