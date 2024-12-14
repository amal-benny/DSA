from collections import Counter

print("------Remove duplicates in an Array------")
a = input("Enter numbers with spaces: ")
a = [int(x) for x in a.split()]

count = Counter(a)
duplicates = []

for i in a:
    if count[i] >= 2 and i not in duplicates:
        duplicates.append(i)

result = [x for x in a if x not in duplicates]

if result:
    print(f"The array before removing duplicates is {a}")
    print(f"The array after removing duplicates is {result}")
else:
    print("No elements left after removing duplicates")
