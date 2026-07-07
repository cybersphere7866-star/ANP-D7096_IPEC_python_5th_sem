#WAP to count number of uppercase character as well as lowercase character in your sentebce . without using any library
sentence = input("Enter a sentence: ")
uppercase_count = 0
lowercase_count = 0
for x in sentence:
    if x>="A"and x<="Z":
        uppercase_count += 1
    elif x>="a"and x<="z":
        lowercase_count += 1
print("Number of uppercase characters:", uppercase_count)
print("Number of lowercase characters:", lowercase_count)
