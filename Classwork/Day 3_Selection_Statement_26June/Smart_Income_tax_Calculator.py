# Government Tax Portal - Tax Calculator with Rebates

# Get input from user
income = float(input("Enter Annual Income: "))
age = int(input("Enter Age: "))
gender = input("Enter Gender (M/F): ").upper()

# Calculate tax based on income slabs
if income <= 500000:
    tax_rate = 0
elif income <= 1000000:
    tax_rate = 0.10
elif income <= 2000000:
    tax_rate = 0.20
else:
    tax_rate = 0.30

# Calculate base tax
base_tax = income * tax_rate

print(f"Tax before rebate: ₹{base_tax}")

# Apply rebates
senior_citizen_rebate = 0
women_rebate = 0

# Senior citizen rebate (Age >= 60): 5% rebate on tax
if age >= 60:
    senior_citizen_rebate = base_tax * 0.05
    print(f"Senior Citizen Rebate: ₹{senior_citizen_rebate}")

# Women taxpayer rebate: Additional 2% rebate on tax
if gender == 'F':
    women_rebate = base_tax * 0.02
    print(f"Women Rebate: ₹{women_rebate}")

# Calculate final tax payable
final_tax = base_tax - senior_citizen_rebate - women_rebate

print(f"Final Tax Payable: ₹{final_tax}")
