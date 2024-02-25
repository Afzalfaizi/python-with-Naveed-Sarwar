# print("Hello world")
# userName = "Muhammad Afzal"
# print(userName)

# num1 = 2
# num2 = 4
# sum = num1 + num2 
# subtract = num1  - num2
# product = num1 * num2
# division_remainder = num1 / num2
# quotient = division_remainder // num2
# modulo = num1 % num2

# print("\nThe sum of", num1, "and", num2, "is: ", sum)
# print("The difference between", num1," and", num2, "is: ", subtract)
# print("The product of", num1, "and", num2, "is: ", product)
# print("The quotient when dividing", num1, "by", num2, "is: ", quotient)
# print("The remainder or modulus when dividing", num1, "by", num2, "is: ", modulo)

# # Function in Python
# def greetings():
#     print("Welcome to the function. Let's have some fun.")

# greetings()

# # Return Function in python using variables

# def greetings():
#     return "Welcome to the function. Let's have some fun."

# print(greetings())

# # Function in Python with parameters

# def addNumbers(a, b):
#     return a+b

# print(addNumbers(2, 4))

# # if condition in python - with Naveed sarwar

# myName = "Muhammad Afzal"
# if  "Afzal" in myName:
#    print("Hello Muhammad Afzal")
# else:
#    print("I don't know you!")
   
#    # create a login  system for user
# userName = input("Enter your username : ")
# password = input("Enter your password : ")

# if userName == "Muhammad Afzal" and password == "1122334455":
#     print("Login successful")
# elif userName == "guest" and password == "admin":
#     print("welcome to  guest account")
# else:
#     print("Invalid Username or Password")
    
#  # if condition in python - with Naveed sarwar
 
# number = int(input("Enter Number"))
# num5 = number % 2 == 0
# if num5 :
#     print(number, "is even")
# else :
#     print(number, "is odd")
    
# # write a programe that takes 3 numbers as an input from the user and find the largest number

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# num3 = int(input("Enter the third number : "))

# if num1 > num2 and num1 > num3:
#     print(num1, "is the largest number")
# elif num2 > num1 and num2 > num3:
#     print(num2, "is the largest number")
# else:
#     print(num3, "is the largest number")
    
# # Match case condition in python
# n = int(input("Enter Day number"))
# match n:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day")
        
# List in python
# List is a collection of items that are ordered and changeable. They can contain elements of different data types.
studentNames = ["Afzal", "Noman", "Zeeshan", "Shahid","Imran"]
print(studentNames[2])

# To add one more item in List we can use append method (built in method in python) to save an item at the last of list
studentNames.append("Rizwan")   # Add element to list
print(studentNames)              # Print whole list 
studentNames.pop()
print(studentNames)
studentNames.insert(1, "Asif")    # Insert element at specific position
print(studentNames)

# To remove an item from list we can use remove method or del keyword
studentNames.remove("Imran")      # Using remove method
print(studentNames)               # After using remove method
