# Bank Loan Approval System

# Get input from user
credit_score = int(input("Enter Credit Score: "))
annual_income = float(input("Enter Annual Income: "))
existing_loan = float(input("Enter Existing Loan Amount: "))

# Define criteria
criteria_passed = 0

# Check each condition
condition1_passed = credit_score >= 750  # Credit Score ≥ 750
condition2_passed = annual_income >= 800000  # Annual Income ≥ ₹8,00,000
condition3_passed = existing_loan <= 200000  # Existing Loan Amount ≤ ₹2,00,000

# Count how many conditions are satisfied
if condition1_passed:
    criteria_passed += 1
if condition2_passed:
    criteria_passed += 1
if condition3_passed:
    criteria_passed += 1

# Determine loan status
if criteria_passed == 3:
    # All conditions satisfied
    print("Loan Status: Approved")
elif criteria_passed == 2:
    # Only one condition fails → Manual Review
    print("Loan Status: Manual Review")
    if not condition1_passed:
        print("Reason: Credit score criteria not satisfied.")
    elif not condition2_passed:
        print("Reason: Income criteria not satisfied.")
    else:
        print("Reason: Existing loan amount criteria not satisfied.")
else:
    # More than one condition fails → Rejected
    print("Loan Status: Rejected")
    reasons = []
    if not condition1_passed:
        reasons.append("Credit score criteria not satisfied")
    if not condition2_passed:
        reasons.append("Income criteria not satisfied")
    if not condition3_passed:
        reasons.append("Existing loan amount criteria not satisfied")
    print("Reasons: " + ", ".join(reasons) + ".")
