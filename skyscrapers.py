"""
This module provides some functions to deal with skyscrapers game
"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    data = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            data.append(line)
    return data
