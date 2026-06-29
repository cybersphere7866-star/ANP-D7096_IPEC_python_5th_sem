# Online Examination Result Analyzer

# Get marks for 5 subjects
hindi = float(input("Hindi : "))
english = float(input("English : "))
mathematics = float(input("Mathematics : "))
science = float(input("Science : "))
computer = float(input("Computer : "))

# Store all marks in a list
marks = [hindi, english, mathematics, science, computer]

# Calculate average
average = sum(marks) / len(marks)

print(f"Average Marks: {average}")

# Check if student passed or failed
# Fail if any subject score < 40
if any(mark < 40 for mark in marks):
    result = "FAIL"
    classification = ""
else:
    result = "PASS"
    
    # Determine classification based on average
    if average >= 75:
        classification = "Distinction"
    elif average >= 60:
        classification = "First Division"
    elif average >= 50:
        classification = "Second Division"
    else:
        classification = "Pass"

print(f"Result: {result}")

if result == "PASS":
    print(f"Classification: {classification}")
