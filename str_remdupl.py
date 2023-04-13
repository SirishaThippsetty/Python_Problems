'''
Remove all duplicates from a given string in Python

Input : geeksforgeeks 
Output : geksfor

'''

input_str = input("Enter the string:")
output_str = "".join(dict.fromkeys(input_str))
print(output_str)
