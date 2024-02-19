# python sets data structure, 
# Sets are unordered collections of unique elements. They are similar to lists,
# but unlike lists they do not keep track of element order and cannot contain duplicate values. 

studentsEmailSet = {"test1@gmail.com", "test2@gmail.com", "test3@gmail.com"}
print(studentsEmailSet)
studentsEmailSet.add("test4@gmail.com") # adding element in set
print(studentsEmailSet)
# studentsEmailSet.update("test1@gmail.com", "test5@gmail.com")  # updating the existing element with new one
# print(studentsEmailSet)
studentsEmailSet.remove("test2@gmail.com")    # removing an element from a set
print(studentsEmailSet)
