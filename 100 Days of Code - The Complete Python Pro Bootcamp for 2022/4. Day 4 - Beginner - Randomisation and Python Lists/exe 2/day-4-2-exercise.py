import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇

#getting names in the list
num_names = len(names)

#Generate random numbers between 0 and the last index.
rand_choice = random.randint(0, num_names - 1)

#picking the person who'll foot the bill in using the random choice
person_paying = names[rand_choice]

print(f"{person_paying} is paying our bill for our meal")

#another way to go around it which we weren't allowed to
print(random.choice(names) + " is paying for our meal")


