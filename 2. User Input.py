# Python for beginners
#
# 2. User Input

input("Enter your name: ")
# Outcome: Enter your name: 

# If you want to collect user input you can use the input function
# like above

# To store the data you need a variable

# Example:

name = input("Enter your name: ")
# Outcome: Enter your name: 

# What the user types in will be stored in the variable name
# and can be used in example print statements

# Example:

name = input("Enter your name: ")
# Here I enter John
print("Hello",name+"!")
# Outcome: Hello John!

# For numbers its diffrent
# You need to say if it is a int or a float

# Example:

number1 = int(input("Enter a number: "))

# Or for a float

number1 = float(input("Enter a number: "))

# You dont need to do this for a string

# Practice Project
# Simple calculator:

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
outcome = number1 + number2
print(outcome)

# This is a simple calculator using the things we learned

# If you want to print a number within a print function you might
# run into some problems
# If you want to fix that issue you need to make the int a string

# Example:

number1 = int(input("Enter a number: "))
str(number1)
print("Outcome: "+number1)

# Try it your self!
#
# ---
#
# Make a program that asks for a users name and age and prints it
