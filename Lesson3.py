#x = ['mix', 'xyz', 'apple', 'xanadu', 'rovio']

#new_list_a = [] #contain the words beginning with x
#new_list_b = []# contain the rest

#for word in x:
    #if word[0] =="x":
        #new_list_a.append(word)
    #else:
        #new_list_b.append(word)

#print( sorted(new_list_a) + sorted(new_list_b) )

# #the list of numbers
# numbers = [2, 3, 5, 7, 66, 89, 134]
# #user input
# usrinput = int( input("Give me a number: ") )
# #for every number, if the number is greater than the input, append
# for x in numbers:
#     if x <= usrinput:
#         newList.append(x)
#
# print(newList)

#
# inventory = ["gun", "bat"]
#
# gameOver = False
#
# while not gameOver:
#
#
#
#
#     print (inventory)
#     userinput = input("A zombie jumps out in front of you. Do you want to fight?: ").lower()
#
#     if userinput in ["Yes", "y", "okay", "ok", "sure", "why not"]:
#         f = input("The zombie starts running towards you FAST. Quick, what weapon do you use?: ").lower()
#         if f in inventory:
#             print(" %s is a good choice" % f)
#         else:
#             print("You dont have this weapon")


### multiple choice
# l = ["sword", "dagger", "shield"]
#
# while True:
#
#     print (l)
#
#     usr = input("you can choose 2 items, which ones?: ")
#
#
#
#     usrp = usr.split(" ") #list
#
#     for word in usrp:
#         if word in l and word == "sword":
#             print("you choose sword")
#         elif word in l and word == "dagger":
#             print("you choose dagger")
#         elif word in l and word == "shield":
#             print("you choose shield")
#         else:
#             print("you do not have this")
### List comprehension

# a = []
# for i in range (5):
#     a.append(ixx2)
#
# print a

### Tuples
# an_empty_tuple = ()
# string_tuple = ("Lola", "stitch")
# number_tuple = (2,3)
# randomtuple = (2, "strawberries", "56")
# lists = []
# tupleList= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#
# t1 = []
#
# for i in tupleList:
#      if i:
#          t1.append(i)
# print (t1)

###' Dictionaries

dict = {}
dict = {'name': 'rex', 'age' : 7, 'pedigree' : 'rotweiler'}
print(dict['name'])  #rex

dict["height"] = 12

# my_dict.keys() #returns the list of keys
# my_dict.values() #returns the list of values
# my_dict.items() # returns the list of (key,value) pairs
