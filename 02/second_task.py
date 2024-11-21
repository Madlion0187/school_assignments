import math

def circ(r):
    return 2 * r * math.pi

def area(r):
    return math.pow(r, 2) * math.pi
    
user_choice = input("Enter a number: ")
r = int(user_choice)
    
print(round(circ(r), 2))
print(round(area(r), 2))

def max_value(arr):
    max_number = arr[0]
    
    for i in arr[1:]:
        if i > max_number:
            max_number = i
            
    return max_number

numbers = [22, 15, 32, 45, 12, 46, 87]

print(max_value(numbers))