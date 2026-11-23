"""
This file implements a Ctrl-F search function to find the first occurrence 
of a word in a text file, returning the line number and character offset.

Denzel Asamoah
Denzela1@umbc.edu
"""

def ctrlf(filename, word_to_find):
    # Make the search target case-insensitive
    word_to_find = word_to_find.lower()
    
    try:
        with open(filename, 'r') as file:
            # enumerate(..., 1) keeps track of the line number starting at 1
            for line_num, line in enumerate(file, 1):
                
                # Remove the trailing newline character so the last word matches cleanly
                line = line.replace('\n', '')
                
                # Split strictly by spaces to handle exact space separation
                words = line.split(' ')
                current_offset = 1
                
                for word in words:
                    # Check if the lowercased word matches what we're looking for
                    if word.lower() == word_to_find:
                        return f"{line_num} {current_offset}"
                    
                    # If it doesn't match, shift the offset by the word's length + 1 (for the space)
                    current_offset += len(word) + 1
                    
    except FileNotFoundError:
        # If the file doesn't exist, it should gracefully fall through and return "not found"
        pass
    
    return "not found"

if __name__ == "__main__":
    # Driver code to handle the exact inputs and outputs from the test cases
    filename_input = input()
    target_word = input()
    print(ctrlf(filename_input, target_word))