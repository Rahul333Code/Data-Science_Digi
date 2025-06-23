# LIST
# Initializing a list 
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
print("After Append:", aList) # Output: [123, 'xyz', 'zara', 'abc', 2009]

# Pop: remove the last element from the existing list
print("Popped Element:", aList.pop())  # Output: 2009
print("List after Pop:", aList)  # Output: [123, 'xyz', 'zara', 'abc']

# Pop the element using index number
print("Popped Element at Index 2:", aList.pop(2))  # Output: 'zara'
print("List after Index Pop:", aList)  # Output: [123, 'xyz', 'abc']

# Insert: insert a value at a specific index
aList = [123, 'xyz', 'tommy', 'abc', 123]
aList.insert(3, 2009)
print("After Insert:", aList)  # Output: [123, 'xyz', 'tommy', 2009, 'abc', 123]


# TUPLE
# Initializing a tuple
tup = (10,)  # For a single-element tuple, a trailing comma is required; (10) is just 10, but (10,) is a tuple.

tup1 = (30, 'True', 10+50j, 3.14, 'Hi')
print(tup1)

# Accessing values
print(tup1[3])
print(tup1[1:3])

# index, count
tup2 = (1, 2, 3, 4, 5, 2, 2)
print(tup2.index(2))  # Output: 1 (index of the first occurrence of 2)
print(tup2.count(2))  # Output: 3 (count of occurrences of 2)

#SET
# Initializing a set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1)  # Output: {1, 2, 3, 4, 5}

# Set operations
# 1. Intersection
Iset = set1.intersection(set2)
Iset = set1 & set2 #Both ways we can do   
print("Intersection:", Iset)  

# 2.Union
Uset = set1.union(set2)
Uset = set1 | set2 #Both ways we can do   
print("Union:", Uset) 

# 3. Difference
Dset = set1.difference(set2)
Dset = set1 - set2 #Both ways we can do 
print("Difference: ", Dset)

# 4. Disjoit: If two set have anything in common output gives FALSE
print(set1.isdisjoint(set2))

# 5. Clear: It will remove the logical part of data
set1.clear()
print("Cleared set: ",set1)

# 6. Delete: It will completly erase the variable
del(set1)

# 7. Frozen Set: It is set but it is immutalble whereas set is mutable
set1 = frozenset(set2)
print("Frozen Set:", set1)

# 8. Add: It will add the new element to the set
set2.add(9)
print("Set after adding 9:", set2)

alist = [2, 3.14, 50+10j, 'List']
aset = {3, 10.4, 'Set'}
tup = (6, 5.43, False)
print(alist[2])
print(tup[0])

# Converting between types
# List to Set, Tuple
set1= set(alist)
print(set1)
tup1= tuple(alist)
print(tup1)
# Set to List, Tuple
list1= list(aset)
print(list1)
tup2= tuple(aset)
print(tup2)
# Tuple to List, Set
list2= list(tup)
print(list2)
set2= set(tup)
print(set2)


# DICTIONARY
# Initializing a dictionary
dict1 = {'Name': 'Aditya', 'Age': 40, 'bike': 'Honda'}
print(dict1)

# Access value using key
print(dict1['Name'])
print(dict1['Age'])

# Updating dictionary
dict1 = {'Name': 'Divit', 'Age': 8, 'bike': 'Bicycle'}
print("Updated Dictionary:", dict1)

# Update existing entry
dict1['Age'] = 9
print("Updated Age:", dict1['Age'])  # Output: 9

# Add new entry
dict1['School'] = "DPS School"
dict1['Salary'] = 50000
print("Dictionary after adding new entries:", dict1)

# Retrieve keys, values, and items of the dictionary
print("Keys:", dict1.keys())
print("Values:", dict1.values())
print("Items:", dict1.items())