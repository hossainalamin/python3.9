from array import *
from numpy import *
import sys
# salary = array('i', [2500, 3000, 4000, 5000])
# print(salary)
# for i in range(4):
#     print(salary[i])
# salary.append(6000)
# print(salary)
# salary.remove(6000)
# print(salary)
# salary.reverse()
# print(salary)

list = ['1', 'Alamin', '4.5']
print(list)

list1 = [4, ["Hossian", 24], 56]
print(list1[1][1])
list.extend([1, 2, 3])
print(list)
list1.remove(list1[2])
print(list1)

touple = (1, 2, "alamin")
# touple[2] = 10 not allow
print(touple)
# touple less memmory than list
print('touple', sys.getsizeof(touple))
print ('list', sys.getsizeof(list))

set = {1, 2, 3}
set.add(4)
print(set)
set1 = {9, 10, 11}

set.update([5, 6, 7])
print("Update", set)

set.update([100, 200], set1)
print("Update", set)

set.discard(11)
print("Discard", set)

# set inter section

s1 = {1, 2, 3}
s2 = {4, 2, 1}
s3 = {4, 2, 3}
s4 = s1.intersection("intersection", s3, s2)
s6 = s1.union(s2)

#s1|s2 union
print(s4)
print("union", s6)


s5 = s1.difference(s2)
print("Difference", s5)

array1 = array([
    [1, 2, 3],
    [2, 3, 4]
])
print(array1)
array2 = array1.flatten()
print(array2)

array3 = array2.reshape(3,2)
print(array3)

array4 = array3.reshape(1,3,2)
print(array4)

print(array4.ndim)










