print("===hw tracker===\n")
hw_1="math hw"
hw_2="science hw"
hw_3="english hw"
hw_4="history hw"

hw_completed=int(input("Enter the number of homework assignments completed: "))
while hw_completed<=4:
    if hw_completed==0:
        print("you have 4 home works left ")   
        hw_completed=int(input("Enter the number of homework assignments completed: "))
    elif hw_completed==1:
        print("congrats you finished a hw you have 3 more left ")
        hw_completed=int(input("Enter the number of homework assignments completed: "))

    elif hw_completed==2:
        print("congrats you have finished 2 home works your half way to completing all of your hw.")
        hw_completed=int(input("Enter the number of homework assignments completed: "))

    elif hw_completed==3:
        print("congrats you have one hw left.")
        hw_completed=int(input("Enter the number of homework assignments completed: "))

    elif hw_completed==4:
        print("congrats you have finished all of your hw you can go relaxe now.") 
        break
        

    else:
        print("reminder you just need to write the number of assignmets left .")
