# Employee Information System

employees = {
    101: {"Name": "Alice", "Department": "HR", "Salary": 50000},
    102: {"Name": "Bob", "Department": "IT", "Salary": 60000},
    103: {"Name": "Charlie", "Department": "Finance", "Salary": 55000},
    104: {"Name": "Diana", "Department": "IT", "Salary": 62000},
}

while True:
    print("\nEmployee Information System")
    print("1. Display all employee details")
    print("2. Search employee by ID")
    print("3. Increase salary by 10%")
    print("4. Display employees by department")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAll Employee Details:")
        for emp_id, details in employees.items():
            print("Employee ID:", emp_id)
            print("Name:", details["Name"])
            print("Department:", details["Department"])
            print("Salary:", details["Salary"])
            print()

    elif choice == "2":
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            details = employees[emp_id]
            print("\nEmployee Found:")
            print("Name:", details["Name"])
            print("Department:", details["Department"])
            print("Salary:", details["Salary"])
        else:
            print("Employee not found.")

    elif choice == "3":
        for emp_id in employees:
            employees[emp_id]["Salary"] = employees[emp_id]["Salary"] + (employees[emp_id]["Salary"] * 10 / 100)
        print("Salaries increased by 10%.")

    elif choice == "4":
        dept = input("Enter department name: ")
        print("\nEmployees in department", dept)
        found = False
        for emp_id, details in employees.items():
            if details["Department"].lower() == dept.lower():
                print("Employee ID:", emp_id, "Name:", details["Name"])
                found = True
        if not found:
            print("No employees found in this department.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")