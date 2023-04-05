# Check the number is prime number or not

number = int(input("Enter the input number:"))
fact = 0
if number > 0:
    for i in range(2,number): 
        if number % i == 0:
            fact += 1
if fact == 0:
    print("Given number",number,"is Prime number")
else:
    print("Given number",number,"is not Prime number")