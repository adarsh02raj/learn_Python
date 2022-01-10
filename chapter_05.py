# # Distonary and sets

# myDict = {
#     "Fast" : "In a quick manner",
#     "Harry" : "A coder",
#     "Marks" : [1, 2, 5],
#     "anotherdict" : {'harry': 'player'}
# }

# print(myDict['Fast'])
# print(myDict['Harry'])
# myDict['Marks'] = [45, 58, 60]
# myDict['Marks'] = [45, 58]
# print(myDict['Marks'])
# print(myDict['anotherdict']['harry'])


# # dictionary methods

# print(myDict.keys())
# print(list(myDict.keys())); '''typecasting into list'''
# print(myDict.values())

# # items method
# print(myDict.items())
# print(myDict)
# updateDist = {
#     "lovish": "friend",
#     "harry": "Rohan"
# }



# myDict.update(updateDist)
# print(myDict)
# print(myDict.get("Harry"))
# print(myDict['Harry'])



# # sets --------------------------------------------------->>>>>>>>>>>>>>>

# a = {1, 3, 5, 1, 4}
# print(type(a))
# print(a)

# a = { }
# print(type(a))



# b = set()
# print(type(b))


# b.add(4)
# b.add(5)
# b.add(4)
# b.add(4)
# b.add(4)
# b.add(4)
# b.add(545)
# b.add("H")
# b.add((1, 4, 6))
# print(b)


# # length of the sets
# print(len(b))

# # removel an item in sets

# b.remove(5)
# print(b)

# print(b.pop())
# print(b)

# b.clear()
# print(b)


# # practice sets ------------------->

# # q1>>>>>>>>>>
# mydict = {
    # "Aam" : "Mango",
    # "Papita": "Papya"
# }
# print("Options are", mydict.keys())
# a = input("Enter the hindi word: ")
# print("English meaning of the word is: ", mydict[a])
# print("English Mean of the word: ", mydict.get(a))

# q2>>>>>>>>>>>
# sets = set()
# sets.add(int(input("Enter number: ")))
# sets.add(int(input("Enter number: ")))
# sets.add(int(input("Enter number: ")))
# sets.add(int(input("Enter number: ")))
# sets.add(int(input("Enter number: ")))
# sets.add(int(input("Enter number: ")))
# sets.add(int(input("Enter number: ")))
# sets.add(int(input("Enter number: ")))
# print(sets)

# q3>>>>>>>>>>>
# s1= {18, "18"}
# print(s1)

# q4>>>>>>>>>>>>>>>>>>>>

# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))

# q5>>>>>>>>>>>>>>>>>>>>>>>>
# mydict = {
    # "shubham": "" ,
    # "Rakesh2": "", 
    # "Neeraj": "",
    # "Rohan": ""
# }
# f1 = input("Enter favourite language: ")
# f2 = input("Enter favourite language: ")
# f3 = input("Enter favourite language: ")
# f4 = input("Enter favourite language: ")
# upmy = {
#  "shubham": f1,
# "Rakesh": f2,
# "Neeraj": f3,
# "Rohan": f4
# }
# mydict.update(upmy)
# print(mydict)

favlang = {}
f1 = input("Enter favourite language: ")
f2 = input("Enter favourite language: ")
f3 = input("Enter favourite language: ")
f4 = input("Enter favourite language: ")
favlang['Rohan'] = f1
favlang['roshan'] = f2
favlang['ankit'] = f3
favlang['rohit'] = f4
print(favlang)


# q7>>>>>>>>>>>>>>>
