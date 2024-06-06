import os
import sys
import re
import bs4
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from BD import common_bangladeshi_names

# COLOURS
GREEN = "\33[38;5;46m"
WHITE = "\33[1;97m"
RED = "\33[1;91m"
BLUE = "\33[1;97m"
CYAN = "\33[1;97m"
X = f"{WHITE}[\33[1;91m~{WHITE}]"

# LINE
line = "\33[1;97m═" * 40
logo = f"""
{WHITE}
▀█▀ ░█▄─░█ ░█▀▀█ █▀▀█ 
░█─ ░█░█░█ ░█─── ──▀▄ 
▄█▄ ░█──▀█ ░█▄▄█ █▄▄█

{line}
{GREEN}[\33[1;91m~{GREEN}] AUTHOR    {WHITE}  : {GREEN}INCEPTION
{GREEN}[\33[1;91m~{GREEN}] VERSION    {WHITE} : {RED}BETA
{GREEN}[\33[1;91m~{GREEN}] FEATURE{WHITE}     :{GREEN} OUT C UID RMVR
{line}
"""

# Function to read data from a file
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

# Function to prompt user to input file path
def input_file_path():
    return input("Enter the path to your file: ").strip()

def is_bangladeshi(name):
    # Define a regex pattern for Bengali characters
    bengali_pattern = re.compile("[\u0980-\u09FF]")
    # Check if the name contains Bengali characters or is in the common Bangladeshi names set
    return bool(bengali_pattern.search(name)) or any(common_name in name for common_name in common_bangladeshi_names)

# Function to filter out non-Bangladeshi names
def filter_bangladeshi_names(data):
    filtered_data = []
    for entry in data:
        if '|' in entry:
            number, name = entry.split('|', 1)  # Split only at the first occurrence of '|'
            if is_bangladeshi(name):
                filtered_data.append(entry)
        else:
            print(f"Ignoring line: {entry} (Does not contain expected format)")
    return filtered_data

# Function to remove duplicate lines
def remove_duplicate_lines(data):
    return list(set(data))

# Function to sort lines lexicographically in descending order
def sort_lexicographically_descending(data):
    return sorted(data, reverse=True)

# Function to save filtered data to the same file
def save_to_same_file(filtered_data, file_path):
    with open(file_path, 'w') as file:
        for entry in filtered_data:
            file.write(entry + '\n')

# Main function
def main():
    sys.stdout.write('\x1b]2; INCEPTION \x07')
    line = f"{WHITE}━" * 40
    X = f"{WHITE}[\33[1;91m~{WHITE}]"
    def linex(): print(line)
    def clear(): os.system("clear"); print(logo)
    clear()  # Clear the screen and print the logo
    file_path = input_file_path()
    data = read_data_from_file(file_path)
    data = remove_duplicate_lines(data)
    filtered_data = filter_bangladeshi_names(data)
    filtered_data = sort_lexicographically_descending(filtered_data)
    save_to_same_file(filtered_data, file_path)
    print("Filtered data saved successfully!")

# Execute the main function
if __name__ == "__main__":
    main()
