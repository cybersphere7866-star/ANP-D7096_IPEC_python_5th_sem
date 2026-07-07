 #Student Marks Management Problem Statement: Create a dictionary to store the marks of 5 students, where the key is the student's name and the value is their marks. Perform the following operations: • Display all student names and marks.  • Add a new student with marks.  • Update the marks of an existing student.  • Delete a student by name.  • Display the student who scored the highest marks. 
dict_student = { "kunal" :85, "suresh": 90, "ramesh": 78, "sita": 92, "gita": 88 }
while True:
    print("1. Display all student names and marks")
    print("2. Add a new student with marks")
    print("3. Update the marks of an existing student")
    print("4. Delete a student by name")
    print("5. Display the student who scored the highest marks")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        for name, marks in dict_student.items():
            print(f"{name}: {marks}")
    
    elif choice == 2:
        name = input("Enter the student's name: ")
        marks = int(input("Enter the student's marks: "))
        dict_student[name] = marks
        print(f"Added {name} with marks {marks}.")
    
    elif choice == 3:
        name = input("Enter the student's name to update: ")
        if name in dict_student:
            marks = int(input("Enter the new marks: "))
            dict_student[name] = marks
            print(f"Updated {name}'s marks to {marks}.")
        else:
            print(f"{name} not found.")
    
    elif choice == 4:
        name = input("Enter the student's name to delete: ")
        if name in dict_student:
            del dict_student[name]
            print(f"Deleted {name}.")
        else:
            print(f"{name} not found.")
    
    elif choice == 5:
        highest_student = max(dict_student, key=dict_student.get)
        highest_marks = dict_student[highest_student]
        print(f"The student with the highest marks is {highest_student} with {highest_marks} marks.")
    
    elif choice == 6:
        display = False
        print("Exiting...")
    
    else:
        print("Invalid choice. Please try again.")