# Airline Ticket Pricing Engine

# Base fare
base_fare = 5000

# Get input from user
age = int(input("Enter Passenger Age: "))
business_class = input("Business Class (Y/N): ").upper()
window_seat = input("Window Seat (Y/N): ").upper()
weekend_travel = input("Weekend Travel (Y/N): ").upper()

# Calculate additional charges
additional_charges = 0

if business_class == 'Y':
    additional_charges += 3000

if window_seat == 'Y':
    additional_charges += 500

if weekend_travel == 'Y':
    additional_charges += 1000

# Calculate total fare before discount
total_before_discount = base_fare + additional_charges

# Determine discount based on age
discount_percentage = 0

if age < 12:
    discount_percentage = 50
elif age > 60:
    discount_percentage = 20

# Calculate discount amount
discount_amount = total_before_discount * (discount_percentage / 100)

# Calculate final fare
final_fare = total_before_discount - discount_amount

# Display output
print(f"Base Fare: ₹{base_fare}")
print(f"Additional Charges: ₹{additional_charges}")

if discount_percentage > 0:
    if age < 12:
        print(f"Child Discount: {discount_percentage}%")
    else:
        print(f"Senior Citizen Discount: {discount_percentage}%")

print(f"Final Ticket Fare: ₹{final_fare}")
