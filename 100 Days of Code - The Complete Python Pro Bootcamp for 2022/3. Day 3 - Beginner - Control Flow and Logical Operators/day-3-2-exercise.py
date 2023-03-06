# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight/(height**2))
if BMI < 18.5:
  print(f"your BMI is {BMI},you are Under 18.5 you are underweight")
elif BMI < 25:
  print(f"your BMI is {BMI},you are Over 18.5 but below 25 you have a normal weight")
elif BMI < 30:
  print(f"your BMI is {BMI},you areOver 25 but below 30 you are slightly overweight")
elif BMI < 35:
  print(f"your BMI is {BMI},you areOver 30 but below 35 you are obese")
else:
  print(f"your BMI is {BMI},you are Above 35 you are clinically obese.")
