N = int(input())
S = str(N)
l = len(S)
total = 0
for each in S:
    a = int(each)
    b = a ** l
    total += b
print(total)
