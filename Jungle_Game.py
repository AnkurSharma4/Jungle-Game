print("                                                     Jungle Game                                                     ")
a=int(input("Press 1 for left  |  Press 2 for right"))
if (a==1):
    b=int(input("Press 3 for left  |  Press 4 for right"))
    if (b==3):
        print("Game Over")
    elif (b==4):
        print("Game Over")
    else:
        print("Game Over")
elif (a==2):
    c=int(input("Press 1 for right  |  Press 2 for left"))
    if (c==1):
       print("Game Over")
    elif (c==2):
        print("Do you want to take help from this stranger?")
        d=int(input("Press 1 to take help  |  Press 2 to deny help"))
        if (d==1):
            print("You Win!")
        elif (d==2):
            print("Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")

