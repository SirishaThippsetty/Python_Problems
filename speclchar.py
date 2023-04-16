'''
Program to check if a string contains any special character

Given a string, the task is to check if that string contains any special 
character (defined special character set). If any special character found, 
don’t accept that string.

Examples : 

Input : Geeks$For$Geeks
Output : String is not accepted.

Input : Geeks For Geeks
Output : String is accepted.

'''
ip_str = input("Enter the input string:")
special_char = '[!@#$%^&*(_-+=)][{"?/\|'
total = 0
for i in range(len(ip_str)):
    if ip_str[i] in special_char:
        total += 1
if total > 0:
    print("String is not accepted")
else:
    print("String is accepted")