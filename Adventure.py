print ("You are a detective that has been assigned the case of a mass murder in a hotel room")
print ("There are two dead bodies in front of you, one female and one male")
print ("[1 Female] [2 Male]")

body = int(input("Who do you inspect?:"))

if body == 1:
    print ("You inspect the woman to find a wound on the side of her head.")
    print ("The woman also seems to be holding a gun in her right hand")
    print ("Her purse is on the floor next to her")
    print ("[1 Inspect wound] [2 Inspect gun] [3 Inspect purse]")
    choice1 = int(input("What do you do?:"))
    if choice1 == 1:
        print ("The wound seems to be a strike from a blunt object")
        print ("[1 Inspect gun] [2 Inspect purse] [3 Return to bodies]")
        choice1a = int(input("What do you do?:"))

        if choice1a == 1:
            print ("The guns barrel is still hot and there is gun powder on the carpet, the gun was fired")
            print ("[1 Inspect purse] [2 Return to bodies]")
            choice1b = int(input("What do you do?:"))
            if choice1b == 1:
                print ("She has ID in her purse that says her name is Maria Tumblewood")
                print ("You finish inspecting the woman and return to the bodies")
                print ("[1 Female] [2 Male]")
                body = int(input("Who do you inspect?:"))
            elif choice1b == 2:
                print ("[1 Female] [2 Male]")
                body = int(input("Who do you inspect?:"))


        elif choice1a == 2:
            print ("She has ID in her purse that says her name is Maria Tumblewood")
            print ("[1 Inspect gun] [2 Return to bodies]")
            choice1c = int(input("What do you do?:"))
            if choice1c == 1:
                print ("The guns barrel is still hot and there is gun powder on the carpet, it was fired")
                print ("You finish inspecting the woman and return to the bodies")
                print ("[1 Female] [2 Male]")
                body = int(input("Who do you inspect?:"))
            elif choice1c == 2:
                print ("[1 Female] [2 Male]")
                body = int(input("Who do you inspect?:"))



    elif choice1 == 2:
        print ("The guns barrel is still hot and there is gun powder on the carpet, it was fired")
        print ("[1 Inspect wound] [2 Inspect gun] [3 Inspect purse]")
        choice1 = int(input("What do you do?:"))

    elif choice1 == 3:
        print ("She has ID in her purse that says her name is Maria Tumblewood")
        print ("[1 Inspect wound] [2 Inspect gun] [3 Inspect purse]")
        choice1 = int(input("What do you do?:"))


elif body == 2:
    print ("You inspect the man to see a gun shot wound in his chest")
