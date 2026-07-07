#WAP to ask the user to input the full name and displaay the first name from it without using the library method
full_name = input("Enter your full name: ")
first = " "
for  i in full_name:
    if i == " ":
        break
    else :
        first += i
print("First name is:", first)