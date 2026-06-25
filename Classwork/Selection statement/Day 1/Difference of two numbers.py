'''Write a program to calculate the difference of two numbers'''
#Enter the first number from the user
num1 = float(input("Enter the first number: ")) 
#validating the first number
if num1 < 0:
    exit("Number cannot be negative. Enter valid number.")
#Enter the second number from the user
num2 = float(input("Enter the second number: "))
#validating the second number
if num2 < 0:
    exit("Number cannot be negative. Enter valid number.")
#calculating difference of two numbers
difference = num1 - num2
#displaying the result
print("The difference of the two numbers is:", difference)
