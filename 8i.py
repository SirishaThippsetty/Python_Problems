'''
Sum of N numbers from M
M N
M = 7 N = 3
7+8+9 = 24

'''
M = int(input("Enter the number M:"))
N = int(input("Enter the number N:"))
total = 0
for i in range(M,M+N):
    total += i
print(total)
