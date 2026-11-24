def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

def basic_calculator():
    print("\n--- Basic Calculator ---")
    num1 = get_number("Enter the first number: ")
    operator = input("Enter operator (+, -, *, /): ").strip()
    num2 = get_number("Enter the second number: ")

    if operator == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operator! Please enter one of +, -, *, /.")

def advanced_calculator():
    print("\n--- Advanced Calculator ---")
    print("1. Exponentiation (Power)")
    print("2. Modulus (Remainder)")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        base = get_number("Enter base: ")
        power = get_number("Enter exponent: ")
        result = base ** power
        print(f"Result: {base} ^ {power} = {result}")
    elif choice == "2":
        dividend = get_number("Enter dividend: ")
        divisor = get_number("Enter divisor: ")
        if divisor == 0:
            print("Error: Modulus by zero is not allowed.")
        else:
            result = dividend % divisor
            print(f"Result: {dividend} % {divisor} = {result}")
    else:
        print("Invalid choice! Please select 1 or 2.")

def main():
    print("=== Practical 01: Basic and Advanced Calculator ===")
    basic_calculator()

    choice = input("\nDo you want to perform advanced calculations? (yes/no): ").strip().lower()
    if choice in ["yes", "y"]:
        advanced_calculator()

    print("\nCalculation completed successfully.")

if __name__ == "__main__":
    main()
