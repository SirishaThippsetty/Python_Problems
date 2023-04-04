# Alternate numbers pattern using while loop

'''
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
'''
rows = int(input("Enter the number:"))
# Odd Numbers
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i*2 - 1),end=' ')
        j += 1
    i += 1
    print()
# Even numbers
a = 1
while a <= rows:
    b = 1
    while b <= a:
        print(2*a,end = ' ')
        b += 1
    a += 1
    print()