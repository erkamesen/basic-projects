# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


## İŞLEMLERİMİZİ FONKSİYON İÇİNE ALIP HATAYA FONKSİYONU YAZARSAK DOĞRU OLANA KADAR İŞLEM YAPAR.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please ")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()


