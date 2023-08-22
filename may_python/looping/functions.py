# print() display msg in console
# type()
# input() to read msg from console

# functions are used to perform a specific task

# num1=input("enter the value: ")
# print(num1)


# function for addition and subtraction

def add(n1,n2):
    res=n1+n2
    return res

def sub(n1,n2):
    res=n1-n2
    return res

print(add(10,20))

sub_res=sub(100,40)
print(sub_res)


def smart_sub(n1,n2):
    if n1>n2:
        return n1-n2
    else:
        return n2-n1
print("smart subtraction:",smart_sub(20,30))



def smart_sub(n1,n2):
    # if n1>n2:
    #     return n1-n2
    # else:
    #     return n2-n1
    return n1-n2 if n1>n2 else n2-n1
n1=int(input("enter num1:"))
n2=int(input("enter num2:"))
print("smart subtraction:",smart_sub(n1,n2))



# function for cubing a number

def cube(num1):
    res=num1**3
    return res

print(cube(2))


# function for multiplication using 3 parameters

def mult(n1,n2,n3):
    return n1*n2*n3
print(mult(2,3,4))

# function max_two with 2 parameters that return largest number
def max_two(n1,n2):
    return n1 if n1>n2 else n2
    # if n1>n2:
    #     return n1
    # else:
    #     return n2
    
print(max_two(100,5))
    


# function min_two with 2 parameters that return largest number
def min_two(n1,n2):
    return n1 if n1<n2 else n2

print(min_two(10,24))

# function max_three with 3 parameters that return largest number


def max_three(n1,n2,n3):
    # if n1>n2 and n1>n3:
    #     return n1
    # elif n2>n3:
    #     return n2
    # else:
    #     return n3
    return n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
    
print(max_three(100,200,30))




def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

print("factorial=",factorial(4))



def prime(num):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    return "prime number" if is_prime==True else "not prime"

print("prime or not: ",prime(4))
























