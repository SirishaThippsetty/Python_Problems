'''
Given the string, the task is to capitalize the first and 
last character of each word in a string. 

Examples:

Input: hello world 
Output: HellO WorlD

Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS

'''
string = input("Enter the string:").split()
new = []
for each in string:
    a = len(each)
    first_char = each[0].upper()
    last_char = each[-1].upper()
    rem_char = each[1:a-1]
    final = first_char + rem_char + last_char
    new.append(final)
print(" ".join(new))

