def switch(a, b, c):
    if a == 1:
        operator = "addition"
        result = b + c
    elif a == 2:
        operator = "subtraction"
        result = b - c
    elif a == 3:
        operator = "multiplication"
        result = b * c
    elif a == 4:
        if c != 0:
            operator = "division"
            result = b / c
        else:
            operator = "division"
            result = "not possible (division by zero)"
    return operator, result

print("------CALCULATOR--------")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

a = int(input("Enter your choice: "))

if a not in [1, 2, 3, 4]:
    print("Invalid Choice, Run the program again and enter a valid choice")
else:
    b = int(input("Enter a number: "))
    c = int(input("Enter another number: "))
    operator, result = switch(a, b, c)
    print(f"The {operator} of {b} and {c} is {result}.")
