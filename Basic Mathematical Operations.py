num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = int(num1 + num2)
subtraction = int(num1 - num2)
multiplication = int(num1 * num2)
if num2 != 0:
    division = round(num1 / num2,1)
else:
    division = "Undefined (cannot divide by zero)"


print(f"\nAddition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
