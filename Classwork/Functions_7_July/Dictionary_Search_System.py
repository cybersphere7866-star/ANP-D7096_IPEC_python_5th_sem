# Python program to search a student name using a roll number

# Function to search for a roll number in the dictionary
# If the roll number is found, return the student name
# Otherwise, return a message saying the student was not found

def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"


# Main program
# Create a dictionary with roll numbers as keys and student names as values
students = {
    101: "Aman",
    102: "Riya",
    103: "Karan",
    104: "Sita",
    105: "Neha"
}

# Ask the user to enter a roll number to search
roll_no = int(input("Enter roll number to search: "))

# Call the function and display the result
result = search_student(students, roll_no)
print(result)
