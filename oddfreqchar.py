'''
Input : test_str = 'geekforgeeks'
Output : [r,o,f,s] 
Input : test_str = 'g'
Output : [g]

'''
from collections import Counter
# initializing string
test_str = input("Enter the string:")
 
# printing original string
print("The original string is : " + str(test_str))
 
# Odd Frequency Characters
# Using list comprehension + Counter()
res =  [ chr for chr, count in Counter(test_str).items() if count & 1 ]
 
# printing result
print("The Odd Frequency Characters are : " + str(res))