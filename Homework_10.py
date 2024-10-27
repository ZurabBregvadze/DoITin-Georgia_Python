######################################################
#Homework 10, Task 1
######################################################
def group_lists(*lists):
    return list(zip(*lists))

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']


grouped = group_lists(list1, list2)
print(grouped)


######################################################



######################################################
#Homework 10, Task 2
######################################################
get_even_elements = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 16, 16, 17, 18, 101, 102, 1487, 2398]
even_numbers = get_even_elements(numbers)
print(even_numbers)

######################################################


######################################################
#Homework 10, Task 3
######################################################
import functools

get_positive_numbers = lambda lst: list(filter(lambda x: x > 0, lst))


numbers = [-10, -3, 0, 5, 9, -2, 7, -1, -2, 2, -100, 101, 102, 103, -500, 266, -7,]
positive_numbers = get_positive_numbers(numbers)
print(positive_numbers)

######################################################


######################################################
#Homework 10, Task 4
######################################################
get_palindromes = lambda lst: list(filter(lambda s: s == s[::-1], lst))

strings = ["racecar", "hello", "madam", "python", "level", "world", "kayak", "rotator", "universe", "peep", "WOW", "noon", "civic", "radar"]
palindromes = get_palindromes(strings)
print(palindromes)

######################################################



######################################################
#Homework 10, Task 5
######################################################
from functools import reduce

def product_of_elements(lst):
    return reduce(lambda x, y: x * y, lst)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
product = product_of_elements(numbers)
print(product)

######################################################