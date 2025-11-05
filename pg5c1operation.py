num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

print("Addition:",num1, "+",num2,"=",num1 + num2)
print("Subtraction:",num1, "-", num2, "=", num1 - num2)
print("Multiplication:",num1,"*",num2, "*", num1 * num2 )

if num2 != 0:
    print("Division:",num1, "/" , num2,"=", num1 / num2)
else:
    print("Division: Cannot be divide by zero!")
