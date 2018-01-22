# Count Words in a String
# Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.

str_input = input("Enter a sentence: ")

print("That's a " + str(len(str_input.split(" "))) + "-words sentence, right ?")