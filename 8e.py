'''
Average of N numbers

'''

N = int(input("Enter the number:"))
total = 0
for i in range(1,N+1):
    total += i
average = total/N
print(average)