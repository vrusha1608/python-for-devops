# basic program on recursion

def show(num):
    if(num==0):
        return
    print(num)
    show(num-1)


show(5)