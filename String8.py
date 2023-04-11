'''
Given a string in Python. The task is to check whether the 
string has at least one letter(character) and one number. Return “True” 
if the given string fully fill the above condition else return “False” (without quotes)

Input: welcome2ourcountry34
Output: True

Input: stringwithoutnum
Output: False

'''
string = input("Enter the string:")
alpha = 0
numeric = 0
for each in string:
    if each.isalpha():
        alpha += 1
    elif each.isnumeric:
        numeric += 1
if alpha >= 1 and numeric >= 1:
    print("True")
else:
    print("False")
