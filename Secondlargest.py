from array import array

arr = input("Enter the elements separated by a space: ")
arrnew = array("i", [int(num) for num in arr.split()])

largest = max(arrnew)
arrnew.remove(largest)  

second_largest = max(arrnew)

print(f"The second largest value in the given array is {second_largest}")
