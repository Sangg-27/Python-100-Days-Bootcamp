#Day 3 TREASURE ISLAND 
#The goal is to find the trasure from the image below , I have used control statements.

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

choice_1 = input('Your in a situation to choose between left or right ! Go ahead and make a wise choice.Type "left" or "right".\n').lower()

if choice_1 == "left":
    choice_1_result = print("Hooray ! You have passed the level 1.")
    choice_2 = input('Now you have to cross the island ! Do you want to wait or swim. Type "wait" or "swim".\n').lower()
    if choice_2 == "wait":
       choice_2_result = print("Congratulations ! You have come the last level !")
       choice_3 = input('There are three doors before you. RED , BLUE and YELLOW. What are you going to choose.'
       'Type "Red", "Blue" or "Yellow".\n').lower()
       if choice_3 == "red":
        print("You have lost your game. Could have made a different choice!")
       elif choice_3 == "blue":
        print("Yayyyy !! You have found the treasure. Good job.")
       else:
        print("Sorry ! You have lost your game !")
    else:
        print("Oopsie ! You waited and your dead now. Game over.")
else:
    print("You have fell into a hole ! Sorry Try again")

#OUTPUT
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

Welcome to Treasure Island.
Your mission is to find the treasure.
Your in a situation to choose between left or right ! Go ahead and make a wise choice.Type "left" or "right".
left
Hooray ! You have passed the level 1.
Now you have to cross the island ! Do you want to wait or swim. Type "wait" or "swim".
wait
Congratulations ! You have come the last level !
There are three doors before you. RED , BLUE and YELLOW. What are you going to choose.Type "Red", "Blue" or "Yellow".
blue
Yayyyy !! You have found the treasure. Good job.

