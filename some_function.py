import functools
#lamda function
result = (lambda a,b,c : a * b * c)(1, 2, 3)
print("Lambda : ", result)

#map function
def multiple(number):
    return number*5
num = [1, 2, 3, 4]
result = list(map(multiple,num))
print("Map", result)

#filter function
number = [1,2,2,3,5,6,8]
result = list(filter(lambda a:a%2==0, number))
print("Filter : ", result)

#reduce function
def add_two_numbers(num1, num2):
    return num1+num2
number = [1, 2, 3, 4, 5]
result  = functools.reduce(add_two_numbers, number)
print("Reduce : ",result)