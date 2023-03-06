print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("You are at a Crossroad, which direction do you want to go? Type \"left\" or \"right\". ")
direction = direction.lower()
if direction == "left":
  print("You arrived at a lake there's info about the lake you don't know.")
  swimorwait = input("do you want to swim or wait?")
  if swimorwait == "wait":
    swimorwait = swimorwait.lower()
    threedoors=input("you got to the island safely there are three doors Red, Blue and Yellow which will you pick?")
    if threedoors == "yellow":
      print("congratulations you got to the treasure")
    elif threedoors == "red":
      print("well welcome to the dungeon. You just failed by a whisker to get the treasure")
    elif threedoors == "blue":
      print("you picked the blue door this was leading you to the Kraken welcome to your demise")
    else:
      print("you picked a door that doesn't exist")
  else:
    print("you should have decided to wait, you just jumped in an acidic lake your're dead try again")
else:
  print("You picked right and walked into a big hole")
