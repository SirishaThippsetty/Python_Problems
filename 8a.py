'''
Mon,Tue == Week Start 1,2
Wed,Thu,Fri == Midweek 3,4,5
Sat,Sun == Weekend 6,7

'''
N = int(input("Enter the number between 1 and 7:"))
if N == 1 or N == 2:
    print("Week Start")
elif N == 3 or N == 4 or N == 5:
    print("Midweek")
elif N == 6 or N == 7:
    print("Weekend")