"""
This module provides some functions to deal with skyscrapers game
git repo - https://github.com/yarkoslav/skyscrapers
"""



def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
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
    now_visible = line[0]
    counter = 1
    for height in line:
        if height > now_visible:
            now_visible = height
            counter += 1
    return counter == pivot


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


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    """
    is_hor_visible = True
    rows = board[1:-1]
    for row in rows:
        if row[0].isdigit():
            hint = int(row[0])
            if not left_to_right_check(row, hint):
                is_hor_visible = False
        if row[-1].isdigit():
            hint = int(row[-1])
            row = row[::-1]
            if not left_to_right_check(row, hint):
                is_hor_visible = False
    return is_hor_visible


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    columns = []
    for index in range(0, len(board)):
        column = ''
        for j in range(len(board)):
            column = column + board[j][index]
        columns.append(column)
    return check_horizontal_visibility(columns) and check_uniqueness_in_rows(columns)


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    return check_columns(board) and check_uniqueness_in_rows(board) and\
           check_horizontal_visibility(board) and check_not_finished_board(board)


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
