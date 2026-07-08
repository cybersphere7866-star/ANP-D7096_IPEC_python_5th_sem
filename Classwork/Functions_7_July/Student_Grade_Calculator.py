# Function to calculate the grade based on marks
def calculate_grade(marks):

    # Check the marks and return the grade
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


# Main Program

# Repeat 5 times for 5 students
for i in range(1, 6):

    # Take marks as input
    marks = int(input(f"Enter marks of Student {i}: "))

    # Call the function
    grade = calculate_grade(marks)

    # Display the result
    print("Marks =", marks)
    print("Grade =", grade)
    print()