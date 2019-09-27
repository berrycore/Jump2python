# set features
#    1) There is no duplication
#    2) There is no order

set1 = set([1,2,3])
print(set1)               # {1, 2, 3}

set2 = set("Hello")
print(set2)               # {'o', 'e', 'l', 'H'}

list2 = list(set2);
print(list2)            # ['e', 'H', 'o', 'l']

tuple2 = tuple(list2)
print(tuple2)           # ('e', 'H', 'l', 'o')
##################################################
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

################# Intersection ##################
s3 = s1 & s2
print(s3)               # {4, 5, 6}

s3 = s1.intersection(s2)
print(s3)               # {4, 5, 6}

################# union ##################
s3 = s1 | s2
print(s3)               # {1, 2, 3, 4, 5, 6, 7, 8, 9}

s3 = s1.union(s2)
print(s3)               # {1, 2, 3, 4, 5, 6, 7, 8, 9}


################# difference ##################
s3 = s1 - s2
print(s3)               # {1, 2, 3}

s3 = s1.difference(s2)
print(s3)               # {1, 2, 3}

s3 = s2.difference(s1)
print(s3)               # {8, 9, 7}

################# add ##################
s1 = set([1,2,3])
s1.add(4)
print(s1)               # {1, 2, 3, 4}

s1.add(1)
print(s1)               # {1, 2, 3, 4}    <- nop


################# update ##################
s1 = set([1,2,3])
s1.update([3,5,6])
print(s1)               #   {1, 2, 3, 5, 6}

################# remove ##################
s1 = set(['a','b','c'])
# s1.remove(2)
# print(s1)

# Type/ex4_set.py", line 61, in <module>
#    s1.remove(2)
# KeyError: 2


s1.remove('b')
print(s1)           # {'a', 'c'}
