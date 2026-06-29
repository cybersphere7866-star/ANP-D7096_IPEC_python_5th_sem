# Multi-Level Access Control System

# Get input from user
role = input("Role: ").lower()
account_status = input("Account Status: ").lower()

# Check if account is inactive first
if account_status != "active":
    access_level = "NO ACCESS"
else:
    # Determine access level based on role
    if role == "admin":
        security_clearance = int(input("Security Clearance: "))
        
        if security_clearance >= 5:
            access_level = "FULL ACCESS"
        else:
            access_level = "LIMITED ACCESS"
    
    elif role == "manager":
        experience = int(input("Experience (Years): "))
        
        if experience > 5:
            access_level = "DEPARTMENT ACCESS"
        else:
            access_level = "LIMITED ACCESS"
    
    elif role == "employee":
        experience = int(input("Experience (Years): "))
        
        if experience > 2:
            access_level = "LIMITED ACCESS"
        else:
            access_level = "READ-ONLY ACCESS"
    
    elif role == "guest":
        access_level = "READ-ONLY ACCESS"
    
    else:
        access_level = "NO ACCESS"

# Display output
print(f"Access Level: {access_level}")
