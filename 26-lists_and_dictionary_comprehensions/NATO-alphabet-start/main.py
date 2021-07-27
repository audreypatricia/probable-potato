# TODO 1. Create a dictionary in this format:
with open("nato_phonetic_alphabet.csv") as file:
    data = file.readlines()
    final_data = []
    for code in data[1:]:
        final_data.append(code.strip())

NATO_dict = {code.split(',')[0]: code.split(',')[1] for code in final_data}
print(NATO_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Enter your name: ")
phonetic_code = []
for char in user_name:
    phonetic_code.append(NATO_dict[char.upper()])

print(phonetic_code)


# Solutions
# import pandas
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# NATO_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#
# word = input("Enter a word: ").upper()
# phonetic_code = [NATO_dict[letter] for letter in word]
# print(phonetic_code)
