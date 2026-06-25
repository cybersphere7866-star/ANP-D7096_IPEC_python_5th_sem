'''Write a program to create average of 5 numbers'''
#Enter the 5 numbers from the user
num1 = float(input("Enter the first number: "))
#validating the first number
if num1 < 0:
    exit("Number cannot be negative. Enter valid number.")
num2 = float(input("Enter the second number: "))
#validating the second number
if num2 < 0:
    exit("Number cannot be negative. Enter valid number.")
num3 = float(input("Enter the third number: "))
#validating the third number
if num3 < 0:
    exit("Number cannot be negative. Enter valid number.")
num4 = float(input("Enter the fourth number: "))
#validating the fourth number
if num4 < 0:
    exit("Number cannot be negative. Enter valid number.")
num5 = float(input("Enter the fifth number: "))
#validating the fifth number
if num5 < 0:
    exit("Number cannot be negative. Enter valid number.")
#calculating average of 5 numbers
average = (num1 + num2 + num3 + num4 + num5) / 5
#displaying the result
print("The average of the 5 numbers is:", average)
