try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma :"))
    result = num1/num2
    print("Result is ", result)

except ZeroDivisionError:
    print("Divion by zero dousnt work and is an error!! ")

except SyntaxError:
    print("comma is missing. Enter numbers seperated by comma")

else:
    print("No exceptions ")

finally:
    print("This will execute no matter what")   