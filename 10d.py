# N = int(input())
# for i in range(1,N+1):
#     spaces = (N - i) * " "
#     stars = "*" * i
#     print(spaces+stars)

N = int(input())
for i in range(1,N+1):
    spaces = "  " * (N-i)
    stars = "* " * i
    print(spaces+stars)


# rows = int(input())

# for each_number in range(1, rows + 1):
#     spaces = "  " * (rows - each_number)
#     stars = "* " * (each_number)
#     print(spaces + stars)