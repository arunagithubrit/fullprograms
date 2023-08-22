class Mobile(object):
    name:str
    price:int
    display:str

    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.display=kwargs.get("display")

    def __str__(self):
        return self.name
    
    def get_price(self):
        return self.price
    
obj=Mobile(name="redmi note 8",price=24000,display="amoled")
print(obj)
print(obj.get_price())
print(obj.price)












