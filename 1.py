# DemoBool.py
a=[1,2,3]
b=a
a[0]=38
print(a)
print(b)
print(id(a), id(b))

print("...깊은 복사...")
a=[1,2,3]
b=a[:]
a[0]=38
print(a)
print(b)
print(id(a), id(b))
