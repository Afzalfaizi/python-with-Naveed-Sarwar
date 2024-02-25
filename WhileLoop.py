# # While Loop in Python
# # while loop is used to execute a block of code as long as the condition remains true.
# # It can be thought of as a repeating if statement. The syntax for using the while loop is:

# i = 1

# while i <= 10 :
#     print("hello world")
#     i += 1

# # write a table of 5 using while loop
# i = 1
# while i <= 10 :
#     print("5 *", i, "=" , 5*i)
#     i += 1

# table from user input
num = int(input("Enter Table Number"))
i = 1
while i <= 10 :
    print(num,"*", i, "=" , num*i)
    i += 1