
## exercise 1
# my_dict = {'item1': 4, 'item3' : 5, 'item2' : 6}
# new_dict = {}
#
# x = {"item1":12, "item2":2}
# new_x = {k:v*2 for k,v in x.items()}

## Testing try execpt block

# while True:
#     try:
#         a = int(input("Give me one number:" ))
#         b = int(input("Give me another number:" ))
#         print(a/b)
#     except ValueError:
#         print( "That is not a number!" )
#     except ZeroDivisionError:
#         print( "Can't divide by 0!" )
#     except:
#         print( "something unexpected happened!" )

my_dict = {}
inventory = {'dagger': 0, 'bluepotion': 0, 'goldfeather': 0, 'manuscripts': 0}#

flying = 0
stealth = 0
print(inventory)
while True:
    # try:
    pickup = input("pick an item: ").lower()
# except ValueError:
#     print("no")

    usrInput = pickup.split(" ")

    for n in usrInput:
        if n in inventory and n == "dagger":
            inventory["dagger"] += 1
            print("added 1 dagger to inventory")
            print(inventory)

        elif n in inventory and n == "bluepotion":
            inventory["bluepotion"] += 1
            print("added 1 BluePotion to inventory")
            print(inventory)
            stealth += 1
            print("Stealth increased to", stealth)

        elif n in inventory and n == "goldfeather":
            inventory["goldfeather"] += 1
            flying += 1
            print("added 1 GoldFeather to inventory")
            print(inventory)
            print("Flying increased to", flying)

        elif n in inventory and n == "manuscripts":
            inventory["manuscripts"] += 1
            print("added 1 Manuscripts to inventory")
            print(inventory)
        else:
            print("item not available")
