import random
while True:
    print("====NUMBER GUSSING GAME=====")
    print("gusses any number between 1 to 100")
    player=int(input("enter your number:"))
    if 1<=player<=100:
        print("your gusse is:",player)
    else:
        print("enter the correct number")
    computer=random.randint(1,100)
    print("computer guesses:",computer)
    if player == computer:
        print("you are win🥳")
    else:
        print("you are losse😵")
    choose=input("do you want play again[yes/no]:")
    if choose == "no":
        print(".....GAME OVER.....")
        break
