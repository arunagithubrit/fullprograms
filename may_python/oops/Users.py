class Users:
    data=[
        {"id":1,"username":"john","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
    ]

    def get(self):
        return self.data
    def retrieve(self,id):
      
        return [u for u in self.data if u.get("id")==id]
    def post(self,obj):
        self.data.append(obj)
    def destroy(self,id):
        obj=[u for u in self.data if u.get("id")==id][0]
        self.data.remove(obj)
        # for u in self.data:
        #     if u.get("id")==id:
        #         obj=u
        #         self.data.remove(obj)
    def put(self,id,value):
        obj=[u for u in self.data if u.get("id")==id][0]
       
        print(value[0])
        pos=self.data.index(obj)
        self.data[pos]=value[0]
    
obj=Users()
payload={"id":5,"username":"vinus","email":"vinus@gmail.com","password":"password@123"},
obj.put(5,payload)
print(obj.retrieve(5))
print(obj.get())




# a={"aruna":"age"},
# print(type(a))


# tp=({"a":1},)
# print(tp[0])


# user_data={"id":7,"username":"ram","email":"ram@gmail.com","password":"password@123"}
# obj.post(user_data)
# print(obj.get())
# obj.destroy(6)

# obj.destroy(5)
# print(obj.get())


# print(obj.get())
# print(obj.retrieve(2))





# mobile,book,,,,,=[list,detail,create,update,delete] (C,R,U,D)
# C=>create
# R=>read/retrieve
# U=>update
# D=>delete


# convention but not a rule

# list=>get()
# detail=>retrieve(id)
# create=>post()
# update=>put(id)
# delete=>destroy(id)


# box={"id":1,"color":"green","size":"s"}
# new_box={"id":1,"color":"red","size":"m"}

# box=new_box
# print(box)



# class Users:
#     data=[
#         {"id":1,"username":"john","email":"jhon@gmail.com","password":"password@123"},
#         {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
#         {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
#         {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
#         {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
#         {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
#     ]

#     def get(self):
#         return self.data
#     def retrieve(self,id):
      
#         return [u for u in self.data if u.get("id")==id]
#     def post(self,obj):
#         self.data.append(obj)
#     def destroy(self,id):
#         obj=[u for u in self.data if u.get("id")==id][0]
#         self.data.remove(obj)
#         # for u in self.data:
#         #     if u.get("id")==id:
#         #         obj=u
#         #         self.data.remove(obj)
#     def put(self,id,value):
#         obj=[u for u in self.data if u.get("id")==id][0]
       
#         print(value)
#         pos=self.data.index(obj)
#         self.data[pos]=value
    
# obj=Users()
# payload={"id":5,"username":"vinus","email":"vinus@gmail.com","password":"password@123"}
# obj.put(5,payload)
# print(obj.retrieve(5))
# print(obj.get())














