s = input("Enter the string: ")
n = int(input("Enter the number of copies (non-negative integer):"))

if n >=0:
    result = s * n
    print("Result:", result)
else:
    print("Please enter a non-negative integer for the number of copies.")
