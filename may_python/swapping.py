# swaping

num1=10
num2=20

print("print b4 swapping:","num1=",num1,"num2=",num2)

# temp=num1
# num1=num2
# num2=temp

(num1,num2)=(num2,num1)
print("print after swapping:","num1=",num1,"num2=",num2)

# another logic
num1=num1+num2
num2=num1-num2
num1=num1-num2