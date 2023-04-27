X = int(input())
N = int(input())
count = 0
for i in range(1,N+1):
    a = 2*i
    term = X **a
    count += term
print(count)
