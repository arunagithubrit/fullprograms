
def dec_func(fn):#squaring the number n1 and n2 
    def wrapper(n1,n2):
        return fn(n1**2,n2**2)
    return wrapper




@dec_func
def add(n1,n2):
    return n1+n2

@dec_func
def product(n1,n2):
    return n1*n2


print(add(2,3))#4+9=13
print(product(2,3))#4*9=36