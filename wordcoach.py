"""
File:        wordcoach.py
Author:      Denzel Asamoah
Date:        11/5/2026
Section:     1471
E-mail:      denzela1@umbc.edu
"""

def wordcoach(lines):
    newlist = []
    tempCount = 0
    mostCommon = ""
    
    #go through each line given to us by the user then for every word in the line we will append a lower and split version of the word to newList after we stripped it of any quotation
    for line in lines:
        for word in line.lower().split():
            newlist.append(word.strip(",.!?;:'"))

    for word in newlist:
        if newlist.count(word) > tempCount:
            tempCount = newlist.count(word)
            mostCommon = word
    return mostCommon


    


        

  

if __name__ == "__main__":
    lines = []
#if we put in a line it will append the line to lines but we need a way to even split the lines in lines
    line = input()
    while line != "stop":
        lines.append(line)
        line = input()

    print(wordcoach(lines))