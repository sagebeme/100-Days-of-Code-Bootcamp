# 🚨 Don't change the code below 👇
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if height >= 120:
  print("you can ride the rollercoaster!!")
  age = int(input("what is your age? "))
  if age < 12:
    print("you'll pay $5 to ride")
  elif age <= 18:
    print("you'll pay $7 to ride")
  else:
    print("you'll pay $12 to ride")
else:
  print("Not tall enough to ride")


