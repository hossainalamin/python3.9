a = 20
b = 10

a = a+b
b = a-b
a = a-b

print("Here a is : ", a)
print('\n')
print("Here b is : ", b)

#smart way
a, b = b, a
print(a)
print(b)
