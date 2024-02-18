# Tuple in python.
# how to use tuple in python
#  tuple is a collection of objects which are ordered and unchangeable. 

def print_tuple(t):
    """print elements of the given tuple"""
    for i in t:
        print(i)
        
my_tuple = (1, 'a', True, 3.4)   # creating a tuple with different data types

print("Elements of my_tuple : ")
print_tuple(my_tuple)               # calling function to print all elements of the tuple

print("\nType of my_tuple : ", type(my_tuple))     # checking the datatype of the tuple