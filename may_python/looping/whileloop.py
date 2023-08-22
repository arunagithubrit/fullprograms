# i=1
# while(i<=5):
#     print(i)
#     i+=1


# sum of 10 natural nos

# num=1
# sum=0
# while(num<=10):
#     sum+=num
#     num=+1
# print("sum of 10 natural nos:",sum)


# factorial of a number

# num=5
# fact=1
# while(num>=1):
#     fact*=num
#     num-=1
# print("factorial :",fact)


# print even and odd number within a range

# i=1
# while(i<=20):
#     if i%2==0:
#         print("even",i)
#     else:
#         print("odd",i)
#     i=i+1


# assignmnt
# sum of all even nos and odd nos
# limit=25
# start=1
# even_sum=0
# odd_sum=0

# for i in range(start,limit):
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
#     i+=1
# print("even sun: ",even_sum)
# print("odd sum:",odd_sum )


# while(start<=limit):
#     if start%2==0:
#         even_sum+=start
#     else:
#         odd_sum+=start
#     start+=1
# print("even sum:",even_sum)
# print("odd sum:",odd_sum)




# ip=>2 o/p=>2+22    i/p=>3  o/p=>3+33+333 


# ip=>123 o/p=>1,2,3

# num=123
# while(num!=0):
#     digit=num%10
#     print(digit)
#     num=num//10



# print sum of digit in a given number
# i/p=>123
# o/p=>1+2+3

# num=123
# sum=0
# while(num!=0):
#     digit=num%10
#     sum+=digit
#     num//=10
# print("sum=",sum)





# armstrong number logic
# 153=1**3+5**3+3**3
# 370=3**3+7**3+0**3
# 1634=1**4+6**4+3**4+4**4
num=153
cnt=len(str(num))
org=num
sum=0
while(num!=0):
    digit=num%10
    sum+=digit**cnt
    num//=10
if (sum==org):
    print("armstrong number")
else:
    print("not armstrong")



# i/p=>123
# o/p=>1**3+2**3+3**3
num=153
sum=0
while(num!=0):
    digit=num%10
    sum+=digit**3
    num//=10
print("sum=",sum)















