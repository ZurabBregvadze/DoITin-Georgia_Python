import csv
import os

# Class definition for Student
class Student:
    def __init__(self, name, roll_number, grade):
        # Initialize private attributes with the provided values
        self.__name = name
        self.__roll_number = roll_number
        self.grade = grade  # Use setter to ensure validation is done

    # Getter for the 'name' property
    @property
    def name(self):
        return self.__name

    # Setter for the 'name' property with validation
    @name.setter
    def name(self, value):
        if isinstance(value, str) and (cleaned_name := value.strip()) and len(value.strip()) <= 20:
            self.__name = value.strip()
        else:
            raise ValueError("Name must be a non-empty string with a maximum length of 20 characters")

    # Getter for the 'roll_number' property
    @property
    def roll_number(self):
        return self.__roll_number

    # Setter for the 'roll_number' property with validation
    @roll_number.setter
    def roll_number(self, value):
        if isinstance(value, int) and value > 0:  # Check if value is a positive integer
            self.__roll_number = value
        else:
            raise ValueError("Roll number must be a positive integer")

    # Getter for the 'grade' property
    @property
    def grade(self):
        return self.__grade

    # Setter for the 'grade' property with validation
    @grade.setter
    def grade(self, value):
        if isinstance(value, int) and 1 <= value <= 5:  # Ensure the grade is between 1 and 5
            self.__grade = value
        else:
            raise ValueError("Grade must be an integer between 1 and 5")

    # String representation of a Student object
    def __str__(self):
        return f"სახელი: {self.__name}, სიის ნომერი: {self.__roll_number}, შეფასება: {self.__grade}"

    # Method to convert a Student object to a dictionary
    def to_dict(self):
        return {"name": self.__name, "roll_number": self.__roll_number, "grade": self.__grade}


# Class definition for StudentManagementSystem
class StudentManagementSystem:
    def __init__(self, filename="students.csv"):
        # Initialize with the given filename and load existing students from it
        self.filename = filename
        self.students = []  # List to store Student objects
        self.load_students()

    def load_students(self):
        """Load students from a CSV file into the system."""
        if os.path.exists(self.filename):
            # Read from the CSV file and populate the list of students
            with open(self.filename, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Create a Student object and add it to the list
                    self.students.append(
                        Student(row["name"], int(row["roll_number"]), int(row["grade"]))
                    )
        else:
            # Create an empty CSV file with headers if it doesn't exist
            with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "roll_number", "grade"])
                writer.writeheader()

    def save_students(self):
        """Save students to the CSV file."""
        # Write all student data to the CSV file
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "roll_number", "grade"])
            writer.writeheader()
            for student in self.students:
                writer.writerow(student.to_dict())

    def roll_number_exists(self, roll_number):
        """Check if a roll number already exists in the system."""
        return any(student.roll_number == roll_number for student in self.students)

    def add_student(self):
        """Add a new student to the system."""
        print("ახალი სტუდენტის დამატება")
        try:
            # Collect the student's name
            name = input("შეიყვანეთ სტუდენტის სახელი: ").strip()

            # Validate and ensure unique roll number
            while True:
                try:
                    roll_number = int(input("შეიყვანეთ სტუდენტის სიის ნომერი: ").strip())
                    if self.roll_number_exists(roll_number):
                        print(f"შეცდომა: სიის ნომერი {roll_number} უკვე არსებობს. გთხოვთ, შეიყვანოთ სიის უნიკალური ნომერი.")
                    else:
                        break
                except ValueError:
                    print("არასწორი ინფორმაცია. სიის ნომერი უნდა იყოს ნატურალური რიცხვი.")

            # Validate grade input
            while True:
                try:
                    grade = int(input("შეიყვანეთ სტუდენტის შეფასება (1-5): ").strip())
                    if 1 <= grade <= 5:
                        break
                    else:
                        print("შეცდომა: შეფასება უნდა იყოს 1-დან 5-ის ჩათვლით.")
                except ValueError:
                    print("არასწორი ინფორმაცია. შეფასება უნდა იყოს ნატურალური რიცხვი 1-დან 5-ის ჩათვლით.")

            # Create a new student object and add it to the list
            new_student = Student(name, roll_number, grade)
            self.students.append(new_student)
            print("სტუდენტი წარმატებით დაემატა!")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def view_all_students(self):
        """Display all students in the system."""
        if not self.students:
            print("სტუდენტების სია ამჟამად ცარიელია.")
            return

        print("ყველა სტუდენტის სია:")
        for student in self.students:
            print(student)

    def search_student_by_roll_number(self):
        """Search for a student by their roll number."""
        try:
            roll_number = int(input("მოსაძებნად შეიყვანეთ სიის ნომერი: ").strip())
            for student in self.students:
                if student.roll_number == roll_number:
                    print("მოიძებნა სტუდენტი:")
                    print(student)
                    return
            print("სტუდენტი არ მოიძებნა.")
        except ValueError:
            print("არასწორი ინფორმაცია. გთხოვთ, შეიყვანოთ სიის ნომერი.")

    def update_student_grade(self):
        """Update the grade of a student."""
        try:
            roll_number = int(input("შეიყვანეთ იმ სტუდენტის სიის ნომერი, რომლის შეფასების განახლებაც გსურთ: ").strip())
            for student in self.students:
                if student.roll_number == roll_number:
                    while True:
                        try:
                            new_grade = int(input("შეიყვანეთ ახალი შეფასება 1-დან 5-ის ჩათვლით: ").strip())
                            if 1 <= new_grade <= 5:
                                student.grade = new_grade  # Use the setter for validation
                                print("შეფასება წარმატებით განახლდა!")
                                return
                            else:
                                print("შეცდომა: შეფასება უნდა იყოს 1-დან 5-ის ჩათვლით.")
                        except ValueError:
                            print("არასწორი ინფორმაცია. შეფასება უნდა იყოს ნატურალური რიცხვი 1-დან 5-ის ჩათვლით.")
            print("სტუდენტი ვერ მოიძებნა.")
        except ValueError as e:
            print(f"Error: {e}")

    def run(self):
        """Run the main menu of the Student Management System."""
        while True:
            print("\nსტუდენტების მართვის სისტემა (სმს)")
            print()
            print("1. ახალი სტუდენტის დამატება")
            print("2. ყველა სტუდენტის ნახვა")
            print("3. სტუდენტის ძებნა ნომრის მიხედვით")
            print("4. სტუდენტის შეფასების განახლება")
            print("5. გასვლა")
            print()

            choice = input("შეიყვანეთ ციფრი 1-დან 5-ის ჩათვლით: ").strip()

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.search_student_by_roll_number()
            elif choice == '4':
                self.update_student_grade()
            elif choice == '5':
                print("სტუდენტების შენახვა და სისტემიდან გამოსვლა.")
                self.save_students()
                break
            else:
                print("არასწორი ინფორმაცია. გთხოვთ, შეიყვანოთ ციფრი 1-დან 5-ის ჩათვლით.")


# Main program to run the Student Management System
if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()
