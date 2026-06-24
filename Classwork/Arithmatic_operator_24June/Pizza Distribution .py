'''Write a Python program to find how many slices remain after equal distribution. '''
total_slices = int(input("Enter the total number of slices: "))
slices_per_person = int(input("Enter the number of slices per person: "))
remaining_slices = total_slices % slices_per_person
#output:
print("Number of slices that remain:", remaining_slices)
