def peak(arr):
    n = len(arr)
    value = []
    for i in range(n):
        if(i==0 or arr[i] > arr[i-1]) and (i==n-1 or arr[i]> arr[i+1]):
            value.append(arr[i])
    return value

array = input("Enter numbers with space in between: ")
arr = [int(x) for x in array.split()]
result = peak(arr)
print(f"The Peak element is: {result}")
