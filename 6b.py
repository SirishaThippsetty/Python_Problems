'''
0 to 40: 2
41 to 60: 4
61 to 120: 6
>120 : 8
Bonus:50

ex: ip : 70 op:270
ip: 4 op:58
ip:135  op: 690

'''
D = int(input("Enter the distance:"))

if D > 120:
    a = 40*2 + 20*4 + 60*6
    b = (D - 120)
    result = a + b * 8 + 50
elif D <= 120 and D > 60:
    a = 40*2 + 20*4 
    b = (D - 60)
    result = a + b*6 + 50
elif D <= 60 and D > 40:
    a = 40*2
    b = (D-40)
    result = a + b*4 + 50
elif D <= 40:
    result = D *2 + 50
print(result)