import myMathModule as myMath

print("-----------------------------------")
num = input("What number would you like to square? ")
print("The result is", myMath.customPow(int(num)))

print("-----------------------------------")

print("What numbers would you like to add?")
add_num1 = input("What is the first number? ")
add_num2 = input("What is the second number? ")
print("The result is", myMath.customAdd(int(add_num1), int(add_num2)))
