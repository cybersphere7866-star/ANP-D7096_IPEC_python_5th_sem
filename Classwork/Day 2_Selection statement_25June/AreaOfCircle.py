'''Write a program to calculate area of circle and validate it'''
#Enter the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))
#validating the radius
if radius < 0:
    exit("Radius cannot be negative. Enter valid radius.")
#--------------------------------------------------------------
#displaying data to the user
print("Radius of the circle is:", radius)
#--------------------------------------------------------------
#calculating area of circle
area_of_circle = 3.14 * radius * radius
#displaying the result
print("The area of the circle is:", area_of_circle)
'''Output:
Enter the radius of the circle: 5
Radius of the circle is: 5.0
The area of the circle is: 78.5
'''

