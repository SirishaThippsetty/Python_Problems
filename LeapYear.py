# Find the leap year

'''
Logic: 
The year is multiple of 400.
The year is multiple of 4 and not multiple of 100

'''
year = int(input("Enter the year:"))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("The given year",year,"is Leap year")
else:
    print("The given year",year,"is not leap year")