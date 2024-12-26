def missing(arr):
    n = len(arr) + 1
    total = n * (n+1) // 2
    miss = sum(arr)
    
    return total - miss

array = input("Enter numbers with space in between: ")
arr = [int(x) for x in array.split()]
result = missing(arr)
print(f"The missing number is: {result}")
