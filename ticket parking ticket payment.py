print("parking ticket payment helper\n")
def calculated_change(paid,price):
   change= price-paid
   return change
ticket_price=30
print()
print("coins excepted\n")
print("1")
print("5")
print("10")
print("25")

total_inserted=0
coins_inserted=0

while True:
   coin=int(input("Insert a coin (1,5,10,25): "))
   if coin!=1 and coin !=5 and coin!=10 and coin!=25:
    print("invalid input try again\n")
    continue
   total_inserted +=coin
   coins_inserted+=1
   print(f"Inserted {coin}. Total so far: {total_inserted}\n")
   if total_inserted >=ticket_price:
     print("enough money  inserted!\n")
     break
change_due=calculated_change(total_inserted,ticket_price)
if change_due==0:
  pass
else:
  print(f"here's your change:${change_due}\n")
  
   
print("======================")
print("Amount paid:",total_inserted)
print("total change:",change_due)
print("ticket price was $30")
print("Thank you for shopping at anas and eat's")   
print("======================")