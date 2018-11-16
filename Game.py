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

a = []
for i in range (5):
    a.append(ixx2)

print a
