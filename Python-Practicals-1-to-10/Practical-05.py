def get_positive_integer(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Please enter an integer greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")

def get_valid_score(prompt):
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= 100:
                return val
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric score.")

def main():
    print("=== Practical 05: Student Average Calculator ===")
    num_students = get_positive_integer("Enter the number of students: ")

    student_averages = []

    for i in range(1, num_students + 1):
        print(f"\nEntering 5 scores for Student {i}:")
        total = 0.0
        for j in range(1, 6):
            score = get_valid_score(f"  Test {j} score (0-100): ")
            total += score

        avg = total / 5
        student_averages.append(avg)
        print(f"Student {i} Average Score: {avg:.2f}")

    class_avg = sum(student_averages) / len(student_averages)

    print("\n" + "=" * 35)
    print("CLASS PERFORMANCE SUMMARY")
    print("=" * 35)
    for i, avg in enumerate(student_averages, start=1):
        print(f"Student {i} Average: {avg:.2f}")
    print("-" * 35)
    print(f"Overall Class Average: {class_avg:.2f}")
    print("=" * 35)

if __name__ == "__main__":
    main()
