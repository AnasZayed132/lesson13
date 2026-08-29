print("=====Hello Welcome To My Lemonade Stand =====\n")

def greet_customer():
        print("welcome to the lemonade stand!")

        print("Fresh lemonade,made just for you.")

price_per_cup=float(input("enter the price per cup in dollars:"))
cups_sold=int(input("Enter the number of cups sold:"))

def calculated_total(price,cups):
        total=price*cups
        return total
total_cost=calculated_total(price_per_cup, cups_sold)

rounded_total=round(total_cost,2)
print("Total Cost:", rounded_total)

amount_paid=float(input("enter the amount paid by the customer: "))

def calculated_change(paid,total):
        change= paid -total
        return change
change_due= calculated_change(amount_paid, rounded_total)
rounded_change= round(change_due, 2)

def thank_you_message(cups):
        if cups >= 5 :
                return "Wow big order thank you for the support !"
        else:
                return "Thank yoyu for stopping by the stand!"
closing_message= thank_you_message(cups_sold)

print("")
print("======LEMONADE STAND RECEIPT=====")
print("Price Per Cup:",cups_sold)
print("Total_Cost:",rounded_total)
print("Amount Paid:",amount_paid)
print("Change Due:", rounded_change)
print(closing_message)
print("================================")