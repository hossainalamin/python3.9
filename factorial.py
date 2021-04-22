def fact(x):
    result = 1;
    for i in range(1, x+1):
        result = result*i
    print(result)
fact(5)

#using while
def fibonacci(x):
    final = 1
    i = x
    while i >=1 :
        final *= i
        i -= 1
    print(final)
fibonacci(5)
