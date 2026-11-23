"""
This file contains the tictactoe function, which takes a 3x3 board 
and determines if X wins, O wins, or Nobody won.

Author:      Denzel Asamoah
denzela1@umbc.edu
"""

def tictactoe(board):
    # 1. Check all three rows for a horizontal win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            # Removed the leading space here
            return f"{row[0]} wins" 

    # 2. Check all three columns for a vertical win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return f"{board[0][col]} wins"

    # 3. Check the top-left to bottom-right diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return f"{board[0][0]} wins"

    # 4. Check the top-right to bottom-left diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return f"{board[0][2]} wins"

    # If all checks fail
    return "Nobody won"

if __name__ == "__main__":
    line1 = input()
    line2 = input()
    line3 = input()
    board = [line1, line2, line3]
    print(tictactoe(board))