# Pig Latin
# Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound
# is transposed to the end of the word and an ay is affixed
# (Ex.: "banana" would yield anana-bay).
# Read Wikipedia for more information on rules.

import sys

str_input = input("Enter a word: ")
first_letter = str_input[0]

if (first_letter != "a" and
        first_letter != "e" and
        first_letter != "i" and
        first_letter != "o" and
        first_letter != "u" and
        first_letter != "y"):
    print(str_input[1:] + "-" + str_input[0] + "ay")
else:
    print("Please start your word with a consonant, that's not funny :(")
