# LIST
list1 = ['ssss', 5, 5.5, 40+55j, True]
print(list1)  # Output: ['ssss', 5, 5.5, (40+55j), True]

# Access values in the variable using index numbers
print(list1[0])  # Output: 'ssss'
print(list1[3])  # Output: (40+55j)
print(list1[1:4])  # Output: [5, 5.5, (40+55j)]
list1[2] = 55 + 40j # replace the 2nd index value with this new value
print("Updated List:", list1)

# Append: add new elements to the existing list
aList = [123, 'xyz', 'zara', 'abc']
aList.append(2009) # adds new element / item to the end of the list
print("After Append:", aList) # Output: [123, 'xyz', (55+40j), 'abc', 2009]

# Pop: remove the last element from the existing list
print("Popped Element:", aList.pop())  # Output: 2009
print("List after Pop:", aList)  # Output: [123, 'xyz', (55+40j), 'abc']

# Pop the element using index number
print("Popped Element at Index 2:", aList.pop(2))  # Output: (55+40j)
print("List after Index Pop:", aList)  # Output: [123, 'xyz', 'abc']

# Insert: insert a value at a specific index
aList = [123, 'xyz', 'tommy', 'abc', 123]
aList.insert(3, 2009)
print("After Insert:", aList)  # Output: [123, 'xyz', 'tommy', 2009, 'abc', 123]