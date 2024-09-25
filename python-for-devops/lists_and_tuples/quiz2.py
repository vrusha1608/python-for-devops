# WAP to check if a list contains a palindrome of element (Hint: use copy method)
#e.g.
# [1,2,3,2,1]
# [1,"abc","abc",1]

list1 = [1,2,3,2,1,3]

list2 = list1.copy()   # copy of list 1

list3 = list2.reverse() # reverse of copy of list1

if(list1 == list2):
    print("Palindrome")
else:
    print("Not a Palindrome")

