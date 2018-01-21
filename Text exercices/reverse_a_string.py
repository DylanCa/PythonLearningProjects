# Reverse a String
# Enter a string and the program will reverse it and print it out.

import sys

y = len(sys.argv[1])
reversed_string = ""

for x in range(0, len(sys.argv[1])):
    y = y - 1
    reversed_string += sys.argv[1][y]

print(reversed_string)
