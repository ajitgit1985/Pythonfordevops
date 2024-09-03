"""
Python Variables
Variables are containers for storing data values.
A variable is created the moment you first assign a value to it.
"""
num1= int( input("enter first number: "))
num2= int (input ("enter second number: "))

sum_of_num = (num1 + num2)

print(type(num1))
print(type(num2))
print("sum of to number" , sum_of_num)

diff = (num1 - num2)

print ("diff of two number", diff)

product = num1 * num2
print("Product of two numbers is",product)

quotient = num1 / num2
print("Quotient of two numbers is",quotient)

remainder = num1 % num2
print("Remainder of two numbers is",remainder)