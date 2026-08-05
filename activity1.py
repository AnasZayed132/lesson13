print("this  generator will print a  angle triangle pointing to the right. ")

n=int(input("how many rows do you want to print."))

for i in range(0,n):
   for j in range(0,i+1):
      print("* ", end="")   
   print()
