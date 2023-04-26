'''
Right hand triangle of N rows using *

'''
# N = int(input())
# for i in range(1,N+1):
#     print("*"*i)

'''
Right hand triangle of N rows using numbers

'''
N = int(input())
for i in range(1,N+1):
    for k in range(1,i+1):
        print(i,end=" ")
    print()