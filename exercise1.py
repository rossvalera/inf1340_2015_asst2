#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Describe your function


def pig_latinify():

    word = raw_input("Enter word:")
    original = word.lower() or word.upper() or word.lower[1:]
    pig = "yay"
    first_letter = original[0]
    vowels = list("a,e,i,o,u, y")
    consonants = list("b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,z")
    pig_latin_consonant = original[1: len(original)] + first_letter + pig[1:]
    pig_latin_vowel = original + pig

    if len(original) > 0 and original.isalpha():
        print(original)
    else:
        print("try again")

    if first_letter in original[0] == vowels:
        print(pig_latin_vowel)
    elif first_letter in original[0] == consonants:
        print(pig_latin_consonant)

pig_latinify()


# print (word)


    # :param :
    # :return:
    # :raises:

    # result = ""

    # return result