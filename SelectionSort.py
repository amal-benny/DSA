def selection(arr):
    length = len(arr) 
    for i in range(length - 1):
        index = i
        for j in  range(i+1, length):
            if arr[j] < arr[index]:
                index = j
        swap(arr, i, index)
    return arr
    
def swap(a, b, c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

array = input("Enter elements with a space in between : ")
arr = [int(x) for x in array.split()]

if arr:
    result = selection(arr)
    print(f"The sorted array is {result}")
else:
    print("Enter a valild array")
