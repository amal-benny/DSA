def repeating(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
    return None
    
array = input("Enter numbers with a space in between : ")
arr = [int(x) for x in array.split()]
result = repeating(arr)
if result:
    print(f"The element {result} is the first repeating element in the array \n {arr}")
else:
    print(f"There are no repeating elements in the array {arr}")
