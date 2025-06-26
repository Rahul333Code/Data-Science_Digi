# Built-in Functions
# Zip and Unzip 
name = ["Shakaal", "Gabbar", "Pathan", "Prem"] 
roll_no = [4, 1, 3, 2] 
marks = [40, 50, 60, 70] 

mapped = zip(name, roll_no, marks) 
print(mapped)
  
mapped = set(mapped)  
print("The zipped result is : ", mapped) 

namez, roll_noz, marksz = zip(*mapped) 
print("The unzipped result: \n") 
print("The name list is : ", end = "") 
print(namez) 
print("The roll_no list is : ", end = "") 
print(roll_noz)   
print("The marks list is : ", end = "") 
print(marksz) 


# Sort
animals = ['dog', 'cat', 'cow', 'sheep', 'goat', 'elephant']
sorted(animals) # Ascending order with alphabet (lexicographical)
sorted(animals, reverse = True) # Descending order with alphabet by including parameter "reverse = True"

# Descending order with respect to length of the character
sorted(animals, key = len, reverse = True)

# Ascending order with respect to length of the character 
sorted(animals, key = len) 

# Object 'animals' in memory is not updated
sorted(animals) # on console output you see items sorted based on alphabets (lexicographical technique)

# Built-in function for sort
animals.sort() # it will update memory as well alongside sorting


# Mutability: list vs tuple
# Lists are mutable: applying *= modifies the same object (ID does not change)
l = [1, 2, 3]
print("Before *= on list:", id(l), l)
l *= 2  # Extends the same list in-place
print("After *= on list:", id(l), l)  # Same ID, list is now [1, 2, 3, 1, 2, 3]

# Tuples are immutable: applying *= creates a new object (ID changes)
t = (1, 2, 3)
print("Before *= on tuple:", id(t), t)
t *= 2  # Creates a new tuple (1, 2, 3, 1, 2, 3)
print("After *= on tuple:", id(t), t)  # New ID