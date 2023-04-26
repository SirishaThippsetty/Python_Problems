'''
Product of N numbers after X

X=4 N = 2
2 numbers after X are 5,6
product = 5*6=30

'''
X = int(input())
N = int(input())
product = 1
for i in range(X+1,X+N+1):
    product *= i
print(product)