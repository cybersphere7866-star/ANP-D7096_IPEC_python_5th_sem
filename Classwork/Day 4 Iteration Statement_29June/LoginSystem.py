username = "admin"
password = "python123"

for i in range(3):
    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
else:
    print("Account Locked")