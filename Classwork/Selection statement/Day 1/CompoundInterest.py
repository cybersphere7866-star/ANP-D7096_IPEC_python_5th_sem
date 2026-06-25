'''Write a program to calculate compound interest and validate it.'''
#Enter the principal amount from the user
principal = float(input("Enter the principal (in Rs): "))
#validating the principal amount
if principal < 0:
    exit("Principal amount cannot be negative. Enter valid principal amount.")
#Enter the rate of interest from the user
rate_of_interest = float(input("Enter the rate of interest( in % ): "))
#validating the rate of interest
if rate_of_interest < 0:
    exit("Rate of interest cannot be negative. Enter valid rate of interest.")
#Enter the time period from the user
time_period = float(input("Enter the time period in years: "))
#validating the time period
if time_period < 0:
    exit("Time period cannot be negative. Enter valid time period.")
#Calculating compound interest
compound_interest = principal * (1 + rate_of_interest / 100) ** time_period - principal
#displaying the result
print("The compound interest is:", compound_interest)
