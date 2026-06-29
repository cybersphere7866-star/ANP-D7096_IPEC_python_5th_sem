n = int(input("Enter Number of Products: "))

total_bill = 0
highest_cost = -1
lowest_cost = 99999999
highest_product = ""
lowest_product = ""

for i in range(n):
    name = input("Product Name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price Per Unit: "))

    cost = qty * price

    print("Cost =", cost)

    total_bill += cost

    if cost > highest_cost:
        highest_cost = cost
        highest_product = name

    if cost < lowest_cost:
        lowest_cost = cost
        lowest_product = name

print("Total Bill =", total_bill)
print("Most Expensive Product =", highest_product)
print("Cheapest Product =", lowest_product)
print("Average Product Cost =", total_bill / n)