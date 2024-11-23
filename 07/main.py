from food import Food
from restaurant import Restaurant

food1 = Food(1, "Pizza", 25)
food2 = Food(2, "Hamburger", 18)
food3 = Food(3, "Hot-dog", 14)

restaurant = Restaurant("Brooklyn", [food1, food2])

""" print(restaurant)
restaurant.getmenuItems() """

restaurant + food3

print("Adding a new dish to the menu.")

while True:
    try:
        food_id = len(restaurant) + 1
        food_name = input("Enter the name of the dish: ")
        food_price = int(input("Enter the price of the dish: "))
        
        if food_price <= 0 or food_price >= 10000:
            raise ValueError("The price of the dish must be between 0 and 1000")
        
        food = Food(food_id, food_name, food_price)
        restaurant + food
        break
    
    except ValueError as e:
        print(e)



print(restaurant)
restaurant.getmenuItems()