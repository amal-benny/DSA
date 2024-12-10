def check(word):
    vowels = ["a", "e", "i", "o", "u"] 
    new = word.lower().replace(" ", "")  
    count = 0  
    for char in new:
        if char in vowels:
            count += 1
    return count

a = input("Enter a string: ")
print(f"The number of vowels in '{a}' is {check(a)}.")
