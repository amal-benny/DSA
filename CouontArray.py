from array import array

arr = input("Enter the elements seperated by a space : ")
arrnew = array("i",[int(num) for num in arr.split()])

count = 0

for i in arrnew:
    count += i
print(count)
