class Car:
    
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        
    def _internal_method(self):
        return f"{self._brand}-------{self._model}"
    
    def get_brand(self):
        return self._brand
    
    def get_model(self):
        return self._model
    
    def set_brand(self, new_brand):
        self._brand = new_brand
        
    def set_model(self, new_model):
        self._model = new_model
        
    car_brand = property(get_brand, set_brand)
    car_model = property(get_model, set_model)
        
car1 = Car("Toyota", "Yaris")

print(car1.car_brand, car1.car_model)
print(car1._internal_method())
    

    
    
        