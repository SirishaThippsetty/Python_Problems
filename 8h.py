'''
N numbers after M

N M inputs
Print N numbers after M

ex:3
  5

  4
  5
  6
  7
  8
'''

N = int(input("Enter the number N:"))
M = int(input("Enter the number M:"))
for i in range(N+1,N+M+1):
    print(i)