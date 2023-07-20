import random
#Hint: Remember to import the random module first. 🎲
test_seed = int(input("create a seed number: "))
random.seed(test_seed)

#Write your code below this line 👇
random_side = random.randint(0,1)
if random_side == 1:
   print("Heads")
else:
    print("Tails")
