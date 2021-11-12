import pandas

df_nato = pandas.read_csv('nato_phonetic_alphabet.csv')
code_dict = {row.letter: row.code for (index, row) in df_nato.iterrows()}
name = input("Please enter the word you want to translate to the NATO Alphabet: ").upper()

out = [code_dict[letter] for letter in name]
print(out)