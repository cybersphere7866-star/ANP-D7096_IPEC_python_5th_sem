#Write a program to create a function which works as a calculator for addition, subtraction, multiplication and division.
#function to calculate addition of the number 
def calculate_addtion(num1, num2):
    return num1 + num2
#----------------------------------
#function to calculate subtraction of the number
def calculate_subtraction(num1, num2):  
    return num1 - num2          
#------------------------------------
#function to calculate multiplication of the number
def calculate_multiplication(num1, num2):
    return num1 * num2
#------------------------------------
#function to calculate division of the number
def calculate_division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."
    