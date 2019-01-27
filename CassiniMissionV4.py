# The Cassini mission
# Version 4
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
    hoursLeft = 5
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
    chooseQuicksand()
    print()
    time.sleep(2)
    print("Apollo: If everyone is ready lets continue")
    time.sleep(2)
    print("Hours Left [", hoursLeft, "]")
    timeCheck()

def rover3():
    print()
    time.sleep(2)
    print("*Leo Shivers*")
    time.sleep(1)
    print("Leo: When did it get so co-cold?")
    print()
    time.sleep(2)
    print("Pandora: Titan has a few glaciers left that create their own climate")
    time.sleep(2)
    print(" Imagine global warming on steroids")
    time.sleep(2)
    print()
    print("Apollo: Frozen lake up ahead!")
    print()
    time.sleep(2)
    print("Leo: Brilliant, we'll never make it in time")
    time.sleep(2)
    print()
    print("Pandora: Wait,", name, "do you still have your GPS?")
    time.sleep(2)
    print(" We can check how long it will take us to reach the signal")
    print()
    time.sleep(2)
    print(inv)
    print()
    time.sleep(1)
    if "gps" in inv:
        print("[TIME TO CROSS: 1 HOUR]")
        time.sleep(1)
        print("[TIME TO GO AROUND: 2 HOURS]")
        time.sleep(4)
    else:
        print("Leo: Damn it, the storm scrambled mine too")
    print()
    time.sleep(2)
    print("Pandora: I think we should go around")
    time.sleep(2)
    print(" Looking at how thin the ice is, i'd say we have a 33% chance of making it")
    print()
    time.sleep(3)
    print("Apollo: We have to take the chance")
    time.sleep(2)
    print(" We cant afford to waste any more time")
    time.sleep(2)
    print(" If we stay out here by nightfall we'll freeze either way")
    time.sleep(2)
    print()
    print("Leo: Are you crazy!? We will die! We're going around!")
    time.sleep(2)
    print()
    print("Pandora: The odds are in our favour, but i'd rather not test my luck Sir")
    print()
    time.sleep(2)
    print("Apollo: We'll leave it up to " + name)
    time.sleep(2)
    print(" What should we do?")
    print()
    choice2 = choosePath2()
    checkPath2(choice2)
    timeCheck()



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
        randomItem = random.randint(1, 2, 3)
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


def chooseQuicksand():
    quickSand = ""
    global hoursLeft
    while quickSand != "rev" and quickSand != "pull":
        quickSand = input("Choose a Way out [Rev] or [Pull]").lower()
    if quickSand == "rev":
        hoursLeft -= 1
        print()
        print("Apollo: Are you sure?")
        time.sleep(2)
        print(" I hope you know what you're doing")
        print()
        time.sleep(2)
        print("Leo: Hit the gas", name, "!")
        print()
        time.sleep(2)
        print("*Engine starts revving*")
        print()
        time.sleep(2)
        print("Leo: Come on!")
        time.sleep(1)
        print(" I know you can do it baby!")
        time.sleep(2)
        print()
        print("Apollo: I think its working!")
        print()
        time.sleep(2)
        print("*The Rover bursts out of the sand*")
        print()
        time.sleep(2)
        print("Leo: HAHA! I told you it would work!")
        print()
        time.sleep(2)
        print("*Engine breaks down*")
        time.sleep(2)
        print()
        print("Pandora: You were saying?")
        print()
        time.sleep(2)
        print("Apollo:..")
        time.sleep(2)
        print(" Leo how long will this take to fix?")
        time.sleep(2)
        print()
        print("Leo: Depends, with a Laser Cutter it could be a few minutes")
        time.sleep(2)
        print(" With a welder I could fix it within the hour")
        time.sleep(2)
        print(name + " what have you got?")
        print()
        time.sleep(1)
        chooseEngine()
        print()
        time.sleep(2)
        print(inv)


    else:
        hoursLeft -= 2
        print()
        print("Apollo: Are you sure about this?")
        time.sleep(2)
        print(" This will take too long")
        print()
        time.sleep(2)
        print("Pandora: It is the safest option!")
        time.sleep(2)
        print(" Don't listen to them", name, ", this was the smart choice")
        time.sleep(2)
        print()
        print("Apollo: Okay everyone start pulling on the count of 3")
        time.sleep(2)
        print(" 1")
        time.sleep(1)
        print(" 2")
        time.sleep(1)
        print(" 3")
        time.sleep(1)
        print(" PULL!")
        print()
        time.sleep(1)
        print("*Rover slowly emerges out of sand*")
        print()
        time.sleep(2)
        print("Apollo: Almost there! PULL!")
        time.sleep(2)
        print()
        print("*Rover edges onto dry land to safety*")
        print()
        time.sleep(2)
        print("Pandora: Good work guys, I told you this would work")
        print()
        time.sleep(2)
        print("Leo: At what cost? We only have", hoursLeft, "hours left")
        print()
        time.sleep(2)
        print("Apollo: Then stop talking and lets get a move on")
        time.sleep(2)
        print()
        print("Leo: Sorry Sir! Yes Sir!")

def chooseEngine():
    engine = ""
    global hoursLeft
    while engine != "laser cutter" and engine != "welding tool":
        engine = input("Choose a Tool [Laser Cutter] or [Welding Tool]: ").lower()
    if engine == "laser cutter":
        if engine in inv:
            print("Leo: Thank god, that's going to save a lot of time")
            print()
            time.sleep(2)
            inv.remove("laser cutter")
            print("*Laser Cutter removed from Inventory*")
            return engine
        else:
            print("You don't have that tool")
            chooseEngine()
    elif engine == "welding tool":
        hoursLeft -= 1
        print("Leo: Okay that will do, give me an hour")
        print()
        time.sleep(2)
        inv.remove("welding tool")
        print("*Welding Tool removed from Inventory*")
        return engine

def choosePath2():
    path2 = ""
    while path2 != "cross" and path2 != "go around":
        path2 = input("Choose a Path [Cross] or [Go Around]: ").lower()
    return path2

def checkPath2(chosenPath2):
    global hoursLeft
    if chosenPath2 == "cross":
        print()
        print("Apollo: It's settled, start driving " + name)
        print()
        time.sleep(2)
        print("*Ice starts cracking behind*")
        time.sleep(2)
        print()
        print("Pandora: SIR! THE ICE IS STARTING TO CRACK!")
        print()
        time.sleep(2)
        print("Leo: FLOOR IT", name.upper(), "!")
        print()
        time.sleep(1)
        print("Pandora: ITS CATCHING UP TO US!")
        print()
        time.sleep(1)
        print("Apollo: JUST A LITTLE FURTHER AND WE CAN MAKE IT")
        print()
        time.sleep(2)
        chance = (1,2,3)
        randomIce = random.choice(chance)
        if randomIce == 1:
            print("Pandora: KEEP GO-")
            print()
            time.sleep(1)
            print("*You fell through the ice*")
            print()
            playAgain = ""
            while playAgain != "yes" and playAgain != "y":
                playAgain = input("Do you want to play again? [Yes] or [Y] to continue playing: ").lower()
            if playAgain == "yes" or "y":
                print()
                print("*Starting from checkpoint*")
                choosePath2()
            else:
                return
        else:
            hoursLeft -= 1
            print("Pandora: KEEP GOING!")
            print()
            time.sleep(2)
            print("*Rover drifts onto land*")
            print()
            time.sleep(2)
            print("Pandora: Phew, that was a close one")
            time.sleep(2)
            print(" Good driving " + name)
    elif chosenPath2 == "go around":
        hoursLeft -= 2
        print()
        print("Apollo: Fine, start driving")
        time.sleep(2)
        print(" We better hope we make it in time")


def timeCheck():
    if hoursLeft == 0:
        print()
        time.sleep(2)
        print("Hours Left [", hoursLeft, "]")
        print()
        time.sleep(1)
        print("*You ran out of time*")
        playAgain = ""
        while playAgain != "yes" and playAgain != "y":
            playAgain = input("Do you want to play again? [Yes] or [Y] to continue playing: ").lower()
        if playAgain == "yes" or "y":
            print()
            print("*Starting from checkpoint*")
            rover1()
        else:
            return
        return


#intro()

#name = input("What is your name?: ").lower()
name = "Daniel"

#intro2()
#part1()
#rover1()
#rover2()
rover3()

