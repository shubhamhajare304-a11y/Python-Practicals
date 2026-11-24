import math

def calculate_area(shape, dimension1, dimension2=0):
    shape = shape.strip().lower()
    if shape == "circle":
        # dimension1 represents radius
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        # dimension1 represents length, dimension2 represents width
        return dimension1 * dimension2
    elif shape == "triangle":
        # dimension1 represents base, dimension2 represents height
        return 0.5 * dimension1 * dimension2
    else:
        return None

def get_positive_number(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            print("Dimension must be greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

def main():
    print("=== Practical 08: Area Calculator Using Polymorphism ===")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Select a shape (1-3): ").strip()

    if choice == "1":
        radius = get_positive_number("Enter radius of the circle: ")
        area = calculate_area("circle", radius)
        print(f"Area of Circle: {area:.2f}")

    elif choice == "2":
        length = get_positive_number("Enter length of the rectangle: ")
        width = get_positive_number("Enter width of the rectangle: ")
        area = calculate_area("rectangle", length, width)
        print(f"Area of Rectangle: {area:.2f}")

    elif choice == "3":
        base = get_positive_number("Enter base of the triangle: ")
        height = get_positive_number("Enter height of the triangle: ")
        area = calculate_area("triangle", base, height)
        print(f"Area of Triangle: {area:.2f}")

    else:
        print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
