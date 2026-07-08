# Student Subject Report Card using nested dictionaries

students = {
    'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
    'Priya': {'Math': 78, 'Science': 95, 'English': 82},
    'Ankit': {'Math': 91, 'Science': 89, 'English': 94}
}

# Calculate total and average for each student
student_results = {}
for student, subjects in students.items():
    total = sum(subjects.values())
    average = total / len(subjects)
    student_results[student] = {'Total': total, 'Average': average}

print("Student Report Card")
print("------------------")
for student, result in student_results.items():
    print(student, "-> Total:", result['Total'], "Average:", round(result['Average'], 2))

# Topper based on total marks
max_total = -1
topper = ""
for student, result in student_results.items():
    if result['Total'] > max_total:
        max_total = result['Total']
        topper = student
print("\nTopper:", topper, "with total marks", max_total)

# Subject-wise highest marks
subjects = ['Math', 'Science', 'English']
print("\nSubject-wise highest marks:")
for subject in subjects:
    highest_marks = -1
    highest_student = ""
    for student, details in students.items():
        if details[subject] > highest_marks:
            highest_marks = details[subject]
            highest_student = student
    print(subject, "->", highest_marks, "by", highest_student)

# Students with average >= 85
print("\nStudents with average >= 85:")
for student, result in student_results.items():
    if result['Average'] >= 85:
        print(student, "->", round(result['Average'], 2))

#print the report card in a tabular format
print("\nReport Card:")
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Student', 'Math', 'Science', 'English', 'Total', 'Average'))
print("-" * 60)
for student, subjects in students.items():                                      
    total = student_results[student]['Total']
    average = student_results[student]['Average']
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(student, subjects['Math'], subjects['Science'], subjects['English'], total, round(average, 2)))    
    