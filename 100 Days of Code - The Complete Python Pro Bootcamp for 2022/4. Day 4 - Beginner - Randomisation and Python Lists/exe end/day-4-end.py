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


#Cities in Kenya
Kenyan_cities = ["Nairobi",
"Mombasa",
"Kisumu",
"Nakuru",
"Eldoret",
"Thika",
"Nyeri",
"Machakos",
"Malindi",
"Kitale",
"Garissa",
" Kakamega",
"Voi",
"Lamu",
"Meru",
"Embu",
"Narok",
"Bungoma",
"Homa Bay",
"Kericho"]

print(Kenyan_cities)

Kenyan_cities.append("Kisumu")

print("\n")
Kenyan_cities[2] = "Kiambu"

print(Kenyan_cities)