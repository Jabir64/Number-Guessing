import random
print("YOU HAD ONLY 10 CHANCES TO WIN THE GAME!")
chance = 10
while chance > 0:
    user_input = int(input("type that lucky number to win:"))
    comp = random.randint(1, 10)
    if user_input == comp:
        print("you won the game!!!")
        print("This is the number which get you win", comp)
        break
    else:
        print("you loose")
        print("That unlucky number:", comp)
        chance -= 1
if chance == 0:
    print("get away from the game")
