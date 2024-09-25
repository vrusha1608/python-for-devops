# Demo on in-buil functions of list

list = [2,1,3]

print(list)

list.append(4);  #Append an element at the end of the list
print(list)

list.sort()     #By-default sorts the list in ascending order
print(list)

list.sort(reverse=True)     # Sorting in reverse/ descending order
print(list)

list.reverse()     #Reverses the list 
print(list)

list.insert(2,5) # inserts element at index
print(list)

list.remove(5)  # removes first occurence of an element
print(list)

list.pop(2)     # removes element at index
print(list)
