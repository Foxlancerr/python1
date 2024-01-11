# loops in python
str = [0,1,2,3,4]
i = 0
while(i < len(str)):
    print(i)












# conditional statement
'''age = 34
if age > 50:
    print("the AGE is greater than 50")
else:
    print("the age is less than 50")


country = input("Enter your country:")
if (country == "pak"):
    age = int(input("Enter your age:"))
    if(age >= 18):
        print("You are eligible for voting")
    else:
        print("you are kids and not eligible for voting")
else:
    print("you are not belong to pak, so you not cast vote")

'''










'''
# Assigment operators and arthematics operator
x = 4
y = 6


print(x+y)
print(x-y)
print(x%y)
print(y % x)
print(x*y)
print(x/y)



x += 4
print(x)

x %= 1
print(x)

x -= 4
print(x)

print(x + y - x * x / x +(2+2))
'''







'''
# Find the area of circle?
# formula pi * r ** 2

pi = 3.14
r = float(input("Enter your radius:"))
# print("The area of a circle: ", pi * r * r)
print("The area of a circle: ", pi * r ** 2)
'''









'''
# list in pythons
# In here we can store hetrogenus data and represented by square brakets
marks = [3,4,25,234,23,1,5]
print(marks)

mixedData = [0,"hi",False]
print(mixedData)

# access list data
print(marks[0]) # first Index
print(marks[-1]) # last Index
print(marks[3:5]) # 3 upto 5 index
print(marks[3:]) # 3 upto onward index
print(marks[:3]) # 0 upto 3 index'''








# (#)this symbols is used for Single Line Comments 
'''
this is multiple line comments
and we used the string quotes single or double quotes (""")
'''







'''# all stuff related to print

# end arguments in print
print("A",end="\n\n\n")
print("A",end="--------")

# sep arguments in print
print("A")
print("A","B","C","D", sep= " | ")'''










#import keyword,math
#print(keyword,math)
#print(len(keyword.kwlist))
#print('the power of 2 to 3 is ', math.floor(math.pow(3,3)))




'''num1 = input("Enter a num1:")
num2 = input("Enter a num2:")
print(num1 + num2)
print(type(num1))
numInt1 = int(num1)
numInt2 = int(num2)
print(numInt1 + numInt2)
print(type(numInt1))'''










'''
# simple class example in python
class parent():
    age = 40
    name = "kamran"
    def greet(self):
        print("hello Dear Mr.",self.name)
    
class child(parent): # we can inherit the parent properties to its child
    pass # used when there is no el, or code present in class  (empty class)

child1 = child() # this will called the constructer
child1.greet() # calling the greet method which is present in parent class
'''







# dictionary in python
# obj1 ={
#     "name":"kamran",
#     "age":40,
#     "city":"peshawar"
# }

# print(obj1)
# print(obj1.keys())
# print(obj1.values())

# for i in obj1:
#     print(i,":",obj1[i])

# obj2 = dict(name = "sadiq",age=45)
# obj2 = obj1.copy()
# obj1.update({"zipCode":20000})
# print(obj2)





'''
# function in python
# def kewyord is used to define the function

def greet(): # function defination
    print("Good Morning")

greet() # function calling
greet()

# addition of two numbers
def add(x,y):
    print("Addition:", x+y)

add(3,5)


def add(x,y,z=0): # if no value in z it will take 0 by default
    print("Addition:", x+y+z)
    print("x",x)

add(y=34,x=5)

# if the user send more than 20 arguments how we can handle, for this
# we used * before the argument recieved and it will recieve that in form
# of tuple

def marks(*m):
    print(m) # so here we cannot not minupulate this so we can convert this
    # into list and then we apply the methods to changes its data

    l = list(m) # convert into list
    sum = 0
    for i in m:
        sum += i 
    print(sum) 
marks(1,2)
marks(1,2,3,4,5,56,3,24)
marks(1,2)
'''






