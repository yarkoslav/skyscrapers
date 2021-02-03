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


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    line = input_line[1:-1]
    is_visible = True
    for index in range(pivot-1):
        if line[index] >= line[pivot-1]:
            is_visible = False
    return is_visible


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*',\
 '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    """
    is_finished = True
    for line in board:
        if '?' in line:
            is_finished = False
    return is_finished


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    """
    uniqueness = True
    rows = board[1:-1]
    for row in rows:
        row = row[1:-1]
        set_of_high = set()
        for building in row:
            if building in set_of_high:
                uniqueness = False
            set_of_high.add(building)
    return uniqueness