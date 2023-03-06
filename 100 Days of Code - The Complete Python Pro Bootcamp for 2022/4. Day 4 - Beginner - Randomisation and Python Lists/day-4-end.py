import random

random.seed(123)
#1 - 10
random_integer = random.randint(1 , 10)
print(random_integer)

#0.000000000000 - 0.999999999999
random_float = random.random()
print(random_float)

#prints numbers from 0.999999999 - 4.999999999
random_float = random.random() * 5
print(random_float)
