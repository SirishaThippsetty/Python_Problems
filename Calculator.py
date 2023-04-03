# Simple calculator using Python Using Functions


print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")
print("5.Simple Interest")
print("6.Compound Interest")
print("7.Square of the number")
print("8.Square root of the number")
number = int(input("Enter the input number:"))

if number == 1:
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    addition = a + b
    print("Addition of two numbers is:",addition)
elif number == 2:
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    subraction = a - b
    print("Addition of two numbers is:",subraction)
elif number == 3:
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    multiply = a * b
    print("Multiplication of two numbers :",multiply)
elif number == 4:
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    division = a / b
    print("Division of two numbers:",division)
elif number == 5:
    principal = int(input("Enter the principal:"))
    rate = int(input("Enter the rate: "))
    time = int(input("Enter the time:"))
    simple_interest = (principal*rate*time)/100
    print("Simple Interest:",simple_interest)
elif number == 6:
    principal = int(input("Enter the principal:"))
    rate = int(input("Enter the rate: "))
    time = int(input("Enter the time:"))
    compound_interest = principal * pow((1+rate/100),time)
    print("Compound Interest:",compound_interest)
elif number == 7:
    digit = int(input("Enter the number:"))
    square_numb = digit ** 2
    print("Square of the number:",square_numb)
elif number == 8:
    digit = int(input("Enter the number:"))
    square_root = digit ** 0.5
    print("Square root of the given number:",square_root)
else:
    print("Wrong input!Enter the correct number")
