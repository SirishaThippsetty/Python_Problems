'''
Python program for removing i-th character from a string

Given the string, we have to remove the ith indexed character from the string.
 In any string, indexing always start from 0. Suppose we have a string geeks then 
 its indexing will be as –

g e e k s
0 1 2 3 4
Examples :

Input : Geek
        i = 1
Output : Gek

'''
ip_str = input("Enter the input string:")
ith_index = int(input("Enter the number index:"))
new_str = ip_str[:ith_index] + ip_str[ith_index+1:]
print(new_str)