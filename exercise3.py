#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Sinisa Savic', 'Marcos Armstrong', 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

""""""""


def table_check(table1, table2):
    """
    Function ro check if the attributes of two tables are the same
    :param table1: A table
    :param table2: A table
    :return: Return true if they are the same other wise raise MismatchedAttributesException
    """
    if table1[0] == table2[0]:
        return True
    else:
        raise MismatchedAttributesException


def union(table1, table2):
    """
   Function to add all attributes in two tables together while removing duplicates
   :param table1: A table
   :param table2: A table
   :return: New table with all rows and no duplicates or raise MismatchedAttributesException
    """

    # Checks to make sure attributes are the same
    table_check(table1, table2)

    # Adding tables together and removing duplicates, returns new table
    union_list = table1 + table2
    return remove_duplicates(union_list)


def intersection(table1, table2):
    """
    Function to create a table that only has unique attributes from both tables
    :param table1: A table
    :param table2: A table
    :return: New table with only unique attributes or raise MismatchedAttributesException
    """

    table_check(table1, table2)
    int_list = []

    # Checks for unique rows in both tables and return only the unique rows that are in both tables
    for schema in table1:
        for schema1 in table2:
            if schema == schema1:
                int_list.append(schema)
    return int_list


def difference(table1, table2):
    """
    Function to create a table that only has the unique attributes from teh first table and not the second
    :param table1: A Table
    :param table2: A table
    :return: The resulting table or raise MismatchedAttributesException
    """

    table_check(table1, table2)
    diff_list = []

    # Checks what rows are in table 1 that aren't in table 2 and makes a new table with them
    if table_check(table1, table2):
        diff_list = [table1[0]]
        for schema in table1:
            if schema not in table2:
                diff_list.append(schema)
        return diff_list


#####################
# HELPER FUNCTIONS ##
#####################


def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

