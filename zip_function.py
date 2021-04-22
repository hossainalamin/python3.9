# list1 = ["Alamin ", "Rokib", "Sakib", "Chandan"]
# list2 = [23, 24, 25,22]
#
# result = list(zip('1234', list1, list2))
# print(result)

number = [(1, 2, 4, 5),(5, 6, 8, 9)]
unzip  = list(zip(*number))
print(unzip)