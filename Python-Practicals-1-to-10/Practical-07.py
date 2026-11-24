def calculate_calories(carbs, fats, proteins):
    calories_from_carbs = carbs * 4
    calories_from_fats = fats * 9
    calories_from_proteins = proteins * 4
    return calories_from_carbs + calories_from_fats + calories_from_proteins

def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val >= 0:
                return val
            print("Value cannot be negative.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    print("=== Practical 07: Daily Calorie Calculator ===")
    print("Nutritional conversion standards:")
    print("  - Carbohydrates: 4 cal/g")
    print("  - Fats:          9 cal/g")
    print("  - Proteins:      4 cal/g\n")

    carbs = get_positive_float("Enter carbohydrates intake in grams: ")
    fats = get_positive_float("Enter fats intake in grams: ")
    proteins = get_positive_float("Enter proteins intake in grams: ")

    total_calories = calculate_calories(carbs, fats, proteins)

    print("\n--- Daily Calorie Summary ---")
    print(f"Calories from Carbs:    {carbs * 4:.1f} cal")
    print(f"Calories from Fats:     {fats * 9:.1f} cal")
    print(f"Calories from Proteins: {proteins * 4:.1f} cal")
    print(f"Total Daily Calories:   {total_calories:.1f} cal")

if __name__ == "__main__":
    main()
