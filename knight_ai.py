"""
File:        knight_ai.py
Author:      Denzel Asamoah
Date:        2/6/2026
Section:     1190
E-mail:      denzela1@umbc.edu
Description: This is a chessboard where u find the knights best landing area
"""
PIECE_VALUES = {
    "P": 1,
    "B": 3,
    "R": 5,
    "Q": 9,
    "_": 0,
}

KNIGHT_MOVES = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1),
]

BOARD_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h"]

def knight_ai(board, knight_row, knight_col):
    captures = []  # list of (value, move_string)

    for dr, dc in KNIGHT_MOVES:
        new_row = knight_row + dr
        new_col = knight_col + dc

        # Check if on the board
        if 0 <= new_row <= 7 and 0 <= new_col <= 7:
            piece = board[new_row][new_col]
            value = PIECE_VALUES.get(piece, 0)

            if value > 0:
                letter = BOARD_LETTERS[new_col]
                rank = 8 - new_row
                move_str = "N" + letter + str(rank)
                captures.append((value, move_str))

    # Sort captures by value, descending (use a class sorting algorithm here!)
    # Bubble sort: repeatedly swap adjacent pairs if they're out of order
    for i in range(len(captures)):
        for j in range(len(captures) - 1):
            if captures[j][0] < captures[j + 1][0]:  # compare values (index 0 of tuple)
                captures[j], captures[j + 1] = captures[j + 1], captures[j]  # swap

    # Return just the move strings in sorted order
    return [move_str for value, move_str in captures]


if __name__ == "__main__":
    board = []
    for i in range(8):
        board.append(list(input().strip()))

    position = input().strip().split(",")
    knight_row = int(position[0])
    knight_col = int(position[1])

    results = knight_ai(board, knight_row, knight_col)
    print(" ".join(results))