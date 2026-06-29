while True:
    password = input("Enter Password: ")

    if len(password) >= 8:
        print("Password Accepted")
        break
    else:
        print("Password too short.")