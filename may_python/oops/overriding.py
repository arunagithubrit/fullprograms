# class Parent:
#     def property(self):
#         print("2 car 5kilo gold 10lakh rs")

#     def proposal(self):
#         print("proposal with gopal")
# class Child(Parent):
#     def proposal(self):
#         print("with amal")

# ch=Child()
# # print(ch.property())
# ch.proposal()





class Parent:
    def vehicles(self):
        self.context=["passionpro","duke200"]
        return self.context
    
class Child(Parent):
    def vehicles(self):
        self.context=super().vehicles()
        self.context.append("ktm")
        return self.context
    
obj=Child()
print(obj.vehicles())
        