'''
Given a string, the task is to check if every vowel is present or not. 
We consider a vowel to be present if it is present in upper case or lower case. 
i.e.a,e,i,o,u or A,E,I,O,U
Examples : 

Input : geeksforgeeks
Output : Not Accepted
All vowels except 'a','i','u' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present

'''
string = input("Enter the string:").lower()

vowels = set("aeiou")
s = set({})
for each in string:
    if each in vowels:
        s.add(each)
    else:
        pass
if len(s) == len(vowels):
    print("Accepted")
else:
    print("Not Accepted")
