deposit = 0
withdrawal = 0
balance = 0

while True:
    amount = float(input("Enter Transaction (0 to Stop): "))

    if amount == 0:
        break

    if amount > 0:
        deposit += amount
    else:
        withdrawal += abs(amount)

    balance += amount

print("Total Deposit =", deposit)
print("Total Withdrawal =", withdrawal)
print("Final Balance =", balance)