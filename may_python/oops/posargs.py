# def create_person(*args):
#     # print(args)
#     person_name=args(0)
#     age=args(1)

# create_person("aruna",24,"pakad")





def create_person(**kwargs):
    print(kwargs.get("name"))
    
create_person(name="aruna",age=24,place="pakad")


# *args==> tuple format
# **kwargs==> dictionary format

