def bubble( arr):
    seen = True
    while(seen):
        seen = False
        for i in range(len(arr) - 1):
            if arr[i] > arr [i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                seen = True
    return arr
    
array = input("Enter numbers with space in between : ")
arr = [int(x) for x in array.split()]

if arr:
    result = bubble(arr)
    print(f"The sorted array is {result}")
else:
    print("Enter some values in the array")
