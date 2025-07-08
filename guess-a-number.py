import random
randomNumber = random.randint(1,100)
while True:
    try:
      guess = int(input("Type a number between 1 to 100 : "))
      if(guess > randomNumber):
        print("High try smaller one")
      elif(guess < randomNumber):
        print("Small try higher one")
      else:
        print("Hurray you guess it")
        break
    except ValueError:
      print("Inter a valid Number")

        

