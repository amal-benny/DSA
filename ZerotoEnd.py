def non(arr):
    arr1 = []
    arr2 = []
    
    for i in arr:
        arr1.append(i) if i == 0 else arr2.append(i)
    return arr2 + arr1
    
array = input("Enter the values with space in between : ")
arr = [int(x) for x in array.split()]
result = non(arr)

print(f"The aray after moving zeros to the end is {result}")
            
