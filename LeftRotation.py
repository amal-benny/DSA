def left(arr,d):
    n = len(arr)
    d = d % n
    result = arr[d:] + arr[:d]
    return result if arr else []
        
array = input("Enter numbers with space inbetween : ")
arr = [int(x) for x in array.split()]
d = int(input("Enter how many times the array should be rotated : " ))

if arr:
    result = left(arr,d)
    print(f"The original array is {arr}")
    print(f"The array after rotating for {d} times to the left is \n {result}")
else:
    print("Enter values for array")
