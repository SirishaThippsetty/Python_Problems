# Inverted Pyramid pattern with the same digit

'''
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
'''
rows = int(input("Enter the number:"))
b = 0
for i in range(rows,0,-1):
    b += 1
    for j in range(1,i+1):
        print(rows,end=" ")
    print()


