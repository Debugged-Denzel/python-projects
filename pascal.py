"""
File:        pascal.py
Author:      Denzel Asamoah
Date:        10/30/2026
E-mail:      denzela1@umbc.edu
Description: Building pascals triangle
"""
def next_level(level):
    if not level:
        return []
    result = [level[0]]
    for i in range(len(level) - 1):
        result.append(level[i] + level[i + 1])
    result.append(level[-1])
    return result

if __name__ == "__main__":
    in_string = input()

    while in_string != "":
        values = []
        for x in in_string.split():
            values.append(int(x))

        print(next_level(values))
        in_string = input()