# Write a recursive function to calculate the sum of first n natural numbers

def find_sum_of_n_natural(num):
    if(num==0):
        return 0
    else:
        return num+find_sum_of_n_natural(num-1)


ans = find_sum_of_n_natural(8)

print("Result is=>", ans)