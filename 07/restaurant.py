class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
    
    def __str__(self):
        return f"{self.name} restaurant"
    
    def __add__(self, menu_item):
        self.menu.append(menu_item)
        
    def __len__(self):
        return len(self.menu)
        
    def getmenuItems(self):
        for food in self.menu:
            print(f"{food.id}.{food.name}------------{food.price}$")

          