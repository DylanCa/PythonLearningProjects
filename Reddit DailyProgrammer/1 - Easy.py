# Exercise 1 - Easy
# Create a program that will ask the users name, age, and Reddit username.
# Have it tell them the information back, in the format:
# your name is (blank), you are (blank) years old, and your username is (blank)

user_name = input("What's your name, buddy ? \nIt's ... ")
age = input("\nOkay cool. Now, how old are you ?\nI'm ... ")

while True:
    try:
        age = int(age)
        break
    except ValueError:
        print("\nPlease don't be that guy.. Give me just your age, I'm sure you're between 0 and 110 years old.")
        age = input("\nOkay, now give me JUST your age. Like, '26' if you're 26. \nGo on ... ")

user_nickname = input("\nAwesome ! Now, how can I find you on Reddit ?\n I'm u/")

print("Thanks {0}, I now know you are {1} and you Reddit nickname is u/{2} ! :D".format(user_name, age, user_nickname))
