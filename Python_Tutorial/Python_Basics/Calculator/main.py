first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

if second_number != 0:
    division = first_number / second_number
else:
    division = "undefined (cannot divide by zero)"

print(f"Addition: {first_number} + {second_number} = {addition}")
print(f"Subtraction: {first_number} - {second_number} = {subtraction}")
print(f"Multiplication: {first_number} * {second_number} = {multiplication}")
print(f"Division: {first_number} / {second_number} = {division}")