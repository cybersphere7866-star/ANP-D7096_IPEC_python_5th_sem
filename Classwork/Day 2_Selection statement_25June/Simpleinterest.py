'''To calculate simple interest'''
#input of principal from the user
principal = float(input("Enter the principalIin Rs): "))
#validating the principal amount
if principal < 0:
    exit("principal amoung cannot be nagative.")
#input of rate of interest from the user
rate = float(input("Enter the rate of interest (in %): "))
#validating the rate of interest
if rate < 0:
    exit("Rate of interest cannot be negative.")
#input of time from the user
time = int(input("Enter the time (in years): "))
#validating the time
if time < 0:
    exit("Time cannot be negative.")
#--------------------------------------------------------------
#displaying data to the user
print("Principal: Rs", principal)
print("Rate of interest is:", rate, "%")
print("Time is:", time, "years")
#--------------------------------------------------------------
#displaying data to the user
simple_interest = (principal * rate * time) / 100
#displaying the result
print("The simple interest is:", simple_interest)
'''Output:
Enter the principal (in Rs): 10000
Enter the rate of interest (in %): 5
Enter the time (in years): 2
Principal: Rs 10000.0
Rate of interest is: 5.0 %
Time is: 2 years
The simple interest is: 1000.0
'''


    