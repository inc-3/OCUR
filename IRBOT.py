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
BLUE = "\33[1;94m"
CYAN = "\33[1;96m"
X = f"{GREEN}[\33[1;91m~{GREEN}]"

# LINE
line = "\33[1;94m═" * 40
logo = f"""
{GREEN}
▀█▀ ░█▄─░█ ░█▀▀█ █▀▀█ 
░█─ ░█░█░█ ░█─── ──▀▄ 
▄█▄ ░█──▀█ ░█▄▄█ █▄▄█

{line}
{GREEN}[\33[1;91m~{GREEN}] AUTHOR    {WHITE}  : {GREEN}NIROB RAHMAN
{GREEN}[\33[1;91m~{GREEN}] VERSION    {WHITE} : {GREEN}V{WHITE}/{CYAN}0.1
{GREEN}[\33[1;91m~{GREEN}] FEATURE{WHITE}     :{GREEN} FILE {RED}X {GREEN}RANDOM
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

# Function to save filtered data to a text file
def save_filtered_data(filtered_data, output_file_path):
    with open(output_file_path, 'w') as file:
        for entry in filtered_data:
            file.write(entry + '\n')

# Main function
def main():
    sys.stdout.write('\x1b]2; NIROB~XD \x07')
    line = f"{BLUE}━" * 40
    X = f"{GREEN}[\33[1;91m~{GREEN}]"
    def linex(): print(line)
    def clear(): os.system("clear"); print(logo)
    clear()  # Clear the screen and print the logo
    file_path = input_file_path()
    data = read_data_from_file(file_path)
    filtered_data = filter_bangladeshi_names(data)
    output_file_path = input("Enter the path to save the filtered data: ").strip()
    save_filtered_data(filtered_data, output_file_path)
    print("Filtered data saved successfully!")

# Execute the main function
if __name__ == "__main__":
    main()
