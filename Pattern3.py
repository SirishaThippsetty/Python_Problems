# Inverted pyramid pattern of numbers

rows = int(input("Enter the number:"))
b = 0
for i in range(rows,0,-1):
    b += 1
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# Another inverted half pyramid pattern with number
for i in range(rows,0,-1):
    b += 1
    for j in range(1,i+1):
        print(i,end=" ")
    print()

'''
Enter the number:5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
'''