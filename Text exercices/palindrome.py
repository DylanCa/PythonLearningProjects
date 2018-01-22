# Check if Palindrome
# Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”

str_input = input("Enter a word: ")
palindrome = True

for x in range(0, len(str_input)):
    if str_input[x] != str_input[len(str_input) - ( x + 1 )]:
        palindrome = False
        break

if palindrome:
    print(str_input + " is a palindrome, well done !")

else:
    print(str_input + " isn't a palindrome, try again !")
