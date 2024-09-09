#original code write by INCEPTION
import os
import sys
import re
from bs4 import BeautifulSoup
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
{WHITE}[\33[1;91m~{WHITE}] AUTHOR    {WHITE} :  {GREEN}INCEPTION
{WHITE}[\33[1;91m~{WHITE}] VERSION   {WHITE} :  {RED}BETA
{WHITE}[\33[1;91m~{WHITE}] FEATURE   {WHITE} : {WHITE} OUT C UID RMVR
{line}
"""

# Function to read data from a file
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

# Function to prompt user to input file path
def input_file_path():
    custom_path = input("Would you like to input a custom file path? (y/n): ").strip().lower()
    if custom_path == 'y':
        return input("Enter the path to your file: ").strip()
    else:
        return ['/sdcard/1.txt', '/sdcard/2.txt', '/sdcard/3.txt', '/sdcard/4.txt',
                '/sdcard/5.txt', '/sdcard/6.txt', '/sdcard/7.txt', '/sdcard/8.txt']

def is_bangladeshi(name):
    # Define a regex pattern for Bengali characters
    #bengali_pattern = re.compile("[\u0980-\u09FF]")
    # Check if the name contains Bengali characters or is in the common Bangladeshi names set
    return any(common_name in name for common_name in common_bangladeshi_names)

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
    file_paths = input_file_path()
    if isinstance(file_paths, str):  # If a single custom file path is provided
        file_paths = [file_paths]
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        data = read_data_from_file(file_path)
        data = remove_duplicate_lines(data)
        filtered_data = filter_bangladeshi_names(data)
        filtered_data = sort_lexicographically_descending(filtered_data)
        save_to_same_file(filtered_data, file_path)
        print(f"Filtered data saved successfully for {file_path}!")

# Execute the main function
if __name__ == "__main__":
    main()
