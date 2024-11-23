class Car:
    
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        
    def _internal_method(self):
        return f"{self._brand}-------{self._model}"
    
    @property
    def brand(self):
        return self._brand
    @property
    def model(self):
        return self._model
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand
    @model.setter  
    def model(self, new_model):
        self._model = new_model
        
        
car1 = Car("Toyota", "Yaris")

print(car1.brand, car1.model)
print(car1._internal_method())