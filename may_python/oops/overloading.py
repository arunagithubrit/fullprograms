# overloading



# def add(n1,n2):
#     return n1+n2

# def add(n1,n2,n3):
#     return n1+n2+n3



# print(add(10,20))





class Calculations:
    # def add(self,n1,n2):
    #     return n1+n2
    
    # def add(self,n1,n2,n3):
    #     return n1+n2+n3
    
    # def add(self,n1,n2,n3,n4):
    #     return n1+n2+n3+n4

    def add(*args,**kwargs):
        return sum(args)
    
obj=Calculations()
obj.add(10,20)

    