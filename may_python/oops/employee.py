class Employee:
    id:int
    name:str
    desig:str
    salry:int


    def __init__(self,id,name,desig,salry):
        self.id=id
        self.name=name
        self.desig=desig
        self.salry=salry

    def get_emp(self):
        print(self.name,self.id,self.desig,self.salry)

emp1=Employee(123,"karthik","hr",35000)
emp1.get_emp()


print(dir(emp1))

print(emp1.__class__)
