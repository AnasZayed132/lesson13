print("part 1")
print("="*30)
print("grocery comparison tool")
print("="*30)
rice_price=12
milk_price=4
fruit_price=8
number_of_baskets=2
family_members=4
print("rice_price=12\n milk_price=4\n fruit_price=8\n number_of_baskets=2 \nfamily_members=4")

(milk_price +rice_price +fruit_price)*number_of_baskets/family_members
print("part 2")
total_items=int(input("Enter the number of grocery items:"))
people=int(input("Enter the amount of people sharing them:"))
if total_items >0:
    print("no errors here move on")


elif  people==0: 
    print("you can share woth 0 people")

if total_items%people==0:
    print("you can devide equally between", people,"people-",total_items//people,"each.")
else:
    print(total_items, "items do not divide equally between ",people,"people-",total_items%people,"left over")
print("part 3")
recorded_total=260
corrected_total=290
corrected_weekly_average=72.5
print("recorded_total=260 \ncorrected_total=290\n corrected_weekly_average=72.5")
print("part 4")
store_a=70
store_b=75
store_c=80
print("store_a=70")
print("store_b=75")
print("store_c=80")
average_of_all_stores=(store_a+store_b+store_c)/3

print("===SUMMARY===\n")
print("Correct cost per person = 12.0")
print("Correct weekly average=",average_of_all_stores)
print("verdict              :somewhere\nin between the three stores")
print("="*13)