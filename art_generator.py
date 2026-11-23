"""
File:        art_generator.py
Author:      Denzel Asamoah
Date:        10/30/2026
E-mail:      denzela1@umbc.edu
Description: Making art using the size of certain characters and numbers 1-10
"""
def art_generator(values):
    fills = ".,:;=*#%@$"
    if not values:
        return ""
    smallest = min(values)
    largest = max(values)
    if smallest == largest:
        return "*" * len(values)
    out = []
    for v in values:
        index = int((v - smallest) * 9 / (largest - smallest))
        out.append(fills[index])
    return "".join(out)

if __name__ == "__main__":
    import sys
    while True:
        try:
            line = input()
        except EOFError:
            break
        line = line.strip()
        if line == "":
            break
        nums = [int(x) for x in line.split()]
        print(art_generator(nums))