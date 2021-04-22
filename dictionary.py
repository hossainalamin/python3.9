d1 = {"name" : "MD Alamin Hossain", "age" : 23}
print(d1['name'])
d2 = d1.copy()
print("Copy : ", d2)
d1['university'] = "JnU"
print("D1:", d1)
d1.pop("university")
print("Pop : ", d1)
d1.clear()
print("Clear: ", d1)

print("Item", d2.items())
print("keys", d2.keys())

student = {1: {"Name" : "Md.Alamin Hossain", "Roll" : 123},
           2: {"Name" : "Rokibul Islam", "Roll" : 321}}
print("Nested : ", student)
print("Number 1:", student[1]["Name"])

student[3] = {}
student[3]['name'] = "Sakib"
student[3]["Roll"] = "456"

print(student)

del student[2]
print("Romove", student)







