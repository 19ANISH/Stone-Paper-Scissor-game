# Exercise 6 cwh using random module
print("Start Game")
import random
attempts=1
user=0
system=0
while(attempts<=3):
    options=["Stone","Paper","Scissor"]
    a=random.choice(options)
    #print(a)
    print("1.Stone\n"
          "2.Paper\n"
          "3.Scissor\n")
    user_input=(input("Enter your choice:\n"))
    if user_input=='1' and a=='Paper':
            system=system+1
            print("You choose: Stone")
            print("PC choose: ",a)
            print("YOU LOOSE!")
            print("PC WON :(")
    elif user_input=='1' and a=='Scissor':
            user=user+1
            print("You choose: Stone")
            print("PC choose: ", a)
            print("YOU WIN! :)")
            print("PC LOOSE!")
    elif user_input=='1' and a=='Stone':
            print("You choose: Stone")
            print("PC choose: ", a)
            print("DRAW   :|")
    elif user_input=='2' and a=='Paper':
            print("You choose: Paper")
            print("PC choose: ", a)
            print("DRAW   :|")
    elif user_input=='2' and a=="Scissor":
            system=system+1
            print("You choose: Paper")
            print("PC choose: ", a)
            print("YOU LOOSE!")
            print("PC WIN! :(")
    elif user_input=='2' and a=='Stone':
            user=user+1
            print("You choose: Paper")
            print("PC choose: ", a)
            print("YOU WIN! :)")
            print("PC LOOSE!")
    elif user_input=='3' and a=='Paper':
            user=user+1
            print("You choose: Scissor")
            print("PC choose: ", a)
            print("YOU WIN! :)")
            print("PC LOOSE!")
    elif user_input=='3' and a=='Scissor':
            print("You choose: Scissor")
            print("PC choose: ", a)
            print("DRAW   :|")
    elif user_input=='3' and a=='Stone':
            system=system+1
            print("You choose: Scissor")
            print("PC choose: ", a)
            print("YOU LOOSE!")
            print("PC WIN! :(")
    else:
            print("INVALID INPUT\a")
            continue

    print(f"Number of guesses left {3-attempts}")
    #print(b)
    attempts=attempts+1
if attempts>3:
    print("GAME OVER!")


    print(f"Your Score: {user}")
    print(f"PC Score: {system}")
    #print(f"You Won {user} and Computer Won {system}")
if user>system:
        #print(f"You Won {user} and Computer Won {system}")
        print("You Won and Computer Lost :)\n")
elif system>user:
        #print(f"You Won {user} and Computer Won {system}")
        print("Computer Win and You Lose! :(\n")
else:
        print("It's a TIE  :|\n")
"""print(f"You Won {user} and Computer Won {system}")
if user>system:
        # print(f"You Won {user} and Computer Won {system}")
        print("You Won and Computer Lost :)\n")
elif system>user:
        # print(f"You Won {user} and Computer Won {system}")
        print("Computer Win and You Lose! :(\n")
else:
        print("It's a TIE  :|\n")"""
