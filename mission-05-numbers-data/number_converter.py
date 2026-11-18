
# Mission 5 - Number Converter
# Convert a decimal number into binary and hexadecimal.

number = int(input("Enter a positive decimal number: "))

binary_number = bin(number)
hexadecimal_number = hex(number)

print("Decimal:", number)
print("Binary:", binary_number)
print("Hexadecimal:", hexadecimal_number)
