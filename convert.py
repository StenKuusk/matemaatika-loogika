''''
number_as_string = input("Enter a decimal number:")
# decimal -> binary

# input() gives us text, let's convert it to number
number = int(number_as_string)

# here we gather the result
result = ""

while number > 0:
    remainder = number % 2
    print(remainder)
    result = str(remainder) + result
    number = number // 2

print("Result in binary:", result)
'''
# binary -> decimal
binary_as_string = input("Enter a binary number:")
print(binary_as_string)
binarycount = len(binary_as_string)
print()
decimal_number = 0
pow_value = 0
while(binarycount >= 0):
    print(binary_as_string[binarycount-1])
    decimal_number += pow(2, pow_value) * int(binary_as_string[binarycount -1])
    binarycount -= 1
    pow_value += 1

    print("Result in decimal:", decimal_number)