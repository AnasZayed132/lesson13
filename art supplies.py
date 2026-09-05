def greet_customer():
    print("Welcome to the art shop.")
    print("you can get paints, coulers, paper and so much more")

greet_customer

price= float(input("Tell me the price perart item in dollars."))

items=int(input("tell me the amount of items you are getting now!"))

def calculate_total(price,items):
    total=price+items
    return(total)

total=round(calculate_total(price , items))

paid=int(input("what amount did you pay"))

def change(paid,total):
    return(paid-total)

actual_change=change(paid, total)

def thank_you_message(items):
    if items>5:
        print("thank you for this big contribution")
    else:
        print("thank you for buying here.")

print("===reciept of final order===")
print("price per item is ",price)
print("total is ",total)
print("amount paid is",paid)
print("CHANGE DUE IS ",actual_change)
thank_you_message(items)
print("============================")