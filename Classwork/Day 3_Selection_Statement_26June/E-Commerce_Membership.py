# E-Commerce Premium Membership Qualification System

# Get input from user
total_purchases = float(input("Total Purchases: "))
orders_completed = int(input("Orders Completed: "))
customer_rating = float(input("Customer Rating: "))

# Initialize membership status and reason
is_premium = False
reason = ""

# Check special case: Purchases above ₹1,00,000 automatically qualify
if total_purchases > 100000:
    is_premium = True
    reason = "Purchase amount exceeded ₹100000."
else:
    # Check standard criteria: All three conditions must be met
    if total_purchases > 50000 and orders_completed >= 20 and customer_rating >= 4.5:
        is_premium = True
        reason = "All eligibility criteria satisfied."
    else:
        is_premium = False
        # Provide reason for ineligibility
        reasons = []
        if total_purchases <= 50000:
            reasons.append("Purchase amount is below ₹50000")
        if orders_completed < 20:
            reasons.append("Orders completed is less than 20")
        if customer_rating < 4.5:
            reasons.append("Customer rating is below 4.5")
        reason = ", ".join(reasons) + "."

# Display output
if is_premium:
    print("Premium Membership Status: Eligible")
else:
    print("Premium Membership Status: Not Eligible")

print(f"Reason: {reason}")
