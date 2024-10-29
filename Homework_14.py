########################################
#Homework_14 Task_1
########################################
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        """Initialize the account with account number, account holder, and an optional balance (default is 0)."""
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account and update the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}\n")


# Create multiple BankAccount objects
account1 = BankAccount("123456", "Alice", 1000)
account2 = BankAccount("654321", "Bob", 500)

# Perform multiple transactions
account1.deposit(300)
account1.withdraw(150)
account1.display_balance()

account2.deposit(200)
account2.withdraw(1000)  # Attempt to withdraw more than balance
account2.display_balance()

########################################


########################################
#Homework_14 Task_2
########################################
class Student:
    def __init__(self, name, student_id):
        """Initialize the student with name, student_id, and an empty list of courses."""
        self.name = name
        self.student_id = student_id
        self.courses = []

    def register_course(self, course):
        """Register a course for the student."""
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} has been registered for the course: {course}")
        else:
            print(f"{self.name} is already registered in {course}.")

    def display_info(self):
        """Display the student's name, ID, and list of enrolled courses."""
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:", ", ".join(self.courses) if self.courses else "No courses registered.")
        print()  # Print a blank line for readability

# Create multiple Student objects
student1 = Student("Alice", "S1234")
student2 = Student("Bob", "S5678")

# Register students for different courses
student1.register_course("Mathematics")
student1.register_course("Physics")
student2.register_course("Chemistry")
student2.register_course("Biology")
student2.register_course("Mathematics")

# Display information for each student
student1.display_info()
student2.display_info()

########################################
