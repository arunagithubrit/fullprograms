class Student:
    rolno:int
    name:str
    course:str

    def __init__(self,rol,name,course):
    # def add_student(self,rol,name,course):
        # initializinf instance variable(here constructor is not there)
        self.rolno=rol
        self.name=name
        self.course=course
    
    def get_student(self):
        print(self.rolno,self.name,self.course)


# obj1=Student()
# obj1.add_student(1,"aruna","django")
# obj1.get_student()
# obj2=Student()
# obj2.add_student(2,"aparna","python")

obj1=Student(1,"aruna","django")
obj1.get_student()
obj2=Student(2,"aparna","python")
obj2.get_student()



lst=list()
