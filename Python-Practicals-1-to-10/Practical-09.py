import os

def read_and_display_file(filename):
    # Check if the file is in current directory or script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename) if not os.path.isabs(filename) and os.path.exists(os.path.join(script_dir, filename)) else filename

    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(f"\n--- Contents of '{filename}' ---")
            print(content)
            print("--- End of File ---")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    print("=== Practical 09: File Handling ===")
    filename = input("Enter the file name to read (press Enter for 'sample.txt'): ").strip()
    if not filename:
        filename = "sample.txt"

    read_and_display_file(filename)

if __name__ == "__main__":
    main()
