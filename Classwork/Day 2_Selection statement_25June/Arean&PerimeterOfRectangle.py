'''Write a program to calculate area and perimeter of rectangle and validate it.'''
#Enter the length of the rectangle from the user
length = float(input("Enter the length of the rectangle: "))
#validating the length
if length < 0:
    exit("Length cannot be negative. Enter valid length.")
#Enter the breadth of the rectangle from the user
breadth = float(input("Enter the breadth of the rectangle: "))
#validating the breadth
if breadth < 0:
    exit("Breadth cannot be negative. Enter valid breadth.")
#--------------------------------------------------------------
#displaying data to the user
print("Length of the rectangle is:", length)
print("Breadth of the rectangle is:", breadth)
#--------------------------------------------------------------
#calculating area of rectangle
area_of_rectangle = length * breadth
#calculating perimeter of rectangle
perimeter_of_rectangle = 2 * (length + breadth)
#displaying the result
print("The area of the rectangle is:", area_of_rectangle)
print("The perimeter of the rectangle is:", perimeter_of_rectangle)
