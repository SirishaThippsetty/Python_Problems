'''
A string is given, and you have to find all the words 
(substrings separated by a space) which are greater than the given length k.

Examples:

Input : str = "hello geeks for geeks 
          is computer science portal" 
        k = 4
Output : hello geeks geeks computer 
         science portal
Explanation : The output is list of all 
words that are of length more than k.

'''
input_string = input("Enter the input:")
k = int(input("Enter the number:"))
lst1 = []
lst2 = []
for each in input_string.split( ):
    lst1.append(each)
for each in lst1:
    a = len(each)
    if a >= k:
        lst2.append(each)
print(" ".join(lst2))
