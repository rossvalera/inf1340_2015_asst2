#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

""""""""

def table_check(table1, table2):

    if table1[0] == table2[0]:
        return "true"
    else:
        raise MismatchedAttributesException


def union(table1, table2):

    table_check(table1, table2)

    union_list = table1 + table2
    return remove_duplicates(union_list)


def intersection(table1, table2):

    table_check(table1, table2)
    int_list = []

    for schema in table1:
        for schema1 in table2:
            if schema == schema1:
                int_list.append(schema)
    return int_list




def difference(table1, table2):

    table_check(table1, table2)
    diff_list = []

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

