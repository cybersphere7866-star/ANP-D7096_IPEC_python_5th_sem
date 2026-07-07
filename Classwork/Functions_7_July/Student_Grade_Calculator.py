# Write a Python program that defines a function to calculate a grade.

def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A+"
    elif 75 <= marks <= 89:
        return "A"
    elif 60 <= marks <= 74:
        return "B"
    elif 40 <= marks <= 59:
        return "C"
    elif 0 <= marks < 40:
        return "Fail"
    else:
        return "Invalid marks"


# Main program
print("Enter marks for 5 students:")
for i in range(1, 6):
    marks = float(input(f"Enter marks of student {i}: "))
    grade = calculate_grade(marks)
    print(f"Student {i}: Marks = {marks}, Grade = {grade}")
