# WAP using function to calculate simple interest

def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si


# Main program
principal = float(input("Enter principal (in Rs): "))
rate = float(input("Enter rate (in %): "))
time = int(input("Enter time (in years): "))

simple_interest = calculate_simple_interest(principal, rate, time)
print("Simple Interest (in Rs):", simple_interest)
