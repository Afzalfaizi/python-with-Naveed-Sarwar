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




# Methods of List in Python
# 1. append: It is used to add an element to the end of the list
# 2. pop: It is used to remove an element from the list. If we do not pass any index then it removes the last element.
# 3. pop: This method returns and removes the last element of a list
#         If you pass an integer argument to this method then it will remove that index element
# 4. insert : Inserts an element at the specified place in the list
#             We need two arguments for this method - first is the position where we want to put our element
#             And second one is the element which we want to put there.
# 5. remove : Removes the element with the specific value from the list.
# 