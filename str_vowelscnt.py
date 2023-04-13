'''
Python program to count number of vowels using sets in given string

Given a string, count the number of vowels present in given string using Sets.


Input : GeeksforGeeks
Output : No. of vowels : 5

Input : Hello World
Output : No. of vowels :  3

'''

vowels = set('aeiou')
input_str = input("Enter the string:").lower()
count = 0
for each in input_str:
    for i in vowels:
        if each == i:
            count += 1
print("No of vowels:",count)

# List comprehension Method

count1 = len([char for char in input_str if char in vowels])
print("No of vowels:",count1)