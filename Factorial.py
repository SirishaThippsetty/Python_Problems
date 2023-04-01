# Find the factorial of a number

input_numb = int(input("Enter the number:"))
factorial_numb = 1
for i in range(1,input_numb+1):
    factorial_numb *= i
print("The factorial of",input_numb,"is",factorial_numb)
