"""
This file reads log entries from the user and writes them to a specified 
file, prepending a date prefix to each line.

Denzel Asamoah
denzela1@umbc.edu
"""

def logger(filename_to_write, prefix, records):
    # Open the specified file in write mode
    with open(filename_to_write, "w") as file:
        # Loop through each record and write it to the file with the prefix
        for record in records:
            file.write(f"{prefix}: {record}\n")


if __name__ == "__main__":
    # Read the first line as the date (the prefix)
    date_prefix = input()
    
    # Read the second line as the file name
    file_name = input()
    
    # Collect record lines until the user enters "stop"
    log_records = []
    current_line = input()
    
    while current_line != "stop":
        log_records.append(current_line)
        current_line = input()
        
    # Call the logger function to write the collected records to the file
    logger(file_name, date_prefix, log_records)