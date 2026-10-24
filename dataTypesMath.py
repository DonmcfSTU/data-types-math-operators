# Donavan McFadden - Student ID: Donmcf8357
# PA 1.9: Data Types and Basic Math Operators
# This program asks for the user's name, Student ID, and two different
# whole numbers. It does three math calculations, shows the results with
# two decimal places, and says whether the first number is larger or
# smaller than the second number.

print("Donmcf8357")

# Get the user's name and Student ID (string data)
name = input("Please enter your name: ")
studentID = input("Please enter your Student ID: ")

# Get two whole numbers and convert them to integers
number1 = int(input("Please enter a whole number: "))
number2 = int(input("Please enter a second, different whole number: "))

# Make sure the two numbers are different and the second is not zero,
# because we cannot divide by zero
while number2 == number1 or number2 == 0:
    if number2 == number1:
        print("The two numbers must be different. Please try again.")
    else:
        print("The second number cannot be 0 because we divide by it. Please try again.")
    number2 = int(input("Please enter a second, different whole number: "))

# Three math calculations (the division result is a float)
product = number1 * number2
quotient = number1 / number2
difference = number1 - number2

# Output the results with two decimal places
print()
print(f'{number1} multiplied by {number2} is: {product:,.2f}')
print(f'{number1} divided by {number2} is: {quotient:,.2f}')
print(f'{number1} minus {number2} is: {difference:,.2f}')

# Decide if the first number is larger or smaller than the second
if number1 > number2:
    print(f'{number1} is larger than {number2}.')
else:
    print(f'{number1} is smaller than {number2}.')

# Output the user's name and Student ID
print()
print(f'Name: {name}')
print(f'Student ID: {studentID}')
