
num1 = int(input("Enter a number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

if num1 > num2:
    if num1 > num3:
        print(str(num1)+" is the greatest.")
    elif num1 < num3:
        print(str(num3)+" is the greatest.")
else:
    if num2 > num3:
        print(str(num2)+" is the greatest.")
    elif num2 < num3:
        print(str(num3)+" is the greatest.")