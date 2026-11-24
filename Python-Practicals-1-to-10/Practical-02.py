EARTH_GRAVITY = 9.8
MOON_GRAVITY = 1.62

def calculate_weight(mass, gravity):
    return mass * gravity

def display_concepts():
    print("\n" + "=" * 55)
    print("PROGRAMMING CONCEPTS EXPLANATION")
    print("=" * 55)
    print("1. Identifier of a constant used in the code:")
    print("   EARTH_GRAVITY and MOON_GRAVITY")
    print("\n2. Name of a user-defined function:")
    print("   calculate_weight (also display_concepts and main)")
    print("\n3. Data type of the variable 'layout':")
    print("   The original 'Q01 challenge 1 gravity' file is not provided/available.")
    print("   As instructed, its data type is not guessed without the original file.")
    print("\n4. Name of a parameter used in the code:")
    print("   'mass' and 'gravity' (in calculate_weight)")
    print("\n5. Arithmetic operator used in the code:")
    print("   '*' (multiplication operator used in: mass * gravity)")
    print("=" * 55)

def main():
    print("=== Practical 02: Weight Calculator for Earth and Moon ===")
    try:
        mass = float(input("Enter the mass of the object in kilograms: "))
        if mass < 0:
            print("Error: Mass cannot be negative.")
            return

        weight_earth = calculate_weight(mass, EARTH_GRAVITY)
        weight_moon = calculate_weight(mass, MOON_GRAVITY)

        print(f"\nObject Mass: {mass:.2f} kg")
        print(f"Weight on Earth (g = {EARTH_GRAVITY} m/s²): {weight_earth:.2f} N")
        print(f"Weight on Moon  (g = {MOON_GRAVITY} m/s²): {weight_moon:.2f} N")

        display_concepts()

    except ValueError:
        print("Invalid input! Please enter a numerical value for mass.")

if __name__ == "__main__":
    main()
