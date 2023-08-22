# text="hai hello evening"
# words=text.split(" ")
# print(sorted(words, key=lambda w:len(w), reverse=True))



# def total(*args,**kwargs):
#     print(kwargs.get('key'))
#     return sum(args)

# print(total(10,20,key="square"))





# def create_person(**kwargs):
#     print(kwargs)

# create_person(name="aruna",age=23)


# class Student:
#     rollno:int
#     name:str
#     course:str

# def __init__(self,**kwargs):
#     self.rollno=kwargs.get("rollno")
#     self.name=kwargs.get("name")
#     self.course=kwargs.get("course")

# def get_student(self):
#     print(self.rollno,self.name,self.course)

# # def __str__(self):
# #     return self.name


# obj=Student(rollno=1000,name="vijay",course="django")
# # print(obj)
# obj.get_student()





class Books:
    name:str
    author:str
    price:int
    pages:int


    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.author=kwargs.get("author")
        self.price= kwargs.get("price")
        self.pages=kwargs.get("pages")

    def __str__(self):
        return self.name
obj=Books(name="my fate",author="aruna",price=890,pages=600)
print(obj)
       
     












