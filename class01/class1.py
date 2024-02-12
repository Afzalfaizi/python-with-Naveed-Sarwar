print("Hello world")
userName = "Muhammad Afzal"
print(userName)

num1 = 2
num2 = 4
sum = num1 + num2 
subtract = num1  - num2
product = num1 * num2
division_remainder = num1 / num2
quotient = division_remainder // num2
modulo = num1 % num2

print("\nThe sum of", num1, "and", num2, "is: ", sum)
print("The difference between", num1," and", num2, "is: ", subtract)
print("The product of", num1, "and", num2, "is: ", product)
print("The quotient when dividing", num1, "by", num2, "is: ", quotient)
print("The remainder or modulus when dividing", num1, "by", num2, "is: ", modulo)

# Function in Python
def greetings():
    print("Welcome to the function. Let's have some fun.")

greetings()

# Return Function in python using variables

def greetings():
    return "Welcome to the function. Let's have some fun."

print(greetings())

# Function in Python with parameters

def addNumbers(a, b):
    return a+b

print(addNumbers(2, 4))

