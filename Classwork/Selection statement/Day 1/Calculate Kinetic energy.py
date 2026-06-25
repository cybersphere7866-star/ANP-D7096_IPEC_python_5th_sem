'''Write a program to calculate kinetic energy and validate it.'''
#Enter the mass from the user
mass = float(input("Enter the mass of the object in kilograms: "))
#validating the mass
if mass < 0:
    exit("Mass cannot be negative. Enter valid mass.")
#Enter the velocity from the user
velocity = float(input("Enter the velocity of the object in meters per second: "))
#validating the velocity
if velocity < 0:
    exit("Velocity cannot be negative. Enter valid velocity.")
# Calculate kinetic energy
kinetic_energy = 0.5 * mass * velocity ** 2
#displaying the result
print(f"The kinetic energy of the object is {kinetic_energy} Joules.")
