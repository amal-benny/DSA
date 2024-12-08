def check(num):
    return "even" if num % 2 == 0 else "odd"
num = int(input("Enter the number to be checked : "))
print(f"The number {num} is an {check(num)} number")
