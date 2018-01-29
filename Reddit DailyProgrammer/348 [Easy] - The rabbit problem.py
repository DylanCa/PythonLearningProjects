"""
Exercise 348 [Easy] - The Rabbits problem - NOT WORKING PROPERLY !
https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/

Starting with a small population of male and female rabbits
We have to figure out how long it will take for them to outnumber humans 2:1.
Every month a fertile female will have 14 offspring (5 males and 9 females).
A female rabbit is fertile when it has reached the age of 4 months, they never stop being fertile.
Rabbits die at the age of 8 years (96 months).
"""

male_rabbits = []
female_rabbits = []

month_spent = 0

for x in range(0, int(input("How many male rabbits ?"))):
    male_rabbits.append(2)

for y in range(0, int(input("How many female rabbits ?"))):
    female_rabbits.append(2)

max_rabbits = int(input("How many rabbits do you want ?"))
dead_male = 0
dead_female = 0

while len(male_rabbits) + len(female_rabbits) < max_rabbits:

    for i in range(0, len(male_rabbits)):
        male_rabbits[i] = male_rabbits[i] + 1
        if male_rabbits[i] >= 94:
            for j in range(i, len(male_rabbits)):
                male_rabbits.pop(i)
                dead_male = dead_male + 1
        break

    for i in range(0, len(female_rabbits)):
        female_rabbits[i] = female_rabbits[i] + 1
        if female_rabbits[i] >= 94:
            for j in range(i, len(female_rabbits)):
                female_rabbits.pop(i)
                dead_female = dead_female + 1
            break

        elif female_rabbits[i] >= 4:
            for j in range(0, 5):
                male_rabbits.append(2)
            for k in range(0, 9):
                female_rabbits.append(2)

    month_spent = month_spent + 1
    print("Month n°" + str(month_spent), end=" - ")
    print("There\'s {0} rabbits alive ({1} males and {2} females)".format(str(len(male_rabbits) + len(female_rabbits)),
                                                                          str(len(male_rabbits)),
                                                                          str(len(female_rabbits))))
    print("This month, {0} and {1} died from old age ({2} total)".format(str(dead_male),
                                                                         dead_female,
                                                                         dead_male + dead_female))
