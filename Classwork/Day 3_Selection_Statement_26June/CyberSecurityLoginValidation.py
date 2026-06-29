# Cyber Security Login Validation System

# Correct credentials
correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"

# Get username
username = input("Username: ")

# Check if username is correct
if username != correct_username:
    print("User Not Found")
else:
    # Username is correct, now check password with 3 attempts
    password_attempts = 0
    password_correct = False
    
    while password_attempts < 3:
        password = input("Password: ")
        password_attempts += 1
        
        if password == correct_password:
            password_correct = True
            break
        elif password_attempts < 3:
            print(f"Incorrect Password. {3 - password_attempts} attempts remaining.")
    
    if not password_correct:
        print("Account Locked")
    else:
        # Password is correct, now check OTP
        otp = input("OTP: ")
        
        while otp != correct_otp:
            print("Incorrect OTP. Re-enter OTP")
            otp = input("OTP: ")
        
        # All credentials are correct
        print("Login Successful")
        print(f"Welcome {username.capitalize()}")