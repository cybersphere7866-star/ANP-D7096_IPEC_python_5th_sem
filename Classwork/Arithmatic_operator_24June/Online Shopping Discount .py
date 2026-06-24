'''Write a Python program to calculate the final payable amount after applying the discount.'''
total_amount = float(input("Enter the total amount: "))
discount_percentage = float(input("Enter the discount percentage: "))
discount_amount = total_amount * (discount_percentage / 100)
final_payable_amount = total_amount - discount_amount
#output:
print("The final payable amount is:", final_payable_amount)