# Hospital Emergency Triage System

# Get input from user
critical_condition = input("Critical Condition (Y/N): ").upper()
age = int(input("Age: "))
oxygen_level = float(input("Oxygen Level: "))

# Initialize priority and reason
priority = ""
reason = ""

# Determine priority based on conditions (checked in order of severity)
if critical_condition == 'Y':
    priority = "Immediate Treatment"
    reason = "Critical Condition"
elif oxygen_level < 90:
    priority = "High Priority"
    reason = "Low Oxygen Level"
elif age > 65:
    priority = "Medium Priority"
    reason = "Senior Citizen"
else:
    priority = "Normal Priority"
    reason = "Routine Check-up"

# Display output
print(f"Patient Priority: {priority}")
print(f"Reason: {reason}")
