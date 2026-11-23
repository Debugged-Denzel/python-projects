"""
This file contains the solution for the CrossyStreet problem.
It determines if a continuous path of open spaces exists 
from the top row to the bottom row, moving only down and right.

Denzel Asamoah
Denela1@umbc.edu
"""

def crossystreet(grid):
    # If the grid is empty, it's not possible to cross
    if not grid:
        return "pedestrian unfriendly"
    
    row_length = len(grid[0])
    
    # Initialize the reachable array for the top row.
    # We can enter the top row at any open point ('_').
    reachable = []
    for char in grid[0]:
        if char == '_':
            reachable.append(True)
        else:
            reachable.append(False)
            
    # Go through each subsequent row to update what is reachable
    for r in range(1, len(grid)):
        next_reachable = [False] * row_length
        
        # 1. Check if we can move DOWN from the previous row
        for c in range(row_length):
            if reachable[c] and grid[r][c] == '_':
                next_reachable[c] = True
                
        # 2. Check if we can move RIGHT within the current row
        for c in range(1, row_length):
            # If the cell to our left is reachable, and our current cell is open
            if next_reachable[c - 1] and grid[r][c] == '_':
                next_reachable[c] = True
                
        # Update our main reachable list for the next row iteration
        reachable = next_reachable
        
    # If any column in the very last row is True, we made it across!
    if any(reachable):
        return "cross!"
    else:
        return "pedestrian unfriendly"

if __name__ == "__main__":
    # Driver code to gather the input
    grid = []
    line = input()
    
    while line != "stop":
        grid.append(line)
        line = input()
        
    print(crossystreet(grid))