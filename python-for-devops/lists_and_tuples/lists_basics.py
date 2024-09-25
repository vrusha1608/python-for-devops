# List Basic Concepts Implementation

marks = [34,87,97,69,74]

print(marks)

print("Third Element of list:", marks[2])

print("Length of list is =", len(marks))

marks[3] = 79

print("New List is =>", marks)

#print(marks[6]) #IndexError: list index out of range

# List slicing

print(marks[3:])    #[69,74]
print(marks[:3])    #[34,87,97]