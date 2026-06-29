'''Problem Statement'''
# Parking Fee Waiver
# A shopping mall waives the parking fee if a customer has made
# purchases worth ₹2,000 or more.
# Otherwise, the customer must pay a parking fee of ₹100.
# Write a Python program to accept the purchase amount
# and display whether the parking fee is waived or payable.

purchase = float(input("Enter the purchase amount: "))

if purchase >= 2000:
    print("Parking Fee Waived!")
    print("Parking Fee: ₹0")
else:
    print("Parking Fee Applicable!")
    print("Parking Fee: ₹100")

'''
Sample Output 1
Enter the purchase amount: 2500
Parking Fee Waived!
Parking Fee: ₹0
'''

'''
Sample Output 2
Enter the purchase amount: 1500
Parking Fee Applicable!
Parking Fee: ₹100
'''