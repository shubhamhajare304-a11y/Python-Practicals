def main():
    print("=== Practical 03: Assignment List Management ===")
    
    assignments = ["Math Homework", "Physics Lab Report", "Python Practical"]
    
    print("\nInitial Assignment List:")
    for index, task in enumerate(assignments, start=1):
        print(f"{index}. {task}")

    new_assignment = input("\nEnter a new assignment to add: ").strip()
    if new_assignment:
        assignments.append(new_assignment)
        print(f"Added: '{new_assignment}'")
    else:
        print("No assignment entered.")

    print("\nUpdated Assignment List:")
    for index, task in enumerate(assignments, start=1):
        print(f"{index}. {task}")

    completed_assignment = input("\nEnter the completed assignment to remove: ").strip()
    if completed_assignment in assignments:
        assignments.remove(completed_assignment)
        print(f"Removed: '{completed_assignment}'")
    else:
        print(f"'{completed_assignment}' was not found in the list.")

    print("\nFinal Assignment List:")
    if assignments:
        for index, task in enumerate(assignments, start=1):
            print(f"{index}. {task}")
    else:
        print("No remaining assignments.")

if __name__ == "__main__":
    main()
