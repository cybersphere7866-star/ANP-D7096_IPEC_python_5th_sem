'''Write a Python program to calculate the total recharge amount based on the data pack selected.'''
data_pack = input("Enter the data pack selected (Basic/Standard/Premium): ")
if data_pack == "Basic":
    cost_per_gb = 10
    number_of_gbs = int(input("Enter the number of GBs: "))
    total_recharge_cost = cost_per_gb * number_of_gbs
elif data_pack == "Standard":
    cost_per_gb = 15
    number_of_gbs = int(input("Enter the number of GBs: "))
    total_recharge_cost = cost_per_gb * number_of_gbs
elif data_pack == "Premium":
    cost_per_gb = 20
    number_of_gbs = int(input("Enter the number of GBs: "))
    total_recharge_cost = cost_per_gb * number_of_gbs
else:
    print("Invalid data pack selected.")
    total_recharge_cost = 0
#output:
print("The total recharge cost is:", total_recharge_cost)

