'''Write a Python program to calculate the value of money after a certain number of years assuming it doubles every year. '''
initial_amount = float(input("Enter the initial amount of money: "))
years = int(input("Enter the number of years: "))
final_amount = initial_amount * (2 ** years)
#output:
print("The value of money after", years, "years is:", final_amount)
