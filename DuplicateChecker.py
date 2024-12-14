from collections import Counter
print("------Duplicates in an Array------")
a = input("Enter number with spaces : ")
a = [int(x) for x in a.split()]

count = Counter(a)
duplicates = []

for i in count:
    if count[i] >=2:
        duplicates.append(i)
        
if  duplicates:
    print(f"The duplicates in the array are {duplicates} ")
else:
    print("No duplicates found")
