'''Write a program to caculate velocity and validate it.'''
#Enter the distance from the user
distance = float(input("Enter the distance covered in meters: "))
#validating the distance
if distance < 0:
    exit("Distance cannot be negative. Enter valid distance.")
#Enter the time from the user
time = float(input("Enter the time taken in seconds: "))
#validating the time
if time <= 0:
    exit("Time cannot be zero or negative. Enter valid time.")
# Calculate velocity
velocity = distance / time
print(f"The velocity is {velocity} m/s.")
