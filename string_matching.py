'''
Python | Count the Number of matching characters in a pair of string

Given a pair of non-empty strings. Count the number of matching characters 
in those strings (consider the single count for the character which have 
duplicates in the strings). 

Examples:

Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4 
(i.e. matching characters :- a, d, e, f)

Input : str1 = 'aabcddekll12@'
        str2 = 'bb22ll@55k'
Output : 5 
(i.e. matching characters :- b, 1, 2, @, k)

'''
str1 = input("Enter the string1:")
str2 = input("Enter the string2:")
lst = []

for each in str1:
    for i in str2:
        if i == each:
            lst.append(i)
a = set(lst)
print(len(a))

## ANother one

# count function count the common unique
# characters present in both strings .
# def count(str1 ,str2) :
#     # set of characters of string1
#     set_string1 = set(str1)
 
#     # set of characters of string2
#     set_string2 = set(str2)
 
#     # using (&) intersection mathematical operation on sets
#     # the unique characters present in both the strings
#     # are stored in matched_characters set variable
#     matched_characters = set_string1 & set_string2
 
#     # printing the length of matched_characters set
#     # gives the no. of matched characters
#     print("No. of matching characters are : " + str(len(matched_characters)) )
 
 
# # Driver code
# if __name__ == "__main__" :
 
#     str1 = 'aabcddekll12@'  # first string
#     str2 = 'bb2211@55k'     # second string

#       # call count function
#     count( str1 , str2 )
