import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

data = pd.read_csv("nato_phonetic_alphabet.csv")
dict_alpha = {row.letter: row.code for (index, row) in data.iterrows()}

print(dict_alpha)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Your name?")

user_characters = list(user_word.upper())

nato_list = [dict_alpha[name] for name in user_characters]

print(nato_list)