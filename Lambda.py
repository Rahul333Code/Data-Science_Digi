# LAMBDA 
d = {'a' : 1, 'b' : 2}
#print{d['c']}
# it will show error because 'c' is not there in dictionary
# To overcome this we have to do:
import collections as cl
# Sets default value 'key Not found' to absent keys
defd = cl.defaultdict(lambda : 'key is Not Available')
defd['a'] = 1 # initializing values
defd['b'] = 2
print("The value of 'a' is : ", defd['a']) 
print("The value of 'c' is : ", defd['c'])


# In-built functions';/
from functools import reduce
val = [1, 2, 3, 4, 5, 6]

# map() applies a function to every item in an iterable
# Example 1: Double each value
doubled = listmap((lambda x: x * 2, val))
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
product = reduce(lambda x, y: x * y, val)  
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

# Using list comprehension to calculate squares
squares2 = [i ** 2 for i in list1]

# Using map and lambda function to calculate squares
squares3 = list(map(lambda x: x ** 2, list1))

# Printing the results
print("Squares of list using loop: ",squares1 )
print("Squares of list using Comprehension: ",squares2 )
print("Squares of list using Lambda: ",squares3 )


# ITERATORS
names = ["Shakaal", "Gabbar", "Pathan", "Prem"]
print(names)
# Convert the list into an iterator
new_list = names.__iter__()
# Or
new_list = iter(names)
print(new_list)

names = [i for i in range(1000000)]

# Convert the list into an iterator.
new_list = iter(names)

# Import the sys module to access system-related information.
import sys
# See the differnce in amount of space used that's the reason why we use iterators to reduce storage space
# Print the size of the 'names' variable in bytes.
print(f'size of variable names is {sys.getsizeof(names)} bytes')
# Print the size of the 'new_list' variable in bytes.
print(f'size of variable new_list is {sys.getsizeof(new_list)} bytes')

name = 'Machine'
name_itr = iter(name)
while True: #Always go to the loop as it is always true
    try: # First it tries the statements in try throughout the iteration if anything gives error it goes to catch
        item = next(name_itr)
        print(item)
    except stopItertion:
        break


# GENERATORS
# Define a generator function 'squence' that yields numbers from 0 to N-1
def squence(N):  
    for i in range(N):
        yield i  # Yield each number
blist = squence(1000000)
print(blist)
print(next(blist))

# A generator function to generate Fibonacci numbers up to a specified limit 'limit'.
def fib(limit):   
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1  # Initialize variables 'a' and 'b' to store the first two Fibonacci numbers.
    # One by one yield next Fibonacci Number 
    while a < limit:  # Continue generating Fibonacci numbers until 'a' exceeds the specified limit.
        yield a  # Yield the current Fibonacci number.
        a, b = b, a + b  # Update 'a' and 'b' to calculate the next Fibonacci number.
        # Updates a=b and b=a+b
# Create a generator object by calling the fib() function with argument 5
x = fib(5) 
print(x)  # Print the generator object

# Iterating over the generator object using next() until StopIteration is raised
while True:
    try:
        print(next(x), end = "\n")  # Print the next Fibonacci number
    except StopIteration:  # Catch StopIteration exception
        break  # Break out of the loop


