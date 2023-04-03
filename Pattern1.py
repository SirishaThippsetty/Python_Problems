# Demonstrate Star pattern
number = int(input("Enter the number:"))
for i in range(1,number+1):
    for j in range(1,i+1):
        print("* ",end=" ")
    print()

# Demonstrate number in star pattern
for i in range(1,number+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()