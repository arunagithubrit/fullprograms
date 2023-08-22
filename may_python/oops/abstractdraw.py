# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
# class Rectangle(Shape):
#     def draw(self):
#         print("drawing rectangle")

# class Triangle(Shape):
#     def draw(self):
#         print("drawing triangle")


# obj=Triangle()
# obj.draw()






# from abc import ABC,abstractmethod

# class Shape(ABC):
#     shape_name:str

#     def __init__(self,name):
#         self.shape_name=name 
        
#     @abstractmethod
#     def draw(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, name):
#         super().__init__(name)

#     def draw(self):
#         print(f"{self.shape_name} drawing")

# class Triangle(Shape):
#     def __init__(self, name):
#         super().__init__(name)

#     def draw(self):
#         print(f"{self.shape_name} drawing")


# tri=Triangle("triangle")
# tri.draw()


# rec=Rectangle("rectangle")
# rec.draw()



from abc import ABC,abstractmethod

class Bike(ABC):
    name:str
    model:str
    fuel_type:str

    def __init__(self,name,model,fuel_type) :
        self.name=name
        self.model=model
        self.fuel_type=fuel_type

    @abstractmethod
    def start(self):
        pass

class Duke(Bike):
    def __init__(self, name, model, fuel_type):
        super().__init__(name, model, fuel_type)

    def start(self):
        print(f"{self.name} starting with model {self.model} and fuel type {self.fuel_type}")

class Bullet(Bike):
    def __init__(self, name, model, fuel_type):
        super().__init__(name, model, fuel_type)

    def start(self):
        print(f"{self.name} starting with model {self.model} and fuel type {self.fuel_type}")

duk=Duke("duke 200","2021","petrol")
duk.start()


Bul=Bullet("Bullet 160","2020","petrol")
Bul.start()












