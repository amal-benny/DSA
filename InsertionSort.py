def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > arr[i]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr
    
array = input("Enter elements with space in between : ")
unsorted = [int(x) for x in array.split()]

result = insertion(unsorted)

print(f" After Sorting {result}")
