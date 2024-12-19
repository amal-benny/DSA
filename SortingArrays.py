def sort(arr1,arr2):
    set1 = arr1 + arr2
    return sorted(set1)
    
new1 = input("Enter elements with a space in between : ")
new2 = input("Enter elements with a space in between : ")

arr1 = [int(x) for x in new1.split()]
arr2 = [int(x) for x in new2.split()]

result = sort(arr1,arr2)

if result:
    print(f"The elements after sorting in both arrays are : {result}")
else:
    print("There are no  elements in the given arrays")
                
