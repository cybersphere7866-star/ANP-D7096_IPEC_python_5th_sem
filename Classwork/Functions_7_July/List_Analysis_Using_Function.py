# Write a Python program to analyze a list of 10 integers using functions.

# Function to find the maximum value in a list
def find_max(numbers):
    maximum = numbers[0]  # Assume the first element is the largest initially
    for num in numbers:   # Check each number in the list
        if num > maximum: # If a larger number is found, update maximum
            maximum = num
    return maximum

# Function to find the minimum value in a list
def find_min(numbers):
    minimum = numbers[0]  # Assume the first element is the smallest initially
    for num in numbers:   # Check each number in the list
        if num < minimum: # If a smaller number is found, update minimum
            minimum = num
    return minimum

# Function to find the average of all values in a list
def find_average(numbers):
    total = 0  # Start with zero total
    for num in numbers:   # Add each number to the total
        total += num
    average = total / len(numbers)  # Divide total by the number of elements
    return average


# Main program
numbers = []  # Create an empty list to store the integers

print("Enter 10 integers:")
for i in range(10):  # Ask the user to enter 10 values
    value = int(input(f"Enter number {i + 1}: "))
    numbers.append(value)  # Add each entered value to the list

# Call all functions and store the returned results
maximum_value = find_max(numbers)
minimum_value = find_min(numbers)
average_value = find_average(numbers)

# Display the results
print("Maximum value:", maximum_value)
print("Minimum value:", minimum_value)
print("Average value:", average_value)
