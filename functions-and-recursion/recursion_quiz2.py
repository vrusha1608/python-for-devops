#Write a recursive function to print all the elements in the list (Hint: Use list and index as parameter)

def print_elements_of_list(l1, idx=0):
     if(idx == len(l1)):
          return 
     else:
          print(l1[idx])
          print_elements_of_list(l1, idx+1)


cities = ["Aurangabad","Sangli","Pune","Kolhapur"]

print_elements_of_list(cities)
