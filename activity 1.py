print("This is a number guessing game form 0-9")
import random 
play=True
number=str(random.randint(0,9))

print("you have an unlimeted amount of guesses but with a catch.\n We wont be telling you if you are warm or cold")



while play:
    guess=input("guess the number")

    if number==guess:
        print("you guessed correct either your lucky or you wasted like 5 minutes guessing")
        break
    else:
        print("you guessed wrong you can continue or stop and go do something else")
        
        

