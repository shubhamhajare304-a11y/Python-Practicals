def check_password_strength(password):
    has_min_length = len(password) >= 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if has_min_length and has_uppercase and has_lowercase and has_digit:
        return "Strong"
    else:
        return "Weak"

def main():
    print("=== Practical 06: Password Strength Checker ===")
    print("A Strong password requires:")
    print("  - At least 8 characters")
    print("  - At least one uppercase letter")
    print("  - At least one lowercase letter")
    print("  - At least one digit")
    print("(Type 'stop' to end)\n")

    while True:
        password = input("Enter a password to check: ")
        if password.strip().lower() == "stop":
            print("Program terminated.")
            break

        strength = check_password_strength(password)
        print(f"Password Strength: {strength}\n")

if __name__ == "__main__":
    main()
