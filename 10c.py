X = int(input())
N = int(input())
count = 0
for i in range(1,N+1):
    a = 2*i
    term = X **a
    if i % 2 == 0:
        count -= term
    else:
        count += term   
print(count)
