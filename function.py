def fname():
    print("Inside the function\n")
print("Outside the function")
fname()

def sum(a,b):
    return a + b
result = sum(10, 15)
print("Sum is : ", result)

def fName(*num):
    result = 0
    for i in num:
        result += i
    print(result)
fName(1,2,3,4)

#kwarg

def detail(**info):
    print(info)
detail(name = "Alamin", age = "23", university = "JnU", country = "Bangladesh")