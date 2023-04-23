'''
Group A --> 1 3 5 7 9
Group B --> 2 4 6 8 10

Number is always between 1 to 10

'''
N = int(input("Enter the number:"))
if N % 2 == 0:
    print("Group B")
else:
    print("Group A")