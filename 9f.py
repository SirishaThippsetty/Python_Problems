'''
N and prints the sum of squares of N numbers starting from 1

N = 4
1 2 3 4 => 1+4+9+16 = 30

'''
N = int(input())
total = 0
for i in range(1,N+1):
    total += i ** 2
print(total)