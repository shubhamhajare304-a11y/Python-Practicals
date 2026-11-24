def main():
    print("=== Practical 04: Secret Message Decoder ===")
    secret_message = input("Enter the secret message (substring): ").strip()
    coded_message = input("Enter the coded message (full text): ").strip()

    if not secret_message or not coded_message:
        print("Error: Neither secret message nor coded message can be empty.")
        return

    if secret_message in coded_message:
        position = coded_message.find(secret_message)
        print("\nResult: Match Found!")
        print(f"The secret message '{secret_message}' exists inside the coded message at index {position}.")
    else:
        print("\nResult: No Match Found.")
        print(f"The secret message '{secret_message}' does not exist inside the coded message.")

if __name__ == "__main__":
    main()
