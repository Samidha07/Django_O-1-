# Python has libraries or modules like headers in cpp
# Simple hello world to Start with
print("Hello world")

# Data types
# No concept of defining a datatype
data = 12
print(data)
print(type(data))

# reassigning is also easy however you have to be careful
data = "Samidha"
print(data)
print(type(data))

# No classification in int or float or string no matter size of value
data = 1000000000000000000000000000000.332
print(data)
print(type(data))

data = 1000000000000000000000000000000000
print(data)
print(type(data))

data = 'a'
print(data)
print(type(data))

# Single line comment
'''
"""
multi line comments
"""
'''

################################################################

# String manipulation
print(" ")
myString = '12345'
print(int(myString[0]))  # Typecasting used for int float str list etc

# Substring
# sub_myString = myString[start:end]
# Start is included in substring but end is excluded
sub_myString = myString[1:4]
print(sub_myString)
sub_myString = myString[1:]  # To go to end of the string
print(sub_myString)
sub_myString = myString[4:1:-1]  # reverse
print(sub_myString)
sub_myString = myString[::-1]  # reverse of complete string
print(sub_myString)

# Mutability of string
# String is not mutable i.e. Assignment operator doesn't work
name = "Aditya"
# name[1] = 'm'       # gives error
print(name)
# + for concatenation
name = name[0] + 'm' + name[2:]  # solution
print(name)
print(" ")

##############################################################

# Lists
# Array but powerful. Combination of many things.
# Dynamic resizing and datatype

lst = ['Aditya', 10, 10000020.30]  # Multi-datatype
# Functions of lists
# append (at end) and Insert (at start)
print(lst)
lst.append(3)
print(lst)
# lst.insert(index,value)
lst.insert(1, 'Sharma')
print(lst)
# Pop (to pop an element from the list)
value = lst.pop()
print(lst)
print(value)

# iterations
for i in lst:
    print(i)

n = 4
# for loop 1 parameter :-> end index
for i in range(n):
    print(i, " : ", lst[i])

# for loop 2 parameter :->  start,end
for i in range(1, n):
    print(i, " : ", lst[i])

# for loop 3 parameter :->  start,end,increment/decrement
for i in range(1, n, 2):
    print(i, " : ", lst[i])

# while loop
while n > 0:
    print(n)
    n -= 1

lm = [1, 2, 3, 4]
print(len(lm))  # length of list
print(sum(lm))  # Sum of list

# Tuple
# Non-dynamic unlike list
# only concatenation

tup1 = ('adi', 1, 23.4) + (23, 1, "sharma")
# tup1[0] = 'ask'     gives error -> append, pop and replacement is not allowed

print(tup1[0])
print(tup1)

# sets
# only unique values
# add instead of append
myset = set()
myset1 = {"Aditya", 1, 2, 3, 4}
myset1.add("Sharma")
print(myset1)
myset1.add("Aditya")
myset1.remove("Aditya")
print(myset1)
print(" ")

# Tuple is ordered, Set is not ordered hence index wise access is not allowed
# Hence for manipulation it should be typecast to list


# Dictionary
# Stores key value pairs
d = {}
d1 = {"Username": "Adi", "roll": 88, 23: 46}
print(d1[23])
print(" ")
# iteration
for k in d1.keys():  # Keys function returns single array with only keys
    print(d1[k])

for k, v in d1.items():  # items function returns map with key and values
    print(k, v)

for k in d1.keys():
    print(k, d1[k])

# if else
m = 0
if n > 1 and m < 0:
    print("in and")
elif n < 0 or m > 1:
    print("in or")
else:
    print("in else")

lst = [1, 2, 3, 4]
n = 7
if n not in lst:
    print("Number not found")
if n in lst:
    print("Number found")

# Input from User

n = int(input())
n = input()  # String by default

# Multiline input
a, b, c = map(int, input().split("-"))  # dash separated input is split
print(a, b, c)

lstinput = [int(x) for x in input().split()]
print(lstinput)


# functions
def func():
    return 0
