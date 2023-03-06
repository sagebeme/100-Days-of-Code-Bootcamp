# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Combined_name = name1 + name2
Combined_lower = Combined_name.lower()

t = Combined_lower.count("t")
r = Combined_lower.count("r")
u = Combined_lower.count("u")
e = Combined_lower.count("e")

true = t + r + u + e

l = Combined_lower.count("l")
o = Combined_lower.count("o")
v = Combined_lower.count("v")
e = Combined_lower.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
print(love_score)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are aright together.")
else:
  print(f"Your score is {love_score}")
