import random 
while True:
    user_move=input("Enter a choice (rock, paper or scissors)")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print(f"\nYou chose {user_move}, computer chose {computer_action}.\n")

    if user_move == computer_action:
        print("both players chose",user_move,"its a tie!")
    
    elif user_move=="rock":
        if computer_action=="scissors":
            print("Rock smashes scissors, you wo n    ")
            
        else:
            print("you lost rock gets covered by paper")
            
    elif user_move=="paper":
            if computer_action=="rock":
                print("paper covers rock you win")
            else:
                print("scissor cuts paper you lost")
                

    elif user_move=="scissors":
            if computer_action=="paper":
                print("scissors slices up paper you won")
            else:
                print("rock destroyes scissors you lost")
    play_again=input("Play again yes or no ")
    if play_again!="yes":
         break
    