'''Problem Statement'''
# Loan Eligibility Check
# A bank considers an applicant eligible for a personal loan
# only if their monthly salary is ₹30,000 or more.
# Write a Python program to accept the applicant's monthly salary
# and display whether they are eligible to apply for the loan.

salary = float(input("Enter your monthly salary: "))

if salary >= 30000:
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.")

'''
Sample Output 1
Enter your monthly salary: 45000
Congratulations! You are eligible to apply for the loan.
'''

'''
Sample Output 2
Enter your monthly salary: 22000
Sorry! You are not eligible to apply for the loan.
'''