# The Cassini mission
# Version 6
# Daniel Hitchcock
# 27/01/2019
import time
import random
Gameover = False
inv = ["laser cutter", "blowtorch", "welding tool", "wrench", "gps"]
global hoursLeft
hoursLeft = 5
correctFormula = {"Magnesium" : 2, "Barium" : 1, "Sodium Chloride" : 1, "Phosphorous" : 3}
usrFormula = {"Magnesium" : 0, "Barium" : 0, "Sodium Chloride" : 0, "Phosphorous" : 0}
global choicePath3
choicePath3 = 1
global leoChoice
global pandoraChoice
leoChoice = 1
pandoraChoice = 0

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
    print("and last survivor of the Cassini rescue mission")
    time.sleep(3)
    print("today is monday, the date is the 16th of may 2029")
    time.sleep(3)
    print("1 weeks ago we received a stress signal from the ground team on titan")
    time.sleep(3)
    print("Our mission was to investigate and extract them back to the Orbiter")
    time.sleep(2)
    print("But when we got there.. There was nothing left of them")
    time.sleep(4)
    print("Just the thing that tore them apart..")
    time.sleep(2)
    print("This thing.")
    time.sleep(1)
    print("It eventually infected my enitre team")
    time.sleep(3)
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
    print(" once we get this rover up and running we can reach the stress signal")
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
    time.sleep(2)
    print(" Let the exhibition begin!")
    time.sleep(2)
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
        print("Leo: That's not a wrench")
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
        print(" His sister was part of the ground team")
        time.sleep(3)
        print(" I hope they're okay")
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
    print(" If we don't make it to the bunker by nightfall, we'll freeze to death")
    time.sleep(3)
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
    print("Apollo: Okay nobody panic")
    time.sleep(2)
    print(" Looks like we drove onto some quicksand")
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
    if hoursLeft == 0:
        print()
        time.sleep(1)
        print("Apollo: Doesn't matter, we ran out of daylight, we wont make it")
    else:
        return
    timeCheck()


def bunker1():
    print("Pandora: I see the bunker up ahead!")
    print()
    time.sleep(2)
    print("Apollo: Stop here " + name)
    time.sleep(1)
    print(" Everyone get out, the signal is inside")
    time.sleep(2)
    print(" Grab everything we have left and follow my lead")
    time.sleep(2)
    print(" Who knows what happened in there")
    print()
    time.sleep(2)
    print("Pandora: Don't worry Sir, im sure she's fine")
    print()
    time.sleep(2)
    print("Apollo: For our sake, me too")
    time.sleep(2)
    print()
    print("*Entered the Bunker*")
    print()
    time.sleep(2)
    print("Pandora: Hellooo?")
    time.sleep(1)
    print(" Is anyone here")
    time.sleep(2)
    print()
    print("Leo: Pandora be quiet!")
    time.sleep(1)
    print(" We don't know what's in here")
    time.sleep(2)
    print(" The whole place could be compromised")
    print()
    time.sleep(2)
    print("Apollo: The signal is just in this next room")
    print()
    time.sleep(2)
    print("Leo: 'The Lab'? Why would it come from here?")
    time.sleep(2)
    print()
    print("Apollo: I don't know and don't need to know")
    time.sleep(2)
    print(" On my lead")
    time.sleep(2)
    print(" GO!")
    print()
    time.sleep(2)
    print("Pandora: Oh my god")
    time.sleep(2)
    print(" What-")
    time.sleep(1)
    print(" What happened here?")
    print()
    time.sleep(2)
    print("Leo: They're dead")
    time.sleep(1)
    print(" They're all dead")
    time.sleep(2)
    print()
    print("Apollo: Not everyone, Sandra's body isn't here")
    time.sleep(2)
    print()
    print("Pandora: What do you think done this?")
    time.sleep(2)
    print()
    print("*Screams from another room*")
    time.sleep(1)
    print("Unknown: HELP!")
    print()
    time.sleep(1)
    print("Leo: What was that?")
    time.sleep(2)
    print()
    print("Apollo: That's her!")
    time.sleep(2)
    print(" Leo and Pandora, look around for any clues")
    time.sleep(2)
    print(" I'll go check out the noise")
    time.sleep(2)
    print()
    print("Leo: Sir are you sure that's a good idea?")
    print()
    time.sleep(2)
    print("Apollo: Don't argue with me Leo! Follow my orders")
    time.sleep(2)
    print()
    print("Leo: Yes Sir!")
    print()
    time.sleep(2)
    print("Apollo:", name, ", are you coming with me or staying here?")
    time.sleep(2)
    print()
    choice3 = choosePath3()
    checkPath3(choice3)
    bunker2()


def bunker2():
    time.sleep(2)
    print("*Apollo tackles Leo*")
    print()
    time.sleep(2)
    print("Leo: AHHH!")
    print()
    time.sleep(2)
    print("Pandora: LEO!")
    time.sleep(1)
    print(" IM COMING!")
    time.sleep(1)
    print()
    print("*Pandora runs to help Leo*")
    time.sleep(2)
    print()
    print("Pandora: GET OFF HIM!")
    print()
    time.sleep(1)
    print("*Apollo hits Pandora across the room*")
    print()
    time.sleep(2)
    print("Pandora: Uh!")
    print()
    time.sleep(1)
    print("Leo:", name.upper(), "GET HIM OFF ME!")
    print()
    time.sleep(2)
    print("Pandora: Help me up", name, "!")
    time.sleep(3)
    print()
    chooseSave()

def bunkerLeo():
    print("*You slam the door shut*")
    time.sleep(2)
    print()
    item2()
    print()
    print("*Leo welds the door shut*")
    print()
    time.sleep(2)
    print("Leo: That should hold them for now")
    time.sleep(2)
    print(" What the fuck happened back there", name, "!?")
    time.sleep(2)
    if choicePath3 == 2:
        print()
        print("Leo: I need to tell you something")
        time.sleep(2)
        print(" While you were gone we found out that we're all infected")
        time.sleep(2)
        print(" From the moment we stepped foot on this goddamn planet")
        time.sleep(3)
        print(" Contact with a host just speeds up the infection")
        time.sleep(2)
        print(" In a matter of time we'll turn into those things")
        time.sleep(2)
        print(" Pandora found the formula for the cure but..")
        time.sleep(2)
        print(" She had it on her and now shes gone")
        time.sleep(2)
        print(" So what do we do now?")
        endingLeo1()
    elif choicePath3 == 1:
        print()
        print("Leo: Do you remember the formula for the cure?!")
        time.sleep(2)
        print(" Doesn't matter, we dont have time")
        time.sleep(2)
        print(" get over there and think of something")
        time.sleep(2)
        leoFormula()


def leoFormula():
    print()
    print("[Add the correct number of chemicals in order]")
    print()
    usrFormula["Magnesium"] = 0
    usrFormula["Barium"] = 0
    usrFormula["Sodium Chloride"] = 0
    usrFormula["Phosphorous"] = 0
    print(usrFormula)
    print()
    mag = int(input("Magnesium: "))
    usrFormula["Magnesium"] += mag
    print(usrFormula)
    print()
    bar = int(input("Barium: "))
    usrFormula["Barium"] += bar
    print(usrFormula)
    print()
    sodium = int(input("Sodium Chloride: "))
    usrFormula["Sodium Chloride"] += sodium
    print(usrFormula)
    print()
    phos = int(input("Phosphorous: "))
    usrFormula["Phosphorous"] += phos
    print(usrFormula)
    if usrFormula == correctFormula:
        print()
        print("[Cure Successful]")
        print()
        time.sleep(2)
        print("Leo: Oh my god you did it!")
        time.sleep(2)
        print(" Wait, there's only enough for one cure?")
        time.sleep(2)
        if leoChoice == 1:
            print()
            print("[Leo remembered your decision]")
            time.sleep(2)
            print()
            print("Leo: I need to tell you something " + name)
            time.sleep(2)
            print(" I knew what was waiting for us on Titan")
            time.sleep(2)
            print(" We all did, apart from you")
            time.sleep(2)
            print(" Apollo told us about the virus outbreak in the lab")
            time.sleep(2)
            print(" He promised Pandora and I a lot of money if we helped him")
            time.sleep(2)
            print(" He told us he didn't want you to know")
            time.sleep(2)
            print(" Probably because he knew you'd say no")
            time.sleep(2)
            print(" And we really needed you")
            time.sleep(3)
            print(" Take the cure " + name)
            time.sleep(2)
            print(" We dragged you into this, its only fair if you make it out")
            time.sleep(4)
            print()
            print("*You use the cure*")
            endingLeo2()
        elif leoChoice == 0:
            leoAttack()
    else:
        print()
        print("[Cure Failed]")
        print()
        tryAgain = ""
        while tryAgain != "yes" and tryAgain != "no":
            tryAgain = input("Try Again? [Yes] or [No]: ")
        if tryAgain == "yes":
            leoFormula()
        elif tryAgain == "no":
            print()
            print("Leo: Looks like were stuck here " + name)
            time.sleep(2)
            print(" So what do we do now?")
            endingLeo1()
    return



def leoAttack():
    print()
    print("Leo: Give me the cure " + name)
    time.sleep(2)
    print(" I don't plan on dying here today")
    print()
    time.sleep(1)
    giveCure = ""
    while giveCure != "no":
        giveCure = input("Give him the cure? [No]: ").lower()
    print()
    time.sleep(1)
    print("Leo: I SAID GIVE ME THE CURE", name.upper(), "!")
    print()
    giveCure2 = ""
    while giveCure2 != "no":
        giveCure2 = input("Give him the cure? [No]: ").lower()
    print()
    time.sleep(1)
    print("Leo: ARGH!")
    print()
    time.sleep(1)
    print("*Leo pushes you to the ground*")
    print()
    time.sleep(2)
    print("Leo: I wont ask again " + name)
    time.sleep(2)
    print()
    chooseWeapon()
    print()
    time.sleep(2)
    print("Leo: AAAAAAAAAAAAH!!")
    print()
    time.sleep(1)
    print("Leo: IT BURNS, IT BURNS!")
    time.sleep(2)
    print("*Leo drops dead*")
    time.sleep(2)
    print()
    print("*You use the cure*")
    endingLeo3()

def endingLeo1():
    print()
    time.sleep(3)
    print("*Still recording*")
    print()
    time.sleep(3)
    print("*Sigh*")
    time.sleep(1)
    print("That's how it happened")
    time.sleep(2)
    print("After that Leo turned first")
    time.sleep(2)
    print("Its only a matter of time until I do")
    time.sleep(2)
    print("Whoever finds this message, learn from our mistake")
    time.sleep(2)
    print("STAY AWAY FROM TITAN!")
    time.sleep(2)
    print("My nam-")
    time.sleep(1)
    print("My name is", name[:-3], "...")
    time.sleep(2)
    print("AHHHHH!")
    time.sleep(2)
    print()
    print("*Recording Stopped*")
    print()
    time.sleep(2)
    print("[GAME OVER]")
    print()
    time.sleep(2)
    print("Ending Grade: [D]")

def endingLeo2():
    print()
    time.sleep(3)
    print("*Still recording*")
    print()
    time.sleep(3)
    print("*Sigh*")
    time.sleep(2)
    print("That's how it happened")
    time.sleep(2)
    print("After that Leo sacrificed himself to hold them off")
    time.sleep(3)
    print("The cure has fought back the virus for now")
    time.sleep(3)
    print("However food supplies ran out")
    time.sleep(2)
    print("I have left the formula to the cure attached to this message")
    time.sleep(3)
    print("I hope you find this message before you send the next team here")
    time.sleep(3)
    print("It's too late for us")
    time.sleep(2)
    print("My name is " + name)
    time.sleep(3)
    print("Last survivor of the Cassini mission")
    time.sleep(2)
    print()
    print("*Recording Stopped*")
    print()
    time.sleep(2)
    print("[GAME OVER]")
    print()
    time.sleep(2)
    print("Ending Grade: [A]")

def endingLeo3():
    print()
    time.sleep(3)
    print("*Still recording*")
    print()
    time.sleep(3)
    print("*Sigh*")
    time.sleep(2)
    print("That's how it happened")
    time.sleep(2)
    print("The cure has fought back the virus for now")
    time.sleep(3)
    print("However food supplies ran out")
    time.sleep(2)
    print("I have left the formula to the cure attached to this message")
    time.sleep(3)
    print("I hope you find this message before you send the next team here")
    time.sleep(3)
    print("It's too late for us")
    time.sleep(2)
    print("My name is " + name)
    time.sleep(3)
    print("Last survivor of the Cassini mission")
    time.sleep(2)
    print()
    print("*Recording Stopped*")
    print()
    time.sleep(2)
    print("[GAME OVER]")
    print()
    time.sleep(2)
    print("Ending Grade: [B]")


def chooseWeapon():
    attack = ""
    print(inv)
    print()
    while attack != "laser cutter" and attack != "blowtorch":
        attack = input("Choose a Weapon [Laser Cutter] or [Blowtorch]: ")
    if attack == "laser cutter":
        if attack in inv:
            print()
            print("*You shine the laser into his eyes*")
        else:
            print()
            print("*You don't have this item*")
            chooseWeapon()
    elif attack == "blowtorch":
        print()
        print("*You melt his face*")
    else:
        print()
        print("*That wont work here*")

def item2():
    if "welding tool" in inv:
        print("Leo: Hand me your Welding Tool quick!")
        print()
        time.sleep(1)
        print(inv)
        print()
        welder = ""
        while welder not in inv:
            welder = input("Choose an Item: ").lower()
        if welder != "welding tool":
            print()
            print("Leo: Stop playing around!")
            print()
            item2()
        elif welder == "welding tool":
            print()
            print("*Welding Tool removed from inventory*")
            inv.remove("welding tool")
            print(inv)
            return welder
    else:
        print("Leo: Move out the way!")
        time.sleep(1)
        print(" Im going to weld the door shut")

def bunkerPandora():
    print("*You slam the door shut*")

def chooseSave():
    save = ""
    while save != "leo" and save != "pandora":
        save = input("Who do you want to save? [Leo] or [Pandora]").lower()
    if save == "leo":
        print()
        print("*You push Apollo off Leo*")
        print()
        time.sleep(2)
        print("Pandora: NOOOOOO!")
        print()
        time.sleep(1)
        print("Leo: PANDORA!")
        time.sleep(1)
        print()
        print("*Apollo infects Pandora*")
        time.sleep(2)
        print()
        print("Leo: QUICK SHUT THE DOOR!")
        time.sleep(2)
        print()
        bunkerLeo()
    elif save == "pandora":
        print()
        print("*You help Pandora up*")
        print()
        time.sleep(2)
        print("Leo: AHHHHHH!")
        print()
        time.sleep(1)
        print("Pandora: LEO!")
        time.sleep(1)
        print()
        print("*Apollo infects Leo*")
        time.sleep(2)
        print()
        print("Pandora: QUICK SHUT THE DOOR!")
        time.sleep(2)
        print()
        bunkerPandora()

def choosePath3():
    path3 = ""
    while path3 != "stay" and path3 != "go":
        path3 = input("Choose an option [Stay] or [Go]: ").lower()
    return path3


def checkPath3(chosenPath3):
    global choicePath3
    if chosenPath3 == "stay":
        choicePath3 = 1
        print()
        print("Apollo: Okay you wait and help the others")
        print()
        time.sleep(2)
        print("*Apollo leaves the room*")
        time.sleep(2)
        print()
        print("Pandora: Look at all of this research")
        time.sleep(2)
        print(" Looks like they were trying to find a cure..")
        time.sleep(2)
        print(" But for what?")
        print()
        time.sleep(1)
        print("Leo: Maybe for whatever did this to them")
        time.sleep(2)
        print(" They obviously didn't succeed")
        time.sleep(2)
        print()
        print("Pandora: Hey", name, ", get over here!")
        time.sleep(2)
        print(" This document looks important")
        print()
        read = ""
        while read != "yes" and read != "no":
            read = input("Read the document? [Yes] or [No]: ").lower()
        if read == "yes":
            document()
            print()
        time.sleep(2)
        print("Pandora: With this information we can create the cure!")
        time.sleep(2)
        print(" All of the chemicals are other here" + name)
        time.sleep(2)
        print()
        print("Leo: Okay you two start working on the cure, I'll keep an eye out")
        print()
        time.sleep(1)
        print("*Apollo screams in agony*")
        print()
        time.sleep(2)
        print("Pandora: What was that?")
        print()
        time.sleep(2)
        print("Leo: I think Apollo is coming back")
        time.sleep(2)
        print()
        print("Apollo:..")
        time.sleep(1)
        print()
        print("Pandora: Apollo are you okay?")
        time.sleep(2)
        print()
        print("Apollo:...")
        time.sleep(1)
        print()
        print("Leo: Wait, what's wrong with his face?")
        time.sleep(2)
        print()
        print("Pandora: LEO DON'T GO NEAR HIM!")
        print()
        return
    elif chosenPath3 == "go":
        choicePath3 = 2
        print()
        print("Apollo: Okay come with me quick")
        time.sleep(2)
        print()
        print("*You leave with Apollo*")
        print()
        time.sleep(2)
        print("Apollo: Sandra?!")
        time.sleep(1)
        print(" Is that you?!")
        time.sleep(1)
        print()
        print("*Apollo grabs sandra*")
        print()
        time.sleep(2)
        print("Apollo: I knew you were alive!")
        print()
        time.sleep(2)
        print("Sandra:... Uhhhh")
        time.sleep(1)
        print()
        print("Apollo: It's okay Sandra, I have you now")
        time.sleep(2)
        print()
        print("*Sandra screams and pukes on Apollo*")
        print()
        time.sleep(2)
        print("Apollo: What-?!")
        time.sleep(1)
        print(" What is this?")
        time.sleep(1)
        print(" AHHHHHHHHHHH!")
        time.sleep(1)
        print(" IT BURNS!")
        time.sleep(2)
        print(" RUN", name.upper(), "!")
        time.sleep(1)
        print(" RUN!!")
        run = ""
        while run != "run" and run != "stay":
            run = input("Choose an option [Run] or [Stay]?: ")
        if run == "run":
            print()
            time.sleep(1)
            print("*You start running towards the Lab*")
            print()
            time.sleep(2)
            print("Pandora: What's wrong", name, "?")
            time.sleep(2)
            print(" Quick Leo, shut the door")
            time.sleep(2)
            print()
            print("Leo: Wait, Apollo is still out there, hes coming now")
            time.sleep(2)
            print(" Apollo! Over here!")
            print()
            time.sleep(1)
            print("Pandora: LEO DON'T GO OUT THERE!")
            print()
            time.sleep(2)
            print("Apollo:..")
            time.sleep(1)
            print()
            print("Leo: Apollo?")
            print()
            time.sleep(1)
        elif run == "stay":
            print()
            time.sleep(2)
            print("*Apollo leaps onto you and infects you*")
            print()
            time.sleep(2)
            playAgain = ""
            while playAgain != "yes" and playAgain != "y":
                playAgain = input("Do you want to play again? [Yes] or [Y] to continue playing: ").lower()
            if playAgain == "yes" or "y":
                print()
                print("*Starting from checkpoint*")
                bunker1()
            else:
                return

def document():
    print()
    print("*******************************************************************")
    print("[THE TITAN VIRUS RESEARCH NOTES]")
    print("[02/02/2029]")
    print()
    print("Virus cure attempt #6")
    print()
    print("We are still contained within the lab")
    print("Food supplies are running low and we are losing men each day")
    print("Yesterday we lost another great scientist to the virus")
    print("Some of the infected are still roaming around the bunker")
    print("Including are best researcher Sandra")
    print("We've theorised a new combination of compounds that should work")
    print()
    print("[CURE RECIPE]")
    print()
    print("Magnesium : 2")
    print("Barium : 1")
    print("Sodium Chloride : 1")
    print("Phosphorous : 3")
    print()
    print("If we don't make it, use this formula to cure the infected")
    print()
    print("*******************************************************************")
    time.sleep(10)
    print()
    done = ""
    while done != "yes" and done != "y":
        done = input("Continue? [Yes] or [Y]: ")
    if done == "yes" or "y":
        return

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


def chooseQuicksand():
    quickSand = ""
    global hoursLeft
    global leoChoice
    global pandoraChoice
    while quickSand != "rev" and quickSand != "pull":
        quickSand = input("Choose a Way out [Rev] or [Pull]").lower()
    if quickSand == "rev":
        leoChoice = 1
        hoursLeft -= 1
        print()
        print("[Leo will remember that]")
        print()
        time.sleep(2)
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
        pandoraChoice = 1
        print()
        print("[Pandora will remember that]")
        print()
        time.sleep(2)
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
                rover3()
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
    global hoursLeft
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
            hoursLeft += 5
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
#rover3()
#bunker1()
bunker2()
#leoFormula()

