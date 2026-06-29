n = int(input("Enter Number of Houses: "))

total = 0
highest = -1
lowest = 999999

for i in range(n):
    units = int(input("Enter Units: "))

    total += units

    if units > highest:
        highest = units

    if units < lowest:
        lowest = units

average = total / n

print("Total Units =", total)
print("Average =", average)
print("Highest =", highest)
print("Lowest =", lowest)