fruits = ["peach", "grape", "banana", "apple", "mango"]
arranged_fruits = sorted(fruits)

print("----------------------------------")
print(fruits)
print("----------------------------------")     
print(arranged_fruits)
print("----------------------------------")

for i in fruits:
    print(i)
    
print("----------------------------------")
    
for i in arranged_fruits:
    print(i)
    
print("----------------------------------")
    
fruits.sort()
print(fruits)

print("----------------------------------")

for i in fruits:
    if i.startswith("a"):
        print("This fruit start with \"a\": " + i)