import random

#1 - 10
ran_integer = random.randint(1 , 10)
print(ran_integer)

#0.000000000000 - 0.999999999999
random_float = random.random()
print(random_float)

#prints numbers from 0.999999999 - 4.999999999
random_float = random.random() * 5
print(random_float)

#prints random numbers from 0.999999999 - 4.999999 depending on params
float_int = ran_integer + random_float
print(float_int)

#love Calculator
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")