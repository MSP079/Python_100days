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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to Treasure Island!!!")
print("Your mission is to find the treasure")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right":').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to lake. '
    'There is an island in the middle of the lake. '
    'Type "wait" to wait for a boat:'
    'Type "swim" to swim across ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is house with 3 doors. One Red, one Blue, one Yellow. Which color do you choose").lower()
        if choice3 == "red":
            print("It's a room full of fire: Game over")
        elif choice3 == "yellow":
            print("You found the treasure: You win>>>")
        elif choice3 == "blue":
            print("You enter a room full of beast: Game over")
        else:
            print("You choose a different door: ")
    else:
        print("You got attacked by an angry trout. Game over")
else:
    print("You fell into a Hole: Game Over")