# class Myclass:
#     def instance_method(self):
#         print("inside instance method")

#     @staticmethod
#     def static_methods():
#         print("static method")


# obj=Myclass()
# obj.instance_method()

# Myclass.static_methods()


from datetime import date
# import datetime
class Operations:
    num1:int
    num2:int

    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def add(self):
        return self.num1+self.num2
    
    def product(self):
        return self.num1*self.num2
    
    @staticmethod
    def get_date():
        return date.today()
    
op=Operations(10,20)
print(Operations.get_date())
# print(op.add())
# print(op.product())


    

