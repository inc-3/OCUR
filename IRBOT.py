import os
import re

os.system('clear')

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
    "Abdul", "Akhtar", "Ali", "Amin", "Anis", "Asif", "Aziz", "Bashir", "Bilal", "Faisal", "Farhan", "Habib", 
    "Hassan", "Hossain", "Imran", "Iqbal", "Jamil", "Kamal", "Karim", "Khan", "Mahmud", "Moin", "Monir", "Nasir", 
    "Nawaz", "Rahim", "Rashid", "Rehman", "Salim", "Sami", "Shahid", "Sharif", "Tariq", "Yasin", "Zaman", "Salman", 
    "Wajid", "Sk", "Rahman", "Hasan", "Jahan", "Parvez", "Shakil", "Shahin", "Sohel", "Tarek", "Sajjad", "Raju", 
    "Shamim", "Sumon", "Shahed", "Shakib", "Arif", "Sabbir", "Noman", "Shafi", "Shah", "Shahriar", "Tanvir", "Rafi", 
    "Masud", "Rafiq", "Rakib", "Sobuj", "Shuvo", "Faruk", "Nayeem", "Mehedi", "Munna", "Anwar", "Kabir", "Shuvo", 
    "Rajib", "Sohag", "Sajib", "Rony", "Sakib", "Shahjalal", "Nasim", "Sakil", "Shuvojit", "Sujon", "Ashik", "Shafiq", 
    "Mahfuz", "Habibullah", "Rasel", "Mizan", "Monir", "Mithun", "Mamun", "Shanto", "Mehrab", "Rubel", "Sumon", "Sabbir", 
    "Razib", "Khairul", "Rafat", "Arafat", "Mahbub", "Nizam", "Biplab", "Pavel", "Arman", "Bijoy", "Shanto", "Hasib", 
    "Ranjan", "Masum", "Liton", "Shamim", "Nazim", "Tuhin", "Arman", "Forhad", "Sakif", "Jabed", "Shakir", "Rifat", 
    "Rakib", "Muntasir", "Biplob", "Tuhin", "Rabbi", "Rab", "Sourav", "Jony", "Partha", "Pavel", "Sohan", "Ratul", 
    "Rabiul", "Rifat", "Mizanur", "Jahid", "Alamin", "Tanjim", "Mahir", "Sajal", "Rifat", "Ratul", 
    "Sarwar", "Shihab", "Rajon", "Jamil", "Rasel", "Ahsan", "Maruf", "Tanveer", "Sajjad", "Rifat", "Saiful", "Shohel", 
    "Tuhin", "Anik", "Shuvo", "Ridoy", "Arafat", "Saif", "Hasib", "Bipul", "Jewel", "Sakib", "Sahed", "Sujon", "Mehedi", 
    "Rafat", "Sakib", "Shihab", "Shamim", "Siam", "Munim", "Sharif", "Rana", "Shamim", "Rana", "Kawsar", "Mahmud", "Akash", 
    "Rafi", "Mahbub", "Munna", "Rasel", "Mehedi", "Shohel", "Rakib", "Nayeem", "Rakib", "Mehedi", "Arafat", "Kawsar", 
    "Tahsin", "Rasel", "Arif", "Biplob", "Rakib", "Sajjad", "Tanzim", "Tuhin", "Mehedi", "Mehedi", "Hasan", "Rasel", 
    "Rakib", "Shamim", "Munna", "Rony", "Fahim", "Mehedi", "Jewel", "Rafsan", "Munna", "Shamim", "Najim", "Rakib", 
    "Najim", "Sabbir", "Shanto", "Biplob", "Mithun", "Shamim", "Nazim", "Mukul", "Tahsin", "Anisur", "Abdus", "Mohammad", 
    "Kazi", "Abul", "Nur", "Nazmul", "Sohel", "Monjur", "Arifur", "Mostafizur", "Kamrul", "Sazzad", "Aminul", "Rashed", 
    "Mahfuzur", "Monirul", "Shafiqul", "Imtiaz", "Enamul", "Fakrul", "Mahmudul", "Samsul", "Abdur", "Farid", "Mizanur", 
    "Jahirul", "Helal", "Shahidul", "Liton", "Rezaul", "Jashim", "Selim", "Anwar", "Motiur", "Azizul", "Golam", "Habiba", "Hanif", "Ibrahim", "Jamal", "Kabir", "Laila", 
    "Mamun", "Kaniz", "Rasheda", "Tasfia", "Tania", "Rifa", "Rimi", "Shathi", "Shantona", "Afrin", "Shila",
    "Sultana", "Mousumi", "Anika", "Rumi", "Anjana", "Nazia", "Shila", "Rina", "Lovely", "Tania",
    "Nipa", "Munni", "Sabiha", "Shanta", "Anisa", "Runa", "Soma", "Bithi", "Laila", "Ferdousi",
    "Jasmine", "Sushmita", "Shapla", "Meher", "Shoma", "Poppy", "Ishrat", "Monika", "Urmila",
    "Tamanna", "Purnima", "Jesmin", "Khadija", "Swapna", "Afroza", "Nila", "Mou", "Sathi", "Rima",
    "Ritu", "Rokhsana", "Mitu", "Khadijah", "Nargis", "Kajol", "Neelima", "Disha", "Sajeda",
    "Shireen", "Luna", "Jhuma", "Keya", "Mariya", "Aklima", "Afroja", "Sohana", "Sraboni", "Arifa",
    "Chandni", "Sadia", "Oishi", "Nishat", "Pushpa", "Puja", "Trisha", "Ria", "Bonna", "Tumpa",
    "Reema", "Zinia", "Ishita", "Arpita", "Alpana", "Mim", "Shima", "Shalini", "Monira",
    "Alifa", "Afifa", "Afsana", "Tithi", "Tumpa", "Sarika", "Munia", "Samira",
    "Moriom", "Tanjina", "Shukria", "Rifa", "Rabeya", "Tahmina", "Jahanara", "Ayesha", "Fatima",
    "Mariam", "Nasrin", "Sabina", "Taslima", "Farzana", "Sharmin", "Rehana", "Suraiya", "Shahnaz",
    "Shahana", "Nusrat", "Sumaiya", "Shabnam", "Md", "Jannat", "Nusrat", "Jahan", "Sex", "Ewr"
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
