import random
choices = ("r", "p", "s")
emoji = {"r":"🪨", "p":"📃", "s": "✂️"}
while True:
    users_input = input("Inter guess = Rock, Paper, Scissor (r/p/s) : ")
    computer_choice = random.choice(choices)
    if(users_input == "n"):
        break
    elif(users_input not in choices):
       print("inter a valid guess")
    elif(users_input == computer_choice):
       print("Tie !! 😕😕")
    elif(
        ((users_input == "p" and computer_choice == "s") 
       or(users_input == "r" and computer_choice == "p") 
       or(users_input == "s" and computer_choice == "r"))):
        print(f'user:{emoji[users_input]}  computer: {emoji[computer_choice]}')
        print("computer win you lose 🥹🥲")

    else:
        print(f'user:{emoji[users_input]}  computer: {emoji[computer_choice]}')
        print("you win 🥳🎉🎊")
