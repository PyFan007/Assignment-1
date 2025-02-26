a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
add = a + b
sub = a - b
mul = a * b
print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
if b == 0:
    print("Division by zero is not defined.")
else:
    div = a / b
    print("Division: ", round(float(div), 2))