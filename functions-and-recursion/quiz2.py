# WAF to print the elements of the list in a single line. (list is the parameter)

list1 = ["Aurangabad","Sangli","Pune","Kolhapur"]

def print_list_in_single_line(list1):
    for el in list1:
        print(el, end=" ")

print_list_in_single_line(list1)