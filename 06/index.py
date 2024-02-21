# String in python

# single line output
print('hello world')
print("Hello world")

# multi line output

print("""
      pakistan 
      zindaabad
      """)

# single line comments
# symbols is used to single line comments

"""
multiline comments
multiline comments
multiline comments
multiline comments
"""

name = "kamran"
age = 45
city = "peshawar"

# way1
# f string which work as template letrals and dynamically concatenate the values
card1 = f"name:{name} age:{age} city:{city}"
print(card1)

# way2
# f string which work as template letrals and dynamically concatenate the values
card2 = "name:{} age:{} city:{}".format(name,age,city)
print(card2)
card2 = "name:{2} age:{1} city:{0}".format(city,age,name)
print(card2)

# way3
card3 = "name " + name + " age " + str(age) + " city " + city
print(card3)

