import math

def print_hello():
    """Print Hello at screen."""
    print("Hello!")

def get_hello():
    """
    Return Hello string

    :return: String value "Hello"
    """
    return "Hello"

def ask_name_and_greet_user():
    name = input('Insert your name please: ')
    name = name.capitalize()
    print(f"Hi, {name}. Would you like to have a Hamburger?")

def calculate_hypotenuse_lenght(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c

def calculate_cathetus_length(c, a):
    b = math.sqrt(c**2 - a**2)
    return b

print_hello()
result = get_hello()
print(result)

ask_name_and_greet_user()

result = calculate_hypotenuse_lenght(3,4)
print(result)

result = calculate_cathetus_length(5,3)
print(result)
