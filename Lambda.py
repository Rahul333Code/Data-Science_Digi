# LAMBDA Basics
from functools import reduce
import collections as cl
val = [1, 2, 3, 4, 5, 6]

# map() applies a function to every item in an iterable
# Example 1: Double each value
doubled = list(map(lambda x: x * 2, val))
print("Doubled:", doubled)  # [2, 4, 6, 8, 10, 12]

# Example 2: Using map with x % 2 to show odd/even (1 for odd, 0 for even)
mapped_mod = list(map(lambda x: x % 2, val))
print("Mapped x % 2:", mapped_mod)  # [1, 0, 1, 0, 1, 0]


# filter() keeps only the values that return True for the condition
# Example: Keep only odd numbers
filtered_odd = list(filter(lambda x: x % 2, val))
print("Filtered odd:", filtered_odd)  # [1, 3, 5]

# Example: Keep values greater than 50 from 1 to 99
filtered_gt_50 = list(filter(lambda x: x > 50, range(1, 100)))
print("Filtered > 50:", filtered_gt_50)


# reduce() combines all items using a function (like a running total or product)
# Example 1: Product of all elements
product = reduce(lambda x, y: x * y, val)  # (((1*2)*3)*4)*5*6
print("Product:", product)  # Output: 720

# Example 2: Sum of all numbers from 1 to 99
sum_1_to_99 = reduce(lambda x, y: x + y, range(1, 100))
print("Sum 1-99:", sum_1_to_99)  # Output: 4950


# Loop vs Comprehension vs Map (lambda function)
# Original list
list1 = [1, 2, 3, 4, 5]

# Using a loop to calculate squares
squares1 = [] # create an empty list called squares1

for i in list1:
    squares1.append(i ** 2) 
squares1

# Using list comprehension to calculate squares
squares2 = [i ** 2 for i in list1]
squares2

# Using map and lambda function to calculate squares
squares3 = list(map(lambda x: x ** 2, list1))
squares3

# Printing the results
squares1, squares2, squares3