# game settings
secret=39
max_attempts=5
# setup
count=0
guess=0
print("=" * 42)
print("I have a secret number from 1 to 50 guess it and win the game dont and stay a loser for the rest of your life. \n After each bad guess i will tell you if your guess is hot or cold now let the games start.")
print("=" * 42)
# main game loop
while count < max_attempts and guess != secret:
 
 guess = int(input("Your guess:"))
 count=count+1
 if guess ==secret:
  print("\n Correct! You guessed it in", count, "attempt(s)!")
  print("finally i was worried you left ")
# diff caluculators
 else:
  if guess>secret:
   diff = guess-secret
  else:
   diff = secret-guess
# hint levels
 if diff>=20:
  print("yo this is freezing your not good at this")
 elif diff>=10:
  print("cold but still you are not doing good")
 elif diff>=1:
  print("warm not that bad still not there")
 else:
  print("you did it woohoo ladida its not much of an achievment ")

 
# remaining lives
remaining=max_attempts - count 
if max_attempts==0:
 print("your a looser you had 5 chances bro!")
elif max_attempts == 1:
 print("you have one last try come on i dont believe in you")
elif max_attempts == 2:
 print("you have 2 tries left carefull.")
elif max_attempts == 3:
 print("3 tries left okay!")
elif max_attempts == 4:
 print("4 tries left come on man")
elif max_attempts == 5:
 print("5 tries left carefull you have a chance")

# game over check
if guess != secret:
 print("="*5)
 print("you lost game over your chances went bye bye. \n the secret number was ",secret)
 print("The annoyed talk was for experimental purposes only.")
 print("="*5)
