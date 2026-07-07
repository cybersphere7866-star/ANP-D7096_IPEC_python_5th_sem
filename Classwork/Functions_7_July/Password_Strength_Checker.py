# Simple password strength checker

def check_password(password):
    # Count the length of the password
    length = len(password)

    # Check for uppercase, lowercase, and digit
    upper = False
    lower = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True
        if ch.islower():
            lower = True
        if ch.isdigit():
            digit = True

    # Check all conditions
    if length >= 8 and upper and lower and digit:
        return "Strong Password"
    else:
        return "Weak Password"


# Main program
password = input("Enter your password: ")
result = check_password(password)
print(result)
