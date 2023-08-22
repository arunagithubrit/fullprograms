from abc import ABC,abstractmethod

class Employee(ABC):
    name:str
    salry:int

    def __init__(self, name,salry):
        self.name=name
        self.salry=salry

    @abstractmethod
    def calculate_salry(self):
        pass

class Manager(Employee):
    def __init__(self, name, salry):
        super().__init__(name, salry)

    def calculate_salry(self):
        return self.salry + 25000

class Developer(Employee):
    def __init__(self, name, salry):
        super().__init__(name, salry)
    
    def calculate_salry(self):
        return self.salry +10000

man=Manager("Kalidas",20000)
print(man.calculate_salry())

dev=Developer('hardin',15000)
print(dev.calculate_salry())