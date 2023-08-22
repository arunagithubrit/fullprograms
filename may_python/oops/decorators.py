# class Mobile(object):
#     name:str
#     price:int
#     display:str

#     def __init__(self,**kwargs):
#         self.name=kwargs.get("name")
#         self.price=kwargs.get("price")
#         self.display=kwargs.get("display")

#     def __str__(self):
#         return self.name
#     @property
#     def get_price(self):
#         return self.price
#     @property
#     def get_disc_price(self):
#         return self.price-1000
    
# obj=Mobile(name="redmi note 8",price=24000,display="amoled")
# print(obj.get_price)
# print(obj.get_disc_price)








def dec_func(fn): #fn=sub(10,20)
    def inner_func(n1,n2):#inner_func(10,20)
        if n1<n2:#10<20
            (n1,n2)=(n2,n1)#n1=20 n2=10
        return fn(n1,n2)#sub(20,10)
    return inner_func

@dec_func
def sub(n1,n2):
    return n1-n2
@dec_func
def div(n1,n2):
    return n1/n2


print(sub(10,20))
print(div(5,20))























