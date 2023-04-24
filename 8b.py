'''
0-50km:3
51-100:5
101-200:6
>200:each km=10
Bonus:100

'''
D = int(input("Enter the distance in km:"))
bonus = 100
if D > 200:
    a = (D-200)
    b = 50*3 + 50*5 + 100*6
    result = b + a*10 + bonus
elif D <= 200 and D > 100:
    a = (D - 100)
    b = 50*3 + 50*5 + a*6
    result = b + bonus
elif D <= 100 and D > 50:
    a = (D-50)
    b = a*5 + 50*3
    result = b + bonus
elif D <= 50:
    result = D*3+bonus
print(result)