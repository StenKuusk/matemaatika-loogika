'''Practice different mathematical expressions.'''

# declare num_a and num_b
num_a = 5
num_b = 3

# 1. Sum and difference

sum = num_a + num_b
print(f"{num_a} + {num_b} = {sum}")
difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")

print('----------------------------')

# 2. Float division

division = num_a / num_b
print(f"{num_a} / {num_b} = {division}")

# 3. Integer division

division = num_a // num_b
print(f"{num_a} // {num_b} = {division}")

# 4. Powerful operations

multiply_numbers = num_a * num_b
print(f"{num_a} * {num_b} = {multiply_numbers}")
power = num_a ** num_b
print(f"{num_a} ** {num_b} = {power}")
remainder = num_a % num_b
print(f"{num_a} % {num_b} = {remainder}")

# 5. Find average

average = (num_a + num_b) / 2
print(f"({num_a} + {num_b}) / 2 = {average}")

# 6. Area of a circle

import math
radius = 2
circle = math.pi * (radius ** 2)
circle_area = round(circle, 2)
print(f"{math.pi} * ({radius} ** 2) = {circle}")
print(f"{round(circle), 2} = {circle_area}")

# 7. Area of an equilateral triangle

side_length = 8
triangle = side_length * (math.sqrt(3) / 4)
print(triangle)
triangle_area = round(triangle)
print(triangle_area)

# 8. Calculate discriminant

a = 2
b = 3
c = 4
discriminant = b ** 2 - (4 * a * c)
print(discriminant)

# 9. Calculate hypotenuse length

c = math.sqrt(b ** 2 + a ** 2)
print(round(c))

# 10. Calculate cathetus length

b = math.sqrt(c ** 2 - a ** 2)
print(round(b))

# 11. Time converter

seconds = 121260
minutes = seconds // 60
print(minutes)
hours = seconds // 3600
print(hours)

# 12. Student helper

angle = 70
sine = math.sin(angle)
print(sine)
cosine = math.cos(angle)
print(cosine)

# 13. Greetings

n = 4
lots_of_heys = n * "Hey"
print(lots_of_heys)

# 14. Adding numbers

num_a = 123
num_b = 456
string_numbers = str(num_a) + str(num_b)
print(string_numbers)
