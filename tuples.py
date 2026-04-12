# tuples in python are immutable once its created u cant able to change its value

tup=(1,2,3,4)
print(tup)
print(len(tup))
print(type(tup))

#tuple slicing
print(tup[:2])
print(tup[2:])
print(tup[0:3])

#tuple methods

print(tup.index(2)) # the element we search for
print(tup.count(1)) # we will count the occurances of the element