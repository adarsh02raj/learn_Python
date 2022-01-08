# lists --------------------------------------------->>>>>>>>>

# ̥creaate a list using []


# a = [1,2,3,4,7,8]

# Print the list using print() function
# print(a)

# Access using index using a[0], a[1], a[2]........
# print(a[3])

# Change the value using Index
# a[0] = 98
# print(a)

# we can create a list items of different types
# c = [45, "Harry", False, 6.9]
# print(c)


# List slicing
# friends = ["Harry", "tom", "Rohan", "Divya", 45]
# print(friends[0:2])
# print(friends[-4:])

# l1 = [1,5,7,8,5,4,6,9]
# print(l1)
# l1.sort(); '''   sort in increasing order'''
# print(l1)
# l1.reverse();  '''sort the order in dicrease order'''
# print(l1)
# l1.append(45); '''Add in last of the list'''
# print(l1)
# l1.insert(3,544); '''Add at 544 index of 3 '''
# print(l1)
# l1.pop(2); '''Extract items on index 2'''
# print(l1)
# l1.remove(4); '''Remove 4 from the lists'''
# print(l1)
# 



# tupple ----------------------------------------->
# create a tuple using ()
# mytuple = (1, 2, 3, 6, 7, 4,8,9,8,8,8)
# print(mytuple[4])

# mytuple[0] = 34

# t = () --- empty tuple
# t = (1) --- throws error
# t = (1,) ---- right
# print(mytuple.count(8))
# print(mytuple.index(8))


# practice sets ------------------------------>>>>>>>>
# fruits = ["Apple", "Orange", "Grapes", "Guava", "Mango", "Litchi", "Watermelon"]
# print(fruits)
# q1
f1 = input("Enter Fruits Name: ")
f2 = input("Enter Fruits Name: ")
f3 = input("Enter Fruits Name: ")
f4 = input("Enter Fruits Name: ")
f5 = input("Enter Fruits Name: ")
f6 = input("Enter Fruits Name: ")
f7 = input("Enter Fruits Name: ")

myFruitList = [f1, f2, f3, f4, f5, f6, f7]
print(myFruitList)

# q2
m1 = int(input("Enter marks: "))
m2 = int(input("Enter marks: "))
m3 = int(input("Enter marks: "))
m4 = int(input("Enter marks: "))
m5 = int(input("Enter marks: "))
m6 = int(input("Enter marks: "))

marks = [m1, m2, m3, m4, m5, m6]
marks.sort()
print(marks)

# q3
tup = (1, 3, 5)
# tup[1] = 5
print(tup)

# q4
numb = [1, 8, 9, 6]
print(numb[0] + numb[1] + numb[2] + numb[3])

# q5
num = [0,1,0,2,8,6,0,7,5,0,0]
print(num.count(0))