#  Figure out a way to store 9 and 9.0 as a separate values in the set. (You can take help of built-in data types)

nums = {9,9.0}
print(nums)

nums1 = {"9", "9.0"}    # Solution1
print(nums1)

nums_dict = {("float",9.0),("int",9)}

print(nums_dict)