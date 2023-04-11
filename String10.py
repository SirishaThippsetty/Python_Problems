'''
Given a String, perform uppercase of later part of string. 

Input : test_str = ‘geeksforgeek’ 
Output : geeksfORGEEK 
Explanation : Latter half of string is uppercased. 

Input : test_str = ‘apples’ 
Output : appLES 
Explanation : Latter half of string is uppercased.

'''
given_string = input("Enter the string:")
len_string = int(len(given_string)/2)
new_string = given_string[:len_string] + given_string[len_string:].upper()
print(new_string)