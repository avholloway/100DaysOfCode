# TODO 1. Create dictionary {"a": "alpha", ...}

import pandas

df = pandas.read_csv("day26alpha.csv")

nato_alpha = {row.letter:row.code for _, row in df.iterrows()}

print(nato_alpha)

# TODO 2. Create list of phonetic alphabet from user input

while (user_input := input("Word: ").upper()) != "EXIT":
    print("\n".join([nato_alpha[letter] for letter in user_input]))