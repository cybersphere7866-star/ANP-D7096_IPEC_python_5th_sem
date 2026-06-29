
correct_pin = 4589

while True:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
