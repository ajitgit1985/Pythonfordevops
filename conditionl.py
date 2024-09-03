"""
Python if...elif...else Statement
The if...elif...else statement is used in Python for decision making.
"""


day_of_week = input("enter the day of week: "). lower()

print (day_of_week)




if day_of_week == "monday" or day_of_week == "sunday":

    print ("i learn python")
else:
    print("i will be practics")   


num_1 = int(input("enter first number: "))    
num_2 = int(input("enter second number: "))
choice = input("Enter the choice + / - / * / / %: ")

if choice == "+":
    sum = num_1 + num_2
    print("Sum of two numbers is",sum)
elif choice == "-":
    diff = num_1 - num_2
    print("Difference of two numbers is",diff)
elif choice == "*":
    product = num_1 * num_2
    print("Product of two numbers is",product)
elif choice == "/":
    quotient = num_1 / num_2
    print("Quotient of two numbers is",quotient)
elif choice == "%":
    remainder = num_1 % num_2
    print("Remainder of two numbers is",remainder)
else:
    print("Invalid choice")
