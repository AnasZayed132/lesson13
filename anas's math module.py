import random
import math 
print("random fun calculator this will calculate \nwich one of the 5 fun activities you need to do.")

lucky_number=random.randint(1,10)
print("your number is ",lucky_number)

fun=["play a ball game","do sprints","talk to your friend on the phone to see how hes doing ","train","play a game"]

random_activity=random.choice(fun)
print("random activity for the day is ",random_activity)
number=random.randint(1,5)

guess=int(input("guess the number from 1 - 5 ."))
while guess!=number:
    print("you guessed wrong guess again" )
    guess=int(input("guess the number from 1 - 5 ."))
    
    if guess==number:
         print("you guessed right the number was ",number); break
gcd=float(input("enter a decimal number to round"))
up=math.ceil(gcd)
down=math.floor(gcd)
print(f"rounded down it becomes {down} and rounded up its{up}")

y=10
x=-5
copy=math.copysign(y,x)
negative=math.fabs(-100)

print(f"math copy sign can change the sign like negative and positive ex:{copy}\nthen fabs can turn negatives to positives from lets ay 100 to this ex:{negative} ")

num1=int(input("give me a number "))
num2=int(input("give me another number and now i will give the greatest commen divisor"))
gcd=math.gcd(num1,num2)
print("the gcd is",gcd)

print("="*20,"\n")
print("your number was",lucky_number)
print(f"the rounded numbers rounded up and down where{up}and{down}")
print("lastly the math gcd was",gcd,"\n")
print("="*20)