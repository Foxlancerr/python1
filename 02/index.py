'''
# write a simple ATM Transiction program

pin = 1234
i = 0
while(i < 3):
    if(int(input("Enter your pin:")) == pin):
        print("transection successful")
    else:
        print("Wrong Pin")
    i +=1
else:
    print("the card is blocked")
'''











# set in pyjon
# enclosed by curly brakets {}
# order will not maintain
# not duplicate is allowed

#s1 = {1,2,3,4,5,6}
#s2 = {5,2,1}
#print(s1.issubset(s2))
#print(s1.issuperset(s2))
#print(s1.intersection(s2))
#print(s1.union(s2)) # it will combines but not change the origianal set
#s1.update(s2) # it will change the original arrays and combines it

'''
s3 = {3,4,2,10}
s4 = s3 # it will reference that varaible in memory and problem occurs
# when we change s3 than automatically s4 will be changed

print("before")
print(s3)
print(s4)
s3.update({30,40,50})
print("after")
print(s3)
print(s4)

s3 = {3,4,2,10}
s4 = s3.copy() # it will make a shollow copy and resolve its issues
print("before")
print(s3)
print(s4)
s3.update({30,40,50})
print("after")
print(s3)
print(s4)
'''







# # tuple in python
# t1 = (4,3,2,45,3,2,1,56)
# print(t1)
# # t1[0] = 34 we can not minupulate the tuples

# # we want to reverse the order of tuple
# cvtList = list(t1) # convert anytype to list by used this method
# cvtList.reverse() # reverse the order
# cvtTuple = tuple(cvtList) # convert anytype to tuple by used this method
# print(cvtTuple)

# for t in t1:
#     print(t)








# for loop in python
# for i in range(10): # range(start,stop,step)
#     print("hello "+ str(i))
# for i in range(5,20): # range(start,stop,step)
#     print("hello "+ str(i))
# for i in range(5,20,2): # range(start,stop,step)
#     print("hello "+ str(i))

# names = ["A","B",["A","B"],"D"]
# for c in names:
#     print(c) 



