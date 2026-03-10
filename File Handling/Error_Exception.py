"""
1. Compile time error >> Syntax Error and Indentation
2. Exception >> Errors during execution
"""

# HOW TO HANDLE THE exception? >> try-except block

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

try:
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be divided by zero")
except ValueError:
    print("Incorrect data type")


