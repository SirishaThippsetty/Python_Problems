'''
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
5 5 5 5

M = 5 N = 4

'''
M = int(input())
N = int(input())
for i in range(1,M+1):
    for k in range(1,N+1):
        print(i,end=' ')
    print()