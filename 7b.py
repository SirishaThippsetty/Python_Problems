'''
Group 1 --> 1 7 13 19 25
Group 2 --> 2 8 14 20 26
Group 3 --> 3 9 15 21 27
Group 4 --> 4 10 16 22 28
Group 5 --> 5 11 17 23 29
Group 6 --> 6 12 18 24 30

Number is always between 1 to 30

'''

N = int(input("Enter the number:"))
remainder = N % 6
if remainder == 1:
    print("Group 1")
elif remainder == 2:
    print("Group 2")
elif remainder == 3:
    print("Group 3")
elif remainder == 4:
    print("Group 4")
elif remainder == 5:
    print("Group 5")
elif remainder == 0:
    print("Group 6")


