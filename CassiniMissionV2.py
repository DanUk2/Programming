# The Cassini mission
# Version 2
# Daniel Hitchcock
# 23/01/2019
import random
import time
Gameover = False
inv = ["Key Card", "Laser Cutter", "Welding Tool"]

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
    print(" once we get this drone up and running we can explore the surface")
    time.sleep(2)
    print("")

def chooseHelp():
    helpJosh = ""
    while helpJosh != "yes" and helpJosh != "no":
        helpJosh = input ("Help Leo? [Yes] [No]: ").lower()
    if helpJosh == "no":
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
        print(" This research could really save the world")
        time.sleep(3)
        print(" Potenially create a new one")
        time.sleep(3)
    elif helpJosh == "yes":
        return helpJosh



intro()

name = input("What is your name?: ").lower()
#name = "Daniel"

intro2()
part1()
