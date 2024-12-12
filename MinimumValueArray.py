from array import array

arr = input("Enter the elements separated by a space: ")
arrnew = array("i", [int(num) for num in arr.split()])

minimum = arrnew[0] 

for i in arrnew:
    if i < minimum:
        minimum = i
  
print(f"The minimum value in the given array is {minimum}")
