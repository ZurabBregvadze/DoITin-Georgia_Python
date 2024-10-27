######################################################
#Homework 9, Task 1
######################################################
int_list = [10, 20, 30, 40]

def added_number(number):
    global int_list
    int_list.append(number)

added_number(5)
print(int_list)
######################################################




######################################################
#Homework 9, Task 2
######################################################
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

n = 10234056789
print(sum_of_digits(n))

######################################################




######################################################
#Homework 9, Task 3
######################################################
def reverse_string(s):

    if len(s) == 0:
        return s
    else:

        return s[-1] + reverse_string(s[:-1])

input_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(reverse_string(input_string))
#####################################################




######################################################
#Homework 9, Task 4
######################################################
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_sequence(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
n = 10
print(fibonacci_sequence(n))

#####################################################
