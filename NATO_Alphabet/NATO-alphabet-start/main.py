import pandas as pd  # Import Pandas with the alias 'pd'

# Read the CSV file
data = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

# Create a phonetic dictionary from the DataFrame
phonetic_dictionary = {row['letter']: row['code'] for (index, row) in data.iterrows()}

# Get user input and convert it to uppercase
word = input("Enter a word: ").upper()

# Create a list of phonetic codes for each letter in the input word
output_list = [phonetic_dictionary.get(letter, letter) for letter in word]

print(output_list)
