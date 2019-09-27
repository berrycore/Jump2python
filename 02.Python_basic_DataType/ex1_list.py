a = [1,2,3,]
b = ['Life','is','too','short']
c = "12345"

print(a[1])     # 2
print(b[1])     # is
print(c[1:3])   # 23
print(c[3:])    # 45

del a[1]
print(a)        # [1,3]

a.append(4)
print(a)        # [1, 3, 4]

a.append([5,6])
print(a)        # [1, 3, 4, [5, 6]]

a = [1,2,3,]
a.insert(1,9)
a.insert(3,9)
print(a)        # [1, 9, 2, 9, 3]

a.remove(9)
print(a)        # [1, 2, 9, 3]

a.append(9)
print(a)        # [1, 2, 9, 3, 9]
print(a.count(9))   # 2

a.extend([4,5])
print(a)        # [1, 2, 9, 3, 9, 4, 5]
