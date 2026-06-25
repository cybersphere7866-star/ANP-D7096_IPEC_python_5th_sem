'''Write a program to calculate the area of a square'''
#Enter the side of the square from the user
side = float(input("Enter the side of the square: "))

#validating the side
if side < 0:
    exit("Side cannot be negative. Enter valid side.")
#calculating area of square 
area_of_square = side * side
#displaying the result
print("The area of the square is:", area_of_square)
