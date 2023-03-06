import random

#1 - 10
random_integer = random.randint(1 , 10)
print(random_integer)

#0.000000000000 - 0.999999999999
random_float = random.random()
print(random_float)

#prints numbers from 0.999999999 - 4.999999999
random_float = random.random() * 5
print(random_float)

#love Calculator
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")