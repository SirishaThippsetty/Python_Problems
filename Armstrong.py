'''
ex: 1634 ==> 1 ** 4 + 6 ** 4 + 3 ** 4 + 4 ** 4 == 1634 then armstrong number
663 ==> 6 ** 3 + 6 ** 3 + 3 ** 3 != 663 then not armstrong number

'''
num = input("Enter the number:")
temp = int(num)
length_num = len(num)
total = 0
for each in num:
    a = int(each)
    total += a ** length_num
if total == temp:
    print("Given number is Armstrong Number")
else:
    print("Given number is not Armstrong Number")
