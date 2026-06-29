# Employee Performance Evaluation System

# Get input from user
project_score = float(input("Project Score: "))
attendance = float(input("Attendance: "))
client_feedback = float(input("Client Feedback: "))

# Determine performance rating based on scores
if project_score > 90 and attendance > 90 and client_feedback > 90:
    rating = "Excellent"
    reason = ""
elif project_score > 75 and attendance > 75 and client_feedback > 75:
    rating = "Good"
    reason = ""
elif project_score > 60 and attendance > 60 and client_feedback > 60:
    rating = "Average"
    reason = ""
else:
    rating = "Poor"
    reason = "Scores below minimum criteria."

# Apply additional rule: Attendance below 70% cannot receive more than Average rating
if attendance < 70:
    if rating == "Excellent" or rating == "Good":
        rating = "Average"
        reason = "Attendance below 70%"
    elif rating == "Average":
        reason = "Attendance below 70%"

# Display output
print(f"Performance Rating: {rating}")
if reason:
    print(f"Reason: {reason}")
