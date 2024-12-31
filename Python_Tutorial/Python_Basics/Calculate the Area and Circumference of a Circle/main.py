import math  

radius = float(input("Enter the radius of the circle: "))

if radius < 0:
    print("Error: Radius cannot be negative. Please enter a valid positive number.")
else:
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

print(f"Area: {area}\nCircumference: {circumference}")

