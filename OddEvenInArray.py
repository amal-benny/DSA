from array import array

arr = input("Enter the elements separated by a space: ")
arrnew = array("i", [int(num) for num in arr.split()])

odd = 0
even = 0

for i in arrnew:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"The number of even numbers in the given array is {even}")
print(f"The number of odd numbers in the given array is {odd}")
