# Reverse number pattern
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1

'''
rows = int(input("Enter the number:"))
for i in range(rows,0,-1):
    number = i
    for j in range(0,i):
        print(number,end=' ')
    print(" ")
'''
This pattern is also called as a inverted pyramid of descending numbers.
'''