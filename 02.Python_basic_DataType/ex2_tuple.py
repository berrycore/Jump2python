t1 = ()
print(t1)       #   ()

t2 = (1,)
print(t2)       #   (1,)

t3 = (1,2,3)
print(t3)       #   (1,2,3)

t4 = 1,2,3
print(t4)       #   (1, 2, 3)

t5 = ('a', 'b', ('ab','cd'))
print(t5)

# del t5[1]
# TypeError: 'tuple' object doesn't support item deletion

t1 = (1,2,'a','b')
print(t1[0])        # 1
print(t1[3])        # b
print(t1[1:])       # (2, 'a', 'b')
t2 = (3,4)
t3 = t1 + t2;
print(t3)        # (1, 2, 'a', 'b', 3, 4)
