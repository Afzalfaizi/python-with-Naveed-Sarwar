# # For loop in python
# # What is for loop?
# # A for loop is a control flow structure that allows you to repeatedly execute a block of code
# # as long as an expression evaluates to True.
# # The syntax of the for loop consists of the keyword "for

# for index in range(0,11,1):
#     print("for loop",index)

# nums = [10,20,30,40,50,60,70,80]
# for index  in nums:
#     print("hello for loop", index)
    
# # table using for loop

# num = int(input("Enter Table Number"))
# for i in range(1,11):
#     print(num,"*", i, "=", num*i)

# write a search programe, search the name of noman if found than loop should be stop.
userNames = ["ali","hamza","mohsin","noman","nomi"]    
for i,searchedName in enumerate(userNames) :
    print("loop runing", searchedName,i)
    if searchedName == "noman":
        print("Name found", searchedName,i)
        break