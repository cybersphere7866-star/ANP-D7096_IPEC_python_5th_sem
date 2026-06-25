'''Write a program to multiply two numbers and validate it.'''
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
#calculating multiplication of two numbers
multiplication = num1 * num2
#displaying the result
print("The multiplication of the two numbers is:", multiplication)
