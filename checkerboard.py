"""
File:        checkerboard.py
Author:      Denzel Asamoah
Date:        10/30/2026
E-mail:      denzela1@umbc.edu
Description: This file is to print a checkerboard pattern using two characters separated by a space
"""

def checkerboard(size, symbol_1, symbol_2):
    for i in range(size):
        for x in range(size):
            if (x+i) % 2 == 0:
                print(symbol_1, end="")
            else:
                print(symbol_2, end="")
        print()
    pass
    

if __name__ == "__main__":
    size = int(input())
    symbols = input().split()
    checkerboard(size, symbols[0], symbols[1])