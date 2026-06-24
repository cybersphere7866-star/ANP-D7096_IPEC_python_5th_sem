'''Write a Python program to calculate how much each participant should pay '''
total_event_cost = float(input("Enter the total event cost: "))
number_of_participants = int(input("Enter the number of participants: "))
amount_per_participant = total_event_cost / number_of_participants
#output:
print("Each participant should pay:", amount_per_participant)
