import  numpy as np

m1 = ([1, 2, 4],
      [4, 3, 8],
      [4, 6, 0]
      )
m2 = ([4, 6, 1],
      [9, 3, 2],
      [8, 3 ,1])
add = np.add(m1, m2)
sub = np.subtract(m1 ,m2)
mul = np.multiply(m1, m2)
Mat_mul = np.dot(m1, m2)

print("Sum : ", add)
print("Sub : ", sub)
print("mul : ", mul)
print("mat_mul : ", Mat_mul)