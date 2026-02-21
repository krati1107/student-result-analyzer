class StudentResultAnalyzer:
    def __init__(self):
        self.students = {}

    def add_student(self):
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        self.students[name] = marks
        print("Student added successfully!")

    def show_all_students(self):
        if not self.students:
            print("No student data available.")
            return

        print("\n--- Student Results ---")
        for name, marks in self.students.items():
            print(f"{name} : {marks}")

    def calculate_average(self):
        if not self.students:
            print("No data to calculate average.")
            return

        avg = sum(self.students.values()) / len(self.students)
        print(f"Average Marks: {avg:.2f}")

    def find_topper(self):
        if not self.students:
            print("No data available.")
            return

        topper = max(self.students, key=self.students.get)
        print(f"Topper: {topper} ({self.students[topper]} marks)")

    def run(self):
        while True:
            print("\n--- Student Result Analyzer ---")
            print("1. Add Student")
            print("2. Show All Students")
            print("3. Calculate Average")
            print("4. Find Topper")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.show_all_students()
            elif choice == "3":
                self.calculate_average()
            elif choice == "4":
                self.find_topper()
            elif choice == "5":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = StudentResultAnalyzer()
    app.run()