"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the list [1, 2, 3, 4, 5]

y = [i for i in range(1, 6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [i ** 3 for i in range(0, 10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["ava", "eon", "aza"]

y = [string.upper() for string in a]

print(y)

# Example I modified from Stack Overflow in order to understand
# how to make inputs append to a list.

shopList = [] 
maxLengthList = 6
while len(shopList) < maxLengthList:
    item = input("Enter your Item to the List: ")
    if item == "exit":
        break
    else:
        shopList.append(item)
        print(shopList)
print("That's your Shopping List")
print(shopList)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [int(input_) for input_ in x]

# Breaking down the logic for the second list comprehension used below.
# for index ,integer in enumerate(y):
#     if (integer % 2) != 0:
#         y.pop(index)

y = [integer for integer in y if (integer % 2) == 0]



print(y)
print(len(y))