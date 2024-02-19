# Tuple in python.
# how to use tuple in python
#  tuple is a collection of objects which are ordered and unchangeable. 
names = ("ali", "rehan", "sara", "zain", "moin", "umar")
print(names[2])
for item in names:
    print(f" hello {item} welcome to the world of coding")

# write a programme that checks duplicate  element in list
nums = [10,20,30,40,50,20,10]

for num in nums:
    if nums.count(num) > 1:
        print(f"{num} is repeated")
    else:
        print(f"{num} is unique")