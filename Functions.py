# FUNCTIONS

# Different types of initializing a fuction 
# 1.No parameters, no return value
def Hello():
    print("Hello World")
Hello()
    
# 2.Parameters, no return value
def Detail(name,age,sal):
    print(f"Name: {name}, Age: {age}, Salary: {sal}")
    
n = input("Enter your name: ")
a = int(input("Enter your age: "))
s = int(input("Enter your salary: "))
Detail(n, a, s)

# 3.No parameters, return value
def sub():
    a=3
    b=4
    return a - b 
sub()

# 4.Parameters and return value
def add(a, b):
    return a + b 
add(2, 3) 

# Example
def func(a, b = 5, c = 10): # This function has '3' arguments 'a', 'b', 'c'
    print('a is', a, 'and b is', b, 'and c is', c)  # Print values of a, b, and c.

# Call func with arguments 3 and 7. a = 3, b = 7, c = 10
func(3, 7)

# Call func with arguments 25 and using default value for b, and explicitly setting c to 24.
func(25, c = 24)

# Call func with argument a set to 100, and explicitly setting c to 50, using default value for b.
func(c = 50, a = 100)


# *arg means initializing tuple
def myFun(*argv): # *argv will allow variable/multiple arguments
    for i in argv:
        print(i)  

myFun('Hello', 'Welcome', 'to', '360digitmg', 360)  

# **data means initialzing a dictionary
def intro(**data): # Remember dictionary - Key & Value pairs
    print("\n Data type of argument:", type(data))
    for key, value in data.items(): 
        print("{} is {}".format(key, value))    # Print each key-value pair.
# '4' items (key-value pairs)
intro(Firstname = "Bahu", Lastname = "Bali", Age = 25, Phone = 9654321123)

# Example of using both * and **
def total(*numbers, initial, **keywords):
    count = initial  # Initialize count with the initial value.
    # Iterate through the positional arguments (numbers) and add them to count.
    for number in numbers:
        count += number
    # Iterate through the keyword arguments (keywords) and add their values to count.
    for item in keywords:
        count += keywords[item] 
    # Return the total count.
    return count

# Call the total function with initial value 10, positional arguments 1, 2, 3, and keyword arguments vegetables = 50, fruits = 100.
print(total(1, 2, 3, initial=10, vegetables=50, fruits=100))
# OR
def total(initial, *numbers, **keywords):
    count = initial  # Initialize count with the initial value.
    # Iterate through the positional arguments (numbers) and add them to count.
    for number in numbers:
        count += number
    # Iterate through the keyword arguments (keywords) and add their values to count.
    for item in keywords:
        count += keywords[item] 
    # Return the total count.
    return count

# Call the total function with initial value 10, positional arguments 1, 2, 3, and keyword arguments vegetables = 50, fruits = 100.
print(total(10, 1, 2, 3, vegetables=50, fruits=100))


#Global Variable
x = 5
def new():
    global x  # Declare x as global within the function.
    x = 10    # Assign a new value to the global variable x.
    print('number is', x)
new()
print(x)# It gives the output 10 because in the fuction it is defined as global variable if it is not defined output will be 5