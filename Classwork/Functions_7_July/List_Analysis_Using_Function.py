# Function to find the maximum number
def find_max(numbers):
    return max(numbers)


# Function to find the minimum number
def find_min(numbers):
    return min(numbers)


# Function to find the average
def find_average(numbers):
    return sum(numbers) / len(numbers)


# Main Program

numbers = []

# Take 10 numbers from the user
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Call the functions
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

# Display the results
print("Maximum =", maximum)
print("Minimum =", minimum)
print("Average =", average)