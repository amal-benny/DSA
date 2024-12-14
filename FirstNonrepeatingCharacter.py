from collections import Counter
print("-----First Non Repeating Character--------  ")
a = input("Enter a string : " )
count = Counter(a.lower())

for char in a:
    if count[char.lower()] == 1:
        print(f"The first non repeating character is {char}")
        break
else:
    print("There are no non-repeating characters")
