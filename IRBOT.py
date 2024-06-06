import re

# Function to read data from a file
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

# Function to prompt user to input file path
def input_file_path():
    return input("Enter the path to your file: ").strip()

# Define a set of common English names used in Bangladesh
common_bangladeshi_names = {
    "Abdul", "Akhtar", "Ali", "Amin", "Anis", "Asif", "Aziz", "Bashir", 
    "Bilal", "Faisal", "Farhan", "Habib", "Hassan", "Hossain", "Imran",
    "Iqbal", "Jamil", "Kamal", "Karim", "Khan", "Mahmud", "Moin", "Monir", 
    "Nasir", "Nawaz", "Rahim", "Rashid", "Rehman", "Salim", "Sami", "Shahid", 
    "Sharif", "Tariq", "Yasin", "Zaman", "Salman", "Wajid", "Sk", "Bibi", 
    "Rani", "Khatun", "Das", "Bibi", "Kamal", "Mia", "Islam", "Shaikh", 
    "Akter", "Begum", "Hasan", "Hossain", "Jahan", "Khan", "Parvin", 
    "Rahman", "Rashid", "Sultana", "Monirul", "Sahin"
    # Add more common names as needed
}

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
    file_path = input_file_path()
    data = read_data_from_file(file_path)
    filtered_data = filter_bangladeshi_names(data)
    output_file_path = input("Enter the path to save the filtered data: ").strip()
    save_filtered_data(filtered_data, output_file_path)
    print("Filtered data saved successfully!")

# Execute the main function
if __name__ == "__main__":
    main()
