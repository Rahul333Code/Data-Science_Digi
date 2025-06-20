#String Slicing
n = "Microsoft Google Facebook"
print(n[:8])
print(n[10:-9])
print(n[-8:25])

#String Formatting
print("Price of %s is $%.2f" %('Pen', 4.588))

#Occurence of a Character in a String
a = "Nakshatra is a very good girl"
b = 'a'
count = a.count((b))
print(f"Occurence of  '{b}' in '{a}' is: {count}")

# isalnum() returns True when value present in string has no special character
x = 'Hi my name is Rahul'
print(x.isalnum())
x = 'HimynameisRahul'
print(x.isalnum())

# isdigit returns True when value present in string is whole numbers without any special characters
x = "123456" 
print(x.isdigit())  
x = "123 456"
print(x.isdigit())

# isalpha returns True when value present in string has no digit or any special character
x = "thisis"
print(x.isalpha())
x = "this is string example" # space is treated as a special character, not alphabet
print(x.isalpha())
x = "this is string 10" 
print(x.isalpha())

# String manipulation
Name = "YASHvi"
print(Name)  # Output: YASHvi
print(Name.capitalize())  # Output: Yashvi
print(Name.upper())  # Output: YASHVI
print(Name.lower())  # Output: yashvi
print(Name.swapcase())  # Output: yashVI
