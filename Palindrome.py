input_one = input("Enter the input:")
input_lower = input_one.lower()
if input_lower == input_lower[::-1]:
    print("Given input is Palindrome")
else:
    print("Given input is not Palindrome")