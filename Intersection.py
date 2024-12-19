def intersect(arr1,arr2):
    set1 = set(arr1)
    return sorted(set1.intersection(arr2))
    
new1 = input("Enter elements with a space in between : ")
new2 = input("Enter elements with a space in between : ")

arr1 = [int(x) for x in new1.split()]
arr2 = [int(x) for x in new2.split()]

result = intersect(arr1,arr2)

if result:
    print(f"The elements that are common in both arrays are : {result}")
else:
    print("There are no common elements in the given arrays")
                
