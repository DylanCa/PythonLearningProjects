# Reverse a String
# Enter a string and the program will reverse it and print it out.

import sys

str_input = input("Enter a word: ")

y = len(str_input)
reversed_string = ""

for x in range(0, len(str_input)):
    y = y - 1
    reversed_string += str_input[y]

print(reversed_string)
