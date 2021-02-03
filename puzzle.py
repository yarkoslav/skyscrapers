"""
This module provide some functions to check whether board is good for game
git repo - https://github.com/yarkoslav/skyscrapers_and_puzzle
"""


def first_property(board: list) -> bool:
    """
    This functions checks first property of board(are the same digits in row)

    >>> first_property(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
" 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    res = True
    for row in board:
        same_row = set()
        for square in row:
            if square.isdigit() and square in same_row:
                res = False
            else:
                same_row.add(square)
    return res


def second_property(board: list) -> bool:
    """
    This function checks second property of board(are the same digits in column)

    >>> second_property(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
" 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    res = True
    for i in range(8):
        same_column = set()
        for j in range(8):
            square = board[j][i]
            if square.isdigit() and square in same_column:
                res = False
            else:
                same_column.add(square)
    return res


def third_property(board: list) -> bool:
    """
    This function ckecks third property of board(are there same digits in same color)

    >>> third_property(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
" 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    res = True
    for i in range(5):
        same_color =  set()
        for j in range(5):
            square = board[8-i-j][i]
            if square.isdigit() and square in same_color:
                res = False
            else:
                same_color.add(square)
        for j in range(1, 5):
            square = board[8-i][i+j]
            if square.isdigit() and square in same_color:
                res = False
            else:
                same_color.add(square)
    return res


def validate_board(board: list) -> bool:
    """
    This fuctions checks is board validate

    >>> validate_board(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
" 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    return first_property(board) and second_property(board) and third_property(board)
