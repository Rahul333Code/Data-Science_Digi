# LOOPS
#LOOPS

# For loops
snacks = ['Pizza', 'Burger', 'Shawarma', 'Franky']
print("Snacks available: ")
for i in snacks: # Iterates over each element in the list 'snacks'.
    print(i)
   
    
print("Even number unil 20 are: ")
for i in range(0, 21, 2):  # Iterates over values from 0 to 6 with a step size of 2.
    print(i)
else:  
    print("The for loop is over")  # Prints a message indicating the loop is over.
    
    
# List Comprehension
numbers = [2, 3, 5]
getsum = [i + 2 for i in numbers]  # Generates a new list by adding 2 to each element of 'numbers'.
print(getsum)  # Prints the modified list 'getsum'.

getnum = [i + 2 for i in numbers if i < 5]  # Generates a new list by adding 2 to elements of 'numbers' less than 5.
print(getnum)  # Prints the modified list 'getnum'.


# Example: Factorial of a number
n = int(input("Enter a number to find factorial: "))
fact = 1
if n < 0:
    print("For negetive value there will be no factorial")
elif n == 0:
    print("Factorial of '0' is : 1")
else:
    for i in range(1,n+1):
        fact = fact * i
    print(f"Factorial of '{n}' is : {fact}")
    
    
# Control Statements
# Continue
names = ["Rishu", 'Aayush', 'Ram', 'Shubh']  
for i in names:  # Iterates through each name in the list.
  if len(i) == 3:  # Checks if the length of the name is 3 characters.
    continue  # Moves to the next iteration of the loop 
  print(f'My name is {i}')  # Prints the name if its length is not 3.

# Pass
names = ["Rishu", 'Aayush', 'Ram', 'Shubh']  
for i in names:  # Iterates through each name in the list.
  if len(i) == 3:  # Checks if the length of the name is 3 characters.
    pass  # move to the next time of code within the loop and print results
  print(f'My name is {i}')  # Prints the name if its length is not 3.

# Break
names = ["Rishu", 'Aayush', 'Ram', 'Shubh']
for i in names:  # Iterates through each name in the list.
  if len(i) == 3:  # Checks if the length of the name is 3 characters.
    break  # Exits the loop if the length is 3.
  print(f'My name is {i}')  # Prints the name if its length is not 3.