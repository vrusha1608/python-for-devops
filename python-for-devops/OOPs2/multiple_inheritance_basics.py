# program on multiple inheritance

class A:
    a = "Welcome to class A"

class B:
    a = "Welcome to class B"

class C(A, B):
    c = "Welcome to class C"

# a1 = A()
# b1 = B()

c1 = C()

print(c1.a)
print(c1.a)