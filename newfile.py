🟢 1️⃣ Area of a Circle – Code Explanation

Code:

pi = 3.14159
radius = float(input("Enter the radius of the circle: "))

area = pi * radius * radius

print("Area of the circle is:", area)

Explanation:

pi = 3.14159
This line stores the value of π (pi) in a variable called pi.

radius = float(input("Enter the radius of the circle: "))

input() takes the radius from the user

float() converts the input into a decimal number

The value is stored in the variable radius


area = pi * radius * radius
This line applies the formula Area = π × r²

radius * radius means r²


print("Area of the circle is:", area)
This line displays the calculated area on the screen.



---

🟢 2️⃣ Area of a Square – Code Explanation

Code:

side = float(input("Enter the side of the square: "))

area = side * side

print("Area of the square is:", area)

Explanation:

side = float(input("Enter the side of the square: "))

Takes the length of the side from the user

Converts it into a decimal value

Stores it in variable side


area = side * side
This line calculates the area using the formula Area = side²

print("Area of the square is:", area)
Displays the area of the square.



---

🟢 3️⃣ Area of a Triangle – Code Explanation

Code:

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print("Area of the triangle is:", area)

Explanation:

base = float(input("Enter the base of the triangle: "))
Takes the base value from the user and stores it in base

height = float(input("Enter the height of the triangle: "))
Takes the height value from the user and stores it in height

area = 0.5 * base * height
Applies the formula Area = ½ × base × height

print("Area of the triangle is:", area)
Displays the calculated area.



---

🔑 Common Concepts Used in All Programs

Concept	Explanation

input()	Takes input from the user
float()	Converts input into decimal number
Variable	Stores data values
*	Multiplication operator
print()	Shows output on screen