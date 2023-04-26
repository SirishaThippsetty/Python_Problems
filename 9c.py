'''
Write a program that reads N inputs and print the average of N inputs
N = 5
next 5 ==> 3 6 2 8 1
average = (3+6+2+8+1)/N

'''
N = int(input())
total = 0
for i in range(N):
    a = int(input())
    total += a
average = total/N
print(average)