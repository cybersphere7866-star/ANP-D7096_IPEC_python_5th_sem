# Write a program to input a full name and display only the first name without using a library method.

name = input("Enter your full name: ")

first_name = ""
for ch in name:
    if ch == ' ':
        break
    first_name += ch

print("First name:", first_name)

