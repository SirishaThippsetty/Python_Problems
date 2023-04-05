'''
Area of circle = pi * r * r
Area of cube = 6 * a * a
Area of cylinder = 2pi * r * h + 2pi * r * r
Area of sphere = 4pi * r * r
'''
import math
pi = math.pi
print("1.Circle")
print("2.Cube")
print("3.Cylinder")
print("4.Sphere")
number = int(input("Enter the number(1/2/3/4):"))

if number == 1:
    radius = int(input("Enter the radius:"))
    area_circle = pi * (radius ** 2)
    print("Area of Circle is",area_circle)
elif number == 2:
    a = int(input("Enter the input:"))
    area_cube = 6 * a * a
    print("Area of cube is",area_cube)
elif number == 3:
    radius = int(input("Enter the radius:"))
    height = int(input("Enter the height:"))
    a = 2 * pi * radius * height
    b = 2 * pi * radius * radius
    area_cylinder = a + b
    print("Area of Cylinder is",area_cylinder)
elif number == 4:
    radius = int(input("Enter the radius:"))
    area_sphere = 4 * pi * radius * radius
    print("Area of Sphere is",area_sphere)
else:
    print("You entered wrong input number!Try again with correct number")
