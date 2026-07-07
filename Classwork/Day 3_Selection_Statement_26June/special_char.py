#WAP to count number of special character in a given sentence
semtence = input("Enter a sentence: ")
count = 0
for x in semtence:
    if not x.isalnum() and not x.isspace():
        count += 1
print("Number of special characters:", count)