# The Cassini mission
# Version 3
# Daniel Hitchcock
# 25/01/2019
import time
import random
Gameover = False
inv = ["key card", "laser cutter", "welding tool", "wrench", "blowtorch", "gps"]
global hoursLeft
hoursLeft = 5

def intro():
    print("*recording started*")
    time.sleep(2)
    print("Hello..")
    time.sleep(2)
    print("is this thing on?")
    time.sleep(2)
    print("to whomever receives this message please listen carefully.")
    time.sleep(2)
    print("STAY")
    time.sleep(1)
    print("AWAY")
    time.sleep(1)
    print("FROM")
    time.sleep(1)
    print("TITAN")
    print()
    time.sleep(2)
    print("My name is ")


def intro2():
    print("I am a Pilot Engineer aboard the Saturn Orbiter..")
    time.sleep(2)
    print("and last survivor of the Cassini mission")
    time.sleep(3)
    print("today is monday, the date is the 16th of may 2029")
    time.sleep(3)
    print("2 weeks ago we successfully landed on Titan..")
    time.sleep(3)
    print("4 days ago a lethal virus infected our Commander Apollo")
    print("We tried to contain him as fast as possible but this virus..")
    time.sleep(4)
    print("it changes people")
    time.sleep(2)
    print("the virus eventually infected our entire crew..")
    time.sleep(5)
    print()
    print("Including me..")
    time.sleep(3)
    print()
    print ("*one week earlier*")


def part1():
    time.sleep(2)
    print()
    print("Leo: Hey " + name)
    time.sleep(1)
    print(" Get over here and give me a hand")
    print()
    chooseHelp()
    print()
    print("Leo: Thanks for helping")
    time.sleep(2)
    print(" once we get this rover up and running we can explore the surface")
    time.sleep(2)
    print(" I just need your wrench and it should be done")
    time.sleep(2)
    print()
    print ("Inventory:")
    print (inv)
    inv1()
    print()
    print("Leo : Okay looks like every things in order")
    time.sleep(2)
    print(" Apollo the rover is ready")
    time.sleep(1)
    print(" Let the exhibition begin!")
    time.sleep(1)
    print()
    print("Apollo: Okay good, lets get this mission started, we're losing daylight")
    time.sleep(2)
    print( name + " get in, you'll be driving")

def inv1():
    item = ""
    while item not in inv:
        item = input("Choose an Item: ").lower()
    if item != "wrench":
        print()
        print("Leo: Thats not a wrench")
        print()
        inv1()
    elif item == "wrench":
        print()
        print("*Wrench removed from inventory*")
        inv.remove("wrench")
        print(inv)
        return item


def chooseHelp():
    helpLeo = ""
    while helpLeo != "yes" and helpLeo != "no":
        helpLeo = input ("Help Leo? [Yes] or [No]: ").lower()
    if helpLeo == "no":
        print()
        print("Apollo: " + name.upper())
        time.sleep(1)
        print(" stop slacking around")
        print(" if we want this mission to be a success we must help and work together!")
        time.sleep(4)
        print(" Now go help Leo")
        time.sleep(3)
        print()
        print("Pandora: Dont take it personally " + name)
        time.sleep(2)
        print(" Apollo's on edge recently, who could blame him")
        time.sleep(2)
        print(" This research could save our world")
        time.sleep(3)
        print(" or potenially create a new one")
        time.sleep(3)
    elif helpLeo == "yes":
        return helpLeo

def rover1():
    print()
    time.sleep(1)
    print("*40 minutes into exhibition*")
    time.sleep(1)
    print()
    print("Leo: Woah! Slow down here " + name)
    time.sleep(2)
    print(" Looks like there's a crater up ahead")
    print()
    time.sleep(2)
    print("Pandora: Oh my god")
    time.sleep(2)
    print(" that has to be at least 300 miles wide")
    time.sleep(2)
    print(" What do we do Commander?")
    print()
    time.sleep(2)
    print("Apollo: The co-ordinates are on the other side")
    time.sleep(2)
    print(" We have to go around")
    time.sleep(1)
    print( name + " Choose a path and lets get a move on")
    time.sleep(2)
    print(" We only have 5 hours of daylight left..")
    time.sleep(2)
    print(" we will all freeze to death at night")
    time.sleep(2)
    print()
    print("Hours Left [", hoursLeft, "]")
    print()
    choice = choosePath()
    checkPath(choice)
    print("Hours Left [", hoursLeft, "]")
    time.sleep(2)

def rover2():
    print("Leo: Okay can't see anything ahead.")
    time.sleep(2)
    print(" I think we're clear")
    print()
    time.sleep(1)
    print("*Engine starts struggling*")
    print()
    time.sleep(2)
    print("Pandora: What's that noise?")
    time.sleep(1)
    print(" Wait..")
    time.sleep(1)
    print(" Are we sinking!?")
    print()
    time.sleep(2)
    print("Apollo: Okay no body panic")
    time.sleep(2)
    print(" Looks like we drove onto some quick sand")
    time.sleep(2)
    print()
    print("Leo: Well we better act fast or we'll drown")
    time.sleep(2)
    print(" We need to rev the engine")
    time.sleep(2)
    print(" If we build enough speed we can drive out")
    print()
    time.sleep(2)
    print("Pandora: Did they teach you anything?")
    time.sleep(2)
    print(" Moving is the last option, creating more movement will make us sink faster")
    time.sleep(4)
    print(" We need to get out and pull, its our only option")
    time.sleep(3)
    print()
    print("Leo: That will take too long, we're running out of time")
    time.sleep(2)
    print(" I built the thing, you think I don't know what im talking about?")
    print()
    time.sleep(3)
    print("Pandora: Evidently not!")
    time.sleep(1)
    print()
    print("Apollo: ENOUGH!")
    time.sleep(2)
    print(name,", how do we get out this?")
    time.sleep(2)
    print()





def choosePath():
    path = ""
    while path != "left" and path != "right":
        path = input("Choose a Path [Left] or [Right]: ").lower()
    return path

def checkPath(chosenPath):
    print()
    print("Pandora: I hope this is the right way " + name)
    time.sleep(2)
    print()
    print("Leo: Hold on guys I think I see something..")
    time.sleep(2)
    print()
    paths = ["left", "right"]
    correctPath = random.choice(paths)
    global hoursLeft
    if chosenPath == correctPath:
        hoursLeft -= 1
        print("Leo: Oh never mind, I think it's just a rock formation")
        time.sleep(2)
        print()
        print("Pandora: Good choice " + name)
        time.sleep(1)
        print(" I think I see a storm forming on the other side")
        print()
        time.sleep(2)
        print("Apollo: Yes. Well done..")
        time.sleep(1)
        print(" Lets keep going")
        time.sleep(2)
        print()
    else:
        hoursLeft -= 2
        print("Leo: Is that a..?")
        print()
        time.sleep(1)
        print("Pandora: THAT'S AN ELECTRICAL STORM!")
        print()
        time.sleep(2)
        print("Leo: The readings are off the charts, its scrambling our equipment!")
        time.sleep(2)
        print(" If we sit here for too long the storm will eat us alive!")
        time.sleep(2)
        print(" We have to power through it!")
        time.sleep(2)
        print()
        print("Apollo: BRACE FOR IMPACT!")
        time.sleep(3)
        print()
        randomItem = random.randint(1, 2)
        if randomItem == 1:
            inv.remove("laser cutter")
            print("*Laser Cutter removed from inventory*")
            print(inv)
            print()
        else:
            inv.remove("gps")
            print("*GPS removed from inventory*")
            print(inv)
            print()
        time.sleep(2)
        print("Leo: Is everyone okay?")
        time.sleep(1)
        print(" Damn it! The storm scrambled some of our equipment")
        print()
        time.sleep(2)
        print("Apollo: It also slowed us down")
        time.sleep(2)
        print(" We only have a few hours left, lets speed this up")
        print()


#intro()

#name = input("What is your name?: ").lower()
name = "Daniel"

#intro2()
#part1()
rover1()

