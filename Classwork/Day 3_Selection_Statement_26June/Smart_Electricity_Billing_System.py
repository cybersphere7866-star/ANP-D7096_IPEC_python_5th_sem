# Smart Electricity Billing System

# Get input from user
units = float(input("Units Consumed: "))
consumer_type = input("Consumer Type (Residential/Commercial): ")
senior_citizen = input("Senior Citizen (Y/N): ").upper()

# Calculate base bill using tiered rates
if units <= 100:
    base_bill = units * 5
elif units <= 300:
    base_bill = (100 * 5) + ((units - 100) * 7)
else:
    base_bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

print(f"Base Bill: ₹{base_bill}")

# Apply commercial charge (20% extra)
commercial_charge = 0
if consumer_type.lower() == "commercial":
    commercial_charge = base_bill * 0.20
    print(f"Commercial Charge: ₹{commercial_charge}")

# Calculate bill after commercial charge
bill_after_commercial = base_bill + commercial_charge

# Apply surcharge if bill > 5000 (5%)
surcharge = 0
if bill_after_commercial > 5000:
    surcharge = bill_after_commercial * 0.05
    print(f"Surcharge: ₹{surcharge}")

# Calculate bill after surcharge
bill_after_surcharge = bill_after_commercial + surcharge

# Apply senior citizen discount (10%)
senior_discount = 0
if senior_citizen == 'Y':
    senior_discount = bill_after_surcharge * 0.10
    print(f"Senior Citizen Discount: ₹{senior_discount}")

# Calculate final bill
final_bill = bill_after_surcharge - senior_discount

print(f"Final Bill Amount: ₹{final_bill}")
