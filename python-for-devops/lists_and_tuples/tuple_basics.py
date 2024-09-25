# Basic concepts of Tuple

tup = (2,1,4,3)

print(tup)
print(type(tup))
print(tup[1])
print(tup[2])

#tup[3] = 5      #TypeError: 'tuple' object does not support item assignment

print(tup[1:3])     # Tuple Slicing

print(tup.index(1))

print(tup.count(3))