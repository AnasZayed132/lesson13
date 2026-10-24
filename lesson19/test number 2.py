print("=====FUCTION_CALCULATOR======")
user=input("what operation do you want")

try:
     
     if user == "+":
      user1=int(input("what is the first number you want to input"))
      user2=int(input("what is the second number you want to input"))
      ans=(user1+user2)
      print(f"ANS={ans}")



     if user == "-":
      user1=int(input("what is the first number you want to input"))  
      user2=int(input("what is the second number you  want to input"))
      ans=(user1-user2)
      print(f"ANS={ans}")

     if user == "*":
      user1=int(input("what is the first number you want to input"))
      user2=int(input("what is the second number you  want to input"))
      ans=(user1*user2)
      print(f"ANS={ans}")

    

     if user == "//":
      user1=int(input("what is the first number you want to input"))
      user2=int(input("what is the second number you  want to input"))
      ans=(user1//user2)
      print(f"ANS={ans}")


 
except ValueError:
     print("you need to type in a number")
except ZeroDivisionError:
     print("you can't divide by zero")
 
    



