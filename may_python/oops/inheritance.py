# class Parent:
#     def mobile(self):
#         print("samsung")
#     def car(self):
#         print("alto")
#     def bike(self):
#         print("duke 200")

# class Child(Parent):
#     pass

# obj=Child()
# obj.mobile()
# obj.bike()
# obj.car()




class Car:
    def start(self):
        print("car starts")

    def accelerte(self):
        print("car accelerates")

    def brakes(self):
        print("car brakes")


class Swift(Car):
    pass

obj=Swift()
obj.start()


