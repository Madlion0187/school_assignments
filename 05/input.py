user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

#user_name_back = ""

""" for i in user_name:
    user_name_reverse = i + user_name_reverse """
    
user_name_back = user_name[::-1]
    
print(f"Your name backward: {user_name_back}")

if user_age < 30:
    print("You are young")
elif user_age >= 30 and user_age <= 50:
    print("You are adult")
else:
    print("You are old")