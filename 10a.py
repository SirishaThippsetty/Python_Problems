X = int(input())
N = int(input())
count = 0
for i in range(1,N+1):
    a = 2*i - 1
    term = X **a
    count += term
print(count)
