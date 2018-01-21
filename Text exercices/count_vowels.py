# Count Vowels
# Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

import sys

vowels = {"a": 0, "e" : 0, "i": 0, "o": 0, "u": 0, "y": 0}
total_vowel = 0

for x in range(0, len(sys.argv[1])):
    if sys.argv[1][x] == "a":
        vowels['a'] += 1

    elif sys.argv[1][x] == "e":
        vowels['e'] += 1

    elif sys.argv[1][x] == "i":
        vowels['i'] += 1

    elif sys.argv[1][x] == "o":
        vowels['o'] += 1

    elif sys.argv[1][x] == "u":
        vowels['u'] += 1

    elif sys.argv[1][x] == "y":
        vowels['y'] += 1


for idx, val in enumerate(vowels):
    print("Number of vowel '" + str(val) + "': " + str(vowels[val]))
    total_vowel += vowels[val]

print("Total number of vowel:" + str(total_vowel))
