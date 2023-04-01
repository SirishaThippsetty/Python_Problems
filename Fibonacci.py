'''
A series in which the next term is the sum of the preceding
two terms is called a fibonacci series. 
Fibonacci series is asked frequently in interviews.
0 1 1 2 3 5 8 13 ---- etc
'''
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
n = int(input("Enter the  number of elements:"))
print(a,b,end=" ")
while n-2:
    c = a+b
    a = b
    b = c
    print(c,end=" ")
    n = n-1