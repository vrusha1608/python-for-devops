#  In-build functions of set

nums = {1,2,3,4,5}

nums.add(6)
print(nums)

nums.remove(3)
print(nums)

# nums.remove(8)     #KeyError: 8
# print(nums)         # Element = 8 is not present in set 


nums.add("hello")
nums.add("world")

nums.add((1,4,9,16)) # adding tuple in to set

#nums.add([1,8,27,64]) #adding list in to set ==> TypeError: unhashable type: 'list'

print("Set is =>", nums)

print("Length of set is=>",len(nums))

nums.pop()      # removes random value from set
print("Set is =>", nums)

nums.clear()
print("Set is =>", nums)

nums = {1,2,3,4}
new_nums = {3,4,5,6,7}

intersection_set = nums.intersection(new_nums)
union_set = nums.union(new_nums)

print("Intersected set elements are=>",intersection_set)  # common values of both sets

print("Union of sets=>",union_set)