'''
0 to 20: 2
21 to 60: 4
>60: 6
Bonus:30

ex: ip : 125 op:620
ip: 15 op:60
ip: 50 op: 190

'''
D = int(input("Enter the distance:"))

if D > 60:
    a = 20*2 + 40 * 4
    b = (D - 60)
    result = a + b * 6 + 30
elif D <= 60 and D > 20:
    a = 20*2
    b = (D - 20)
    result = a + b*4 + 30
elif D <= 20:
    result = D * 2 + 30
print(result)