N = int(input())
for i in range(N,0,-1):
    spaces = "  " * (i-1)
    stars = "+ " *(N-i) + "# "
    print(spaces+stars)
for k in range(1,N):
    stars = "+ " *(N-k-1) + "# "
    spaces = "  " * (k)
    print(spaces+stars)
