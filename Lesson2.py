#game_over = false

#while not game_on:
    #..
    #...
    #..
    #..
    #game_over = True

#game_over = true

#while game_on:
    #..
    #...
    #..
    #..
    #game_over = false
##########
#count = 0

#while count <5:
    #print(count)
    #count += 1

#else: print("oh hello")
#############
#for python in range(0,10):
    #print(python)
############
#count = 0
#while count < 3:
    #print(count)

    #count += 1

    #if count == 2:
    #    print ("python")
        # break
    #else:
    #    continue

    #print("End")
###################
#word = 'python'
#for letter in word:
    #if letter == 't':
    #    continue
    #print (i, end = "")
    ###########################
#name = "v"
#myList = ["green", "red", "blue"]

#numericalList = [3,4,5]
#listofStrings = ["name", "age"]
#mixedList = [3,4, "apple"]
#nestedList = [3,4, [5,6,6]]

#x = "dagger"
#x = "gold"

##list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right
##list.extend(another_list) -- adds the elements of another_list to the end of the list
##list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element doesnt apear (use "in" to check without valueerror, eg if elem in list: print(;ist.index(elem))
##list.reverse() -- reverses the list in place (does not return it!)
##list..pop(index) -- removes and returns the element at the given index. Returns the rightmost element is omitted

###example of a list
#myList = ["apple", "pear", "orange"]
#print (myList)
###adds to list
#myList.append("grapes")
###change item
#myList[1] = "Lemon"
#print (myList)
list = ["xxx", "aaa", "r5t6yy", "g", "wow"]
#for every word in list that is more or equal to 2 and the first and last letter are the same
for l in list:
    if len(l) >= 2 and l[0] == l[-1]:
        print (l)

myList = ["*",
"**",
"***",
"****",
"*****",
"******",
"*******"]
for i in myList:
    print (i)
