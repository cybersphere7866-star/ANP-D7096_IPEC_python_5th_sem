# Function to check password strength
def check_password(password):

    # Variables to check conditions
    upper = False
    lower = False
    digit = False

    # Check every character
    for ch in password:

        if ch.isupper():
            upper = True

        elif ch.islower():
            lower = True

        elif ch.isdigit():
            digit = True

    # Check all conditions
    if len(password) >= 8 and upper and lower and digit:
        return "Strong Password"
    else:
        return "Weak Password"


# Main Program

password = input("Enter your password: ")

result = check_password(password)

print(result)