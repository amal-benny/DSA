from collections import Counter
print("-----ANAGRAM CHECKER-------  ")
a =input("Enter a string : " )
b = input("Enter another string : ")

if Counter(a.lower()) == Counter(b.lower()):
    print("The given string is an Anagram")
else:
    print("The given string is not an Anagram")
