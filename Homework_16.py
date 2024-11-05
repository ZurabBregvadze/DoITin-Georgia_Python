########################################
#Homework_16 Task_1
########################################
def positive_check(func):
    def wrapper(number):
        if number < 0:
            raise ValueError("The number must be positive.")
        result = func(number)
        print(f"Result: {result}")
        return result
    return wrapper

@positive_check
def return_number(number):
    return number

# Example usage
try:
    return_number(5)   # Should print: Result: 5
    return_number(-3)  # Should raise ValueError
except ValueError as e:
    print(e)

############################################


############################################
#Homework_16 Task_2
############################################
class PositiveCheck:
    def __init__(self, func):
        self.func = func

    def __call__(self, number):
        if number < 0:
            raise ValueError("The number must be positive.")
        result = self.func(number)
        print(f"Result: {result}")
        return result

@PositiveCheck
def return_number(number):
    return number

# Example usage
try:
    return_number(5)   # Should print: Result: 5
    return_number(-3)  # Should raise ValueError
except ValueError as e:
    print(e)


############################################


############################################
#Homework_16 Task_3
############################################
import time

def time_calculator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Capture the start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Capture the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to complete.")
        return result
    return wrapper

@time_calculator
def example_function(n):
    # Example function that takes some time to run
    total = 0
    for i in range(n):
        total += i
    return total

# Example usage
example_function(1000000)  # Should print the time taken to execute this function

############################################


############################################
#Homework_16 Task_4
############################################
class LoggingMeta(type):
    def __new__(cls, name, bases, dct):
        # Get all method names (ignoring special methods like __init__, __str__, etc.)
        methods = [key for key, value in dct.items() if callable(value) and not key.startswith('__')]

        # Print the class name and its methods
        print(f"Creating class: {name}")
        print(f"Methods: {methods}")

        # Create the class
        return super().__new__(cls, name, bases, dct)


# Example class using LoggingMeta as its metaclass
class ExampleClass(metaclass=LoggingMeta):
    def method_one(self):
        pass

    def method_two(self):
        pass


# This will trigger the metaclass logging
example = ExampleClass()

############################################
