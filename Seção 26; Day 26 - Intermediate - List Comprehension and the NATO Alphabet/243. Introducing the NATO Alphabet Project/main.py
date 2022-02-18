import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data_frame = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word_input = input("Enter a word to get its corresponding NATO Alphabet translation:\nWord -->  ").upper()
letter_list = [nato_dict[letter] for letter in word_input]
print(letter_list)
