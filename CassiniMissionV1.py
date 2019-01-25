# The Cassini mission
# Version 1
# Daniel Hitchcock
# 23/01/2019

def intro():
    print("*recording started*")
    print("Hello..")
    print("is this thing on?")
    print("to whomever recieves this message please listen carefully.")
    print("STAY")
    print("AWAY")
    print("FROM")
    print("TITAN")
    print()
    print("My name is: ")

def chooseName():
    name = ""
    while name != "pandora" and name != "leo":
        name = input("What is your name? [Pandora] [Leo]: ").lower()
    return name

def intro2():
    print("I am a Pilot Engineer aboard the Saturn Orbiter..")
    print("and last survivor of the Cassini mission")
    print("today is monday, the date is the 16th of may 2029")
    print("2 weeks ago we successfully landed on Titan..")
    print("4 days ago a lethal virus infected our Commander Apollo")
    print("We tried to contain him as fast as possible but this virus..")
    print("it changes people")
    print("the virus eventually infected our entire crew..")
    print()
    print("Including me..")
    print()
    print ("*one week earlier*")


intro()
chooseName()
intro2()
