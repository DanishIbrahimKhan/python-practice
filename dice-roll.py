import random
while True:
    choice = input("want to roll a dice (y/n)").lower()
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if(choice == "y"):
       print("dice :",die1, die2)
    elif(choice == "n"):
       print("thank you for playing!")
       break
    else:
       print("please type y or n")

