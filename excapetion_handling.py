a = 2
b = 0
try:
    print("Resourse open: ")
    print(a/b)
except Exception as e:
    print("You can not devide by zero : ", e)
finally:
    print("Resource closed")
print("ok,Bye")

#assertation

def mysalary(salary):
    assert salary > 0, "Salary can not be less than zero"
    print("My salaray is : ", salary)
mysalary(-50000)
