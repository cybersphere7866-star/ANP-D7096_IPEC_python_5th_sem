# ==========================================
# operations.py
# Main program
# Imports twodfigures module
# ==========================================
import twodfigure 

while True:

    print("\n========== Geometry Calculator ==========")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        side = float(input("Enter side: "))

        print("1. Area")
        print("2. Perimeter")

        op = int(input("Enter operation: "))

        if op == 1:
            print("Area =", twodfigure.square_area(side))

        elif op == 2:
            print("Perimeter =", twodfigure.square_perimeter(side))

        else:
            print("Invalid Choice")

    elif choice == 2:

        radius = float(input("Enter radius: "))

        print("1. Area")
        print("2. Circumference")

        op = int(input("Enter operation: "))

        if op == 1:
            print("Area =", round(twodfigure.circle_area(radius),2))

        elif op == 2:
            print("Circumference =", round(twodfigure.circle_perimeter(radius),2))

        else:
            print("Invalid Choice")

    elif choice == 3:

        print("1. Area")
        print("2. Perimeter")

        op = int(input("Enter operation: "))

        if op == 1:

            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            print("Area =", twodfigure.triangle_area(base,height))

        elif op == 2:

            s1 = float(input("Enter side 1: "))
            s2 = float(input("Enter side 2: "))
            s3 = float(input("Enter side 3: "))

            print("Perimeter =", twodfigure.triangle_perimeter(s1,s2,s3))

        else:
            print("Invalid Choice")

    elif choice == 4:

        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        print("1. Area")
        print("2. Perimeter")

        op = int(input("Enter operation: "))

        if op == 1:
            print("Area =", twodfigure.rectangle_area(length,breadth))

        elif op == 2:
            print("Perimeter =", twodfigure.rectangle_perimeter(length,breadth))

        else:
            print("Invalid Choice")

    elif choice == 5:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")