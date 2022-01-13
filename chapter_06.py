# chapter 06 >>>>>>>>>>>>>>>>>>>>>
# practice sets
# q1----------------------->>>>>
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
num3 = int(input("Enter first number: "))
num4 = int(input("Enter first number: "))
if(num1>num2 and num1>num3 and num1>num4):
    print(str(num1) + " is greater")
elif(num2>num1 and num2>num3 and num2>num4):
    print(str(num2) + " is greater")
elif(num3>num1 and num3>num2 and num3>num4):
    print(str(num3) + " is greater")
elif(num4>num1 and num4>num3 and num4>num2):
    print(str(num4) + " is greater")
    '''

# q2----------------->>>>>>>>
'''
phy = int(input("Enter physics number: "))
che = int(input("Enter chemestry number: "))
Mat = int(input("Enter math number: "))
obt = phy + che + Mat
per = (obt*100)/300
if(per>=40 and phy>=33 and che>=33 and Mat>=33):
    print("Pass")
else:
    print("Fail")
    '''
# q3--------------->>>>>>>>>>>>>>
'''
text = input("Enter comment: ")
if("make a lot of money" in text):
    print("Spam message.")
elif("buy now" in text):
    print("Spam message.")
elif("subscribe this" in text):
    print("Spam message.")
elif("click this" in text):
    print("Spam message.")
else:
    print("no spam message found")
    '''

# q4-------------------->>>>>>>>>>
'''
text = input("Enter sentence: ")
if(len(text)>=10):
    print("Character is more than 10.")
else:
    print("Character is less than 10.")
    '''

# q5---------------->>>>>>>>>>>>
'''
mylist = ["ram", "sita", "gita", "hari", "mango"]
words = input("Enter words to find: ")
if words in mylist:
    print("Match found")
else:
    print("match not found")
    '''

# q6------------------------>>>>>>>>>
'''
marks1 = int(input("Enter (phy)obtained marks: "))
marks2 = int(input("Enter (che)obtained marks: "))
marks3 = int(input("Enter (mat)obtained marks: "))
marks4 = int(input("Enter (hin)obtained marks: "))
marks5 = int(input("Enter (eng)obtained marks: "))
obt = marks5+marks1+marks2+marks3+marks4
per = (obt*100)/500
if(per<100 and per>90):
    print("Ex")
elif(per<90 and per>80):
    print("A")
elif(per>70 and per<80):
    print("B")
elif(per>60 and per<70):
    print("C")
elif(per<60):
    print("F")

    '''
# q7-------------->>>>>>>>>>>>>>>>>

