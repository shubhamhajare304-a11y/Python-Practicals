import matplotlib.pyplot as plt

def create_line_plot(ax):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    temperatures = [22, 24, 21, 25, 27, 26, 23]
    ax.plot(days, temperatures, marker="o", color="blue", linestyle="-")
    ax.set_title("Line Plot: Temperature Trend")
    ax.set_xlabel("Day")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True)

def create_scatter_plot(ax):
    study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    exam_scores = [45, 52, 58, 65, 70, 76, 82, 88, 94]
    ax.scatter(study_hours, exam_scores, color="green", marker="o")
    ax.set_title("Scatter Plot: Study Hours vs Score")
    ax.set_xlabel("Hours Studied")
    ax.set_ylabel("Exam Score")
    ax.grid(True)

def create_box_plot(ax):
    scores = [55, 60, 65, 70, 72, 75, 78, 80, 82, 85, 90, 95]
    ax.boxplot(scores, patch_artist=True)
    ax.set_title("Box Plot: Score Distribution")
    ax.set_ylabel("Marks")
    ax.grid(True)

def create_bar_chart(ax):
    subjects = ["Math", "Physics", "Chemistry", "Python", "English"]
    students = [45, 38, 32, 50, 28]
    ax.bar(subjects, students, color="orange")
    ax.set_title("Bar Chart: Students per Subject")
    ax.set_xlabel("Subject")
    ax.set_ylabel("Number of Students")

def create_pie_chart(ax):
    activities = ["Sleep", "College", "Study", "Exercise", "Leisure"]
    hours = [8, 6, 4, 1, 5]
    ax.pie(hours, labels=activities, autopct="%1.1f%%", startangle=90)
    ax.set_title("Pie Chart: Daily Routine")

def main():
    print("=== Practical 10: Data Visualization Using Matplotlib ===")
    print("Creating visualization dashboard with all 5 required plots:")
    print("  1. Line Plot")
    print("  2. Scatter Plot")
    print("  3. Box Plot")
    print("  4. Bar Chart")
    print("  5. Pie Chart")

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    fig.suptitle("Data Visualization - Practicals (MIT ADT University)", fontsize=16)

    create_line_plot(axes[0, 0])
    create_scatter_plot(axes[0, 1])
    create_box_plot(axes[0, 2])
    create_bar_chart(axes[1, 0])
    create_pie_chart(axes[1, 1])

    # Turn off the unused 6th subplot
    axes[1, 2].axis("off")

    plt.tight_layout()
    print("Displaying graphs. Close the window to finish.")
    plt.show()

if __name__ == "__main__":
    main()
