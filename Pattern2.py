# # Pattern Programs

rows = int(input("Enter the number:"))
for i in range(1,rows+1):
    for j in range(i):
        print(i,end=" ")
    print(" ")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
