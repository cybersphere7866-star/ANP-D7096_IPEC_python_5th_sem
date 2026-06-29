# University Scholarship Award System

# Get input from user
percentage = float(input("Percentage: "))
family_income = float(input("Family Income: "))
disciplinary_action = input("Disciplinary Action (Y/N): ").upper()

# Initialize scholarship
scholarship = "No Scholarship"

# Check conditions
if family_income >= 800000:
    scholarship = "No Scholarship"
elif disciplinary_action == 'Y':
    scholarship = "No Scholarship"
else:
    # Determine scholarship based on percentage
    if percentage >= 95:
        scholarship = "100%"
    elif percentage >= 90:
        scholarship = "75%"
    elif percentage >= 85:
        scholarship = "50%"
    elif percentage >= 80:
        scholarship = "25%"
    else:
        scholarship = "No Scholarship"

# Display output
print(f"Scholarship Awarded: {scholarship}")
