# 'if' condition 
a = 23
if a >= 22:  # Checks if the value of 'a' is greater than or equal to 22.
   print("if")  # Prints "if" if the condition is true.


# 'if and else' conditions when you have two conditions
is_male = False # Assigns the boolean value False to the variable 'is_male'.
if is_male:  # Checks if 'is_male' evaluates to True.
    print("you are male")  # Prints "you are male" if 'is_male' is True.
else:
    print("you are female")  # Prints "you are female" if 'is_male' is False.


# 'if, elif and else conditions when you have two or more conditions
a = 23  # Assigns the value 23 to variable 'a'.
if a >= 22:  # Checks if the value of 'a' is greater than or equal to 22.
   print("if")  # Prints "if" if the condition is true.
elif a >= 21:  # Checks if the previous condition is not met and if the value of 'a' is greater than or equal to 21.
   print("elif")  # Prints "elif" if the condition is true.
else:
   print("else")  # Prints "else" if none of the above conditions are true.



# Nested if Statement: Conditional statement inside a conditional statement
score = 500  # Assigns the value 500 to the variable 'score'.
money = 6000  # Assigns the value 6000 to the variable 'money'.
age = 65  # Assigns the value 65 to the variable 'age'.

if score > 100:  # Checks if the value of 'score' is greater than 100.
    print("You got good points")  # Prints "You got good points" if the condition is true.
   
    if money >= 5000:  # Checks if the value of 'money' is greater than or equal to 5000.
        print("You win")  # Prints "You win" if the condition is true.
        
        if age >= 30:  # Checks if the value of 'age' is greater than or equal to 30.
            print("You win in middle age")  # Prints "You win in middle age" if the condition is true.
        else:
            print("You win in young age")  # Prints "You win in young age" if the condition is false.
    else:
        print("You have high points but you do not have enough money")  # Prints message if 'money' is less than 5000.
else:
    print("You are loser")  # Prints "You are loser" if the condition for 'score' is false.
