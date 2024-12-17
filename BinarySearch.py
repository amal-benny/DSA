def binary(arr,target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

array = input("Enter the element with space in between each : ")
arr = [int(x) for x in array.split()]
arr = sorted(arr)
target = int(input("Enter the value to be found : "))
result = binary(arr, target)

if result is not None:
    print(f"The element {target} is found at the index {result}")
else:
    print(f"The element {target} is not present in the given array")
