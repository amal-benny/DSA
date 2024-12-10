def palindrome(word):
   
    new = word.lower().replace(" ", "")
    return "Palindrome" if new == new[::-1] else "Not a palindrome"

a = input("Enter a number or string to be checked: ")
print(f"{a} is {palindrome(a)}")
