a = 10
b = 20
c = 50

if b>a :
    print("If condition : ", b)
elif b<a :
    print("Elseif conditon : ", b)

input_1 = int(input("Enter the first input : "))
input_2 = int(input("Enter second input : "))
if input_2 > input_1 :
    Sub = input_2-input_1
    print("The subtraction : ",Sub)
elif input_1 > input_2 :
    sum = input_1 + input_2
    print("The sum : ", sum)
#even odd
number = int(input("Enter the number : "))
if number % 2 == 0 :
    print("The number is even")
else:
    print("The number is odd")

# nested
number_for_check = int(input("Enter the number for check : "))
if number_for_check < 0 :
    print("The number is negetive", number_for_check)
elif number_for_check > 0 :
    if number_for_check % 2 == 0 :
        print("The number if even")
    else:
        print("The number is odd")


