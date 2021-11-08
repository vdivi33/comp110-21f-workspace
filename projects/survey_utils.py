"""Utility functions!"""

__author__ = "730470448"
from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'!"""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
    
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    file_handle.close()

    # TODO: More Work!
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column"""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], limit: int) -> dict[str, list[str]]:
    """Returns a specified number of rows of data for each coloumn."""
    headed: dict[str, list[str]]
    headed = dict()
    i: int = 0
    if(limit > len(table)):
        limit = len(table)
    for element in table:
        headed[element] = list()
    for e in table:
        while i < limit:
            headed[e].append(table[e][i])
            i = i + 1
        i = 0
    return headed


def select(table: dict[str, list[str]], selected: list[str]) -> dict[str, list[str]]:
    """Returns specific coloumns with their respective rows."""
    result: dict[str, list[str]]
    result = dict()
    i: int = 0

    while i < len(selected):
        result[selected[i]] = table[selected[i]]
        i = i + 1
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables and combining the rows of each table if there are duplicate keys."""
    result: dict[str, list[str]]
    result = dict()
    for element in table_one:
        result[element] = table_one[element]
    for element in table_two:
        if table_one[element] == table_two[element]:
            result[element] = result[element] + table_two[element]
        else:
            result[element] = table_two[element]
    return result


def listing(table: dict[str,list[str]]) -> list[str]:
    result: list[str]
    result = list()
    j: int = 0
    for element in table:
        for i in table[element]:
            result.append(i)
    return result

def merge(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str,str]:
    result: dict[str, str]
    result = dict()

    for element in table_one:
        for i in table_two:
            result[table_one[element]] = "hi"



def count(list1: list[str]) -> dict[str, int]:
    """Counts the number of times a value exists in a key and puts it into a dictionary."""
    store: dict[str, int]
    store = dict()
    i: int = 0
    k: int = 0
    while k < len(list1):
        store[list1[k]] = 0
        k = k + 1
    for element in store:
        while i < len(list1):
            if(element == list1[i]):
                store[element] = store[element] + 1
                i = i + 1
            else:
                i = i + 1
        i = 0
    return store


