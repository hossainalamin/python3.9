from array import *
touple = ("Alamin", "Rokib", "Sojib", "Chandan")
for name in touple :
    print(name)

list = [1, 2, 3, 4]
total = 0
for element in list :
    total = total + element
print("Sum : ", total)

#using range

total = 0
for i in range(1,11):
    if i % 2 == 0:
        total += i;
print("Even number addition : ", total)

mobile = int(input("Enter the number of mobile you want : "))
available = 10
n = 1
while n <= mobile:
    if n > available:
        break
    else:
        print("There are " ,n , "mobile available")
    n += 1



