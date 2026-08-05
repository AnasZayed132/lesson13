rows=int(input("how many rows"))
number=1
print("Floyd's Triangle")

for r in range(1,rows+1):
    for i in range(1,r+1):
       print(number,end=" ")
       number=number+1
    print()
