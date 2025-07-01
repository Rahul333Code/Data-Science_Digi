# NUMPY
import numpy as np
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 5, 7, 9]
print(list1[1:4])
list3 = list1 + list2
print(list3)

a = [1, 2, 3, 4, 5]
print(type(a))
b = [6, 7 , 8, 9 ,10]
x = np.array(a)# Creates a numpy array 'y' from the list 'x'.
y = np.array(b)
print(type(x))
print(y * 2)
print(x * y)

print(y > 7) # Checks which elements of 'y' are greater than 10.
print(y[y > 7]) # Retrieves the elements of 'y' that are greater than 10.

from numpy import random
x = random.randint(3, 100) # Generates a random integer between 3 and 100 and assigns it to 'x'.
print(x)


# Memory savers
import numpy as np
l = list(range(10)) 
print(l)
a = np.arange(10) # Create a numpy array 'a' containing numbers from 0 to 9
print(a)

b = a[::2]  #Create a new array 'b' by slicing 'a' with a step of 2
print(b)

print(np.shares_memory(a,b)) # Check whether 'a' and 'b' share the same memory
common = np.intersect1d(a, b) # Gets values that are common in 'a' and 'b'
print(common)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])  # Create a 2D numpy array 'arr'
print(arr)
lis = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(lis[0][1])
print(arr[0, 1])  # Print the element at row 0, column 1 of 'arr'
print(arr[0, 2])  # Print the element at row 0, column 2 of 'arr'
print(arr[1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])  # Create a 1D numpy array 'arr'
print(arr[1:4])  # Slice elements from the beginning to index 4 (not included) of 'arr'
print(arr[1::2])  # Slice elements from the beginning to index 1 to index 5 of 'arr' with a step of 2

a = np.arange(10)
mask = (a % 2 == 0)
print(mask) # Prints boolean values which are true and false in an array
print(a[mask]) # To get values we have to do like this


# Numpy matrices 
# Define a 2x2 matrix 'a' using string notation
a = np.matrix('1 2; 6 9; 4 6 ') # Defining a matrix
print(a)
print(a.shape) # To get the dimension of an array
print(a)
#or
b = np.matrix([1, 2, 3])
print(b.shape)
print(b)

a = np.arange(0, 40, 10)
b = np.array([0, 1, 2])
print(b)
a = a[:, np.newaxis]  # Adds one extra axis
print(a+b)


# Data Structures
## Arrays/Vectors
from array import * # * means everything
array1 = array('i', [10, 20, 30, 40, 50])
print(array1)
# Iterate through elements of 'array1' and print each element
for x in array1:
    print(x)

print(array1.remove(30))
array1[2] = 90
for x in array1:
    print(x)


## 2D Arrays
import numpy as np
from numpy import *
# Define a 2D array 'T'
T = [[11, 12, 5, 2], [15, 6, 10, 20], [10, 8, 12, 5]]
arr = np.array(T)
print(arr)
print(arr[2,3])
#Or
print(arr[2][3])
m = reshape(arr, (4, 3)) # changer 3*4 matrix to 4*3 
print(m)
m = array([['Mon', 18, 20, 22, 17],
           ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19],
           ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22],
           ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])
# Append a new row to 'm' using the 'append' function
m_r = append(m, [['Avg', 12, 15, 13, 11]], 0) # Add a row at the end
print(m_r)  # Print the resulting matrix after appending
# Insert a new column to 'm' using the 'insert' function
m_c = insert(m, [3], [1, 2, 3, 4 ,5 ,6, 7], 1) # Add a column at index 5
print(m_c)
# Delete a row at index 2 from 'm' using the 'delete' function
n1 = delete(m, [2], 0) # if we keep zero row will be delected
print(n1)  
# Delete a column at index 2 from 'm' using the 'delete' function
n2 = delete(m, [2], 1) #Other than zero column will be delected 
print(n2)

#Example
ex = array([[1, 2, 3], [4, 5, 6]])
print(ex)
a = append(ex, [[2,3,4]],0)
b = append(ex, [[2],[3]], 1)
print(a)
print(b)
ex_c = insert(ex, 1, [1,2,4],0)
print(ex_c)
ex_d = insert(ex, 2, [3,4], 1)
print(ex_d)
d_r = delete(ex, 1,0)
print(d_r)
d_c = delete(ex, 1,1)
print(d_c)

# Create a diagonal matrix 'z' using numpy
z = np.diag(1 + array([1,4,8,3,0]))
print(z) 

# Create a numpy array 'z' containing zeros of size 10
z = np.zeros(10)
print(z)
z[4] = 1  # Set the value at index 4 to 1
print(z)

# Create a random vector 'z' of size 30 and find its mean value
z = np.random.random(30) #random.random gives the random values from 0 to 1
print(z)
m = z.mean()  # Calculate the mean value of 'z'
print(m)

# Reverse a vector (first element becomes last)
z = np.arange(50)  # Create a numpy array containing numbers from 0 to 49
print(z)  # Print 'z'
z = z[::-1]  # Reverse the order of elements in 'z'
print(z)  # Print the reversed 'z'
#Or
x = np.flip(z)
print(x)
