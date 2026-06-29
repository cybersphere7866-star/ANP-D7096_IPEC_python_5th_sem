'''Problem Statement'''
# ATM Minimum Balance Check
# A bank requires customers to maintain a minimum balance of ₹5,000 in their savings account.
# Write a Python program that accepts the current account balance from the user.
# If the balance is less than ₹5,000, display a warning message indicating
# that the minimum balance requirement is not maintained.

balance = int(input("Enter Account Balance: "))

if balance < 5000:
    print("Warning! Your account balance is below the minimum required balance of ₹5000.")

'''
Sample Output 1
Enter Account Balance: 3200
Warning! Your account balance is below the minimum required balance of ₹5000.
'''

'''
Sample Output 2
Enter Account Balance: 8000
(No output)
'''