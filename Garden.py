# Exercise 36: Designing and Debugging - Learn Python the Hard Way
# http://learnpythonthehardway.org/book/ex36.html
# This script is designed for Python 3, but it should work with other versions. However, the 'from sys import exit' and 'exit(0)' statements may cause issues in other versions.

# The exit function allows the program to terminate and return the user to the command prompt.
from sys import exit

# Importing the 'os' module to use the 'os.system('clear')' function, which clears the screen.
import os

# The game areas are based on a map and potential plot lines.
# Map: https://drive.google.com/open?id=0B_QocyXoG7zlNk1jYnhSOVcyTXM
# For more story ideas, visit:
# http://www.write4fun.net/view-entry/205506
# http://www.collegehumor.com/tag/choose-your-own-adventure

# *****Known Issues*****
# Currently, after collecting a crystal, the choice text changes, but the option remains available, allowing the player to collect the same crystal multiple times. This does not affect the game's functionality, but it can result in duplicate crystals in the backpack.

# Backpack Inventory
# To fix this issue, we need to ensure that each crystal can only be collected once. This can be achieved by removing the crystal from its location when it is added to the backpack.
# Alternatively, we can hide the choice to collect the crystal if it is already in the backpack.
# To implement this, add the following code to the choices section of each garden area to change the choice from 'search' to 'found':
#    try:
#        backpack.index("<crystal name>")
#    except ValueError:
#        print("<choice that finds crystal>")
#    else:
#        print("<text saying the crystal has been found>")
#    choice = input("What will you do? > ")

backpack = ['water']
backpackFilled = ['water','red crystal','clear crystal','yellow crystal','green crystal','blue crystal']

def addToBackpack(item):
    backpack.append(item)

# Check all crystals are collected before exiting the garden.
# To do this, we can add a check that compares the player's current inventory ('backpack') to the required inventory ('backpackFilled') and restrict access until all crystals are found.


def crystal_check():
    backpack
    backpackFilled  = ['water','red crystal','clear crystal','yellow crystal','green crystal','blue crystal']
    for crystal in backpack:
        print ("You have a %s" % crystal)
    print ("")
    for item in backpackFilled:
        print ("You should have a %s" % item)
    exit(0)

# Main Script with Garden Areas and Navigation

def clear():
    os.system ('clear')
    print ("As you enter this part of the garden the first thing you notice is a large marble fountain in the center of the clearing with geysers of water shooting high into the sunlit sky.  Once you are able to drag your eyes from the fountain you see little else.  The ground is covered in a thin layer of crushed marble flakes. There are two archways leading back into the garden.  One is to the west and the other to the east. You realize this must be the center of the garden.  The focal point of this odd, yet beautiful place.")
    print ("Your backpack contains: ", backpack)
    print ("You can:")
    print ("1. Head through the archway to the east")
    print ("2. Head through the archway to the west")
    try:
        backpack.index("clear crystal")
    except ValueError:
        print("3. Look closer at the fountain.")
    else:
        print ("You see the fountain you took the clear crystal from.")
    choice = input("What will you do? > ")


# use these to send the player to other locations

    if choice == "1":
        print ("\nYou turn toward the eastern archway and head down the path. You begin to feel a breeze on your face as you move along the path.\n")
        input("<enter>") # pauses before calling the 'blue' function which will clear the screen and display the room text
        blue()
    elif choice == "2":
        print ("\nYou turn toward the western archway and head down the path. The path and walls gradually becomes covered in vines.\n")
        input("<enter>")
        green()
    elif choice == "3": #crystal
        print ("\nYou look closer at the fountain.  Something sparkling in the water catches your eye and you realize it is a perfectly transparent crystal.  You take the clear crystal and add it to your backpack.\n")
        backpack # lets the function know what backpack is
        addToBackpack("clear crystal") # calls the 'addToBackpack' function and sends it 'clear'
        print ("You have the following crystals: ", backpack) # prints what is in the backpack inventory
        input("<enter>")
        clear()
    else:
        print ("\nI'm sorry, but I don't understand.\n")
        input("<enter>")
        clear()

def yellow():
    os.system ('clear')
    print ("The sun is dazzling in this part of the garden.  You quickly realize its very hard to see because the sun is reflecting off many shiny surfaces.  Shielding your eyes with your hand you squint through your fingers to have a look. You see several archways leading out of this part of the garden.  And though you can't make out what the shiny objects are they appear to be on stone pedestals.")
    print ("Your backpack contains: ", backpack)    
    print ("You can:")
    print ("1. Head through the open gated archway to the north")
    print ("2. Head through the archway to the east")
    print ("3. Head through the archway to the west")
    try:
        backpack.index("yellow crystal")
    except ValueError:
        print("4. Have a closer look at the shiny objects.")
    else:
        print ("You see the spot where you found the yellow crystal")



    choice = input("What will you do? > ")

# use these to send the player to other locations

    if choice == "1": # need to check for crystals
        print ("\nYou turn toward the northern archway and head down the path. As you leave the garden gates close behind you.  I hope you found all five crystals.  \n")
        input("Click <enter> to check your backpack.")
        crystal_check()
        exit(0)
    elif choice == "2":
        print ("\nYou turn toward the eastern archway and head down the path. As the path curves to the right you begin to feel a breeze on your face as you move along the path. \n")
        input("<enter>")
        blue()
    elif choice == "3":
        print ("\nYou turn toward the western archway and head down the path. After a short time the path and walls become completely covered by green vines. The path curves left and soon you are in another part of the garden. \n")
        input("<enter>")
        green()
    elif choice == "4": #crystal
        print ("\nYou continue to shield your eyes and walk to the closest pillar.  You begin to see that the object is a sundial made of metal with a mirrored finish.  The symbols on the metal don't look familiar to you, but you guess it's some time just after noon based on the position of the shadow.  Then you see it.  Right where the shadow is pointing is a small yellow crystal.  You pick up the crystal and place it in your backpack.\n")
        backpack
        addToBackpack("yellow crystal")
        print ("You have the following crystals: ", backpack)
        input("<enter>")
        yellow()
    else:
        print ("\nI'm sorry, but I don't understand.\n")
        input("<enter>")
        yellow()

def blue():
    os.system ('clear')
    print ("Here the garden has small pools of water surrounds by vibrate blue flowers.  They a have the most lovely hue of color with slightly lighter shade on the inside.  There is a soft breeze in this part of the garden making quiet ripples on the surface of the pools. There several paths leading out of here to the north, west, and south.")
    print ("Your backpack contains: ", backpack)    
    print ("You can:")
    print ("1. Head through the archway to the north")
    print ("2. Head through the archway to the west")
    print ("3. Head through the archway to the south")
    try:
        backpack.index("blue crystal")
    except ValueError:
        print("4. Investigate the pools of water.")
    else:
        print ("You see the spot where you found the blue crystal")
    



    choice = input("What will you do? > ")

# use these to send the player to other locations

    if choice == "1":
        print ("\nYou turn toward the northern archway and head down the path. As the path curves to the left you quickly notice how bright your surroundings are becoming.\n")
        input("<enter>")
        yellow()
    elif choice == "2":
        print ("\nYou turn toward the western archway and head down the path. You begin to hear crashing water coming from the other end of the path.\n")
        input("<enter>")
        clear()
    elif choice == "3":
        print ("\nYou turn toward the southern archway and head down the path. As the path curves right you start seeing large red flowers blooming on the vines. You then come to another part of the garden.\n")
        input("<enter>")
        red()
    elif choice == "4":
        print ("\nJust below the surface of the pools are countless oval shaped blue crystals.  You take one and add it to your backpack.\n")
        backpack
        addToBackpack("blue crystal")
        print ("You have the following crystals: ", backpack)
        input("<enter>")
        blue()

    else:
        print ("\nI'm sorry, but I don't understand.\n")
        input("<enter>")
        blue()

def green():
    os.system ('clear')
    print ("This part of the garden is almost completely lost to the green vines.  They are so think that it almost looks likes a sea swirling around the clearing.  Among the thick vines you see what must be statues completely covered.  It is very difficult for you move around.  You wonder if you could even get back out.  You see archways to the south, west, and north leading to other parts of the garden.")
    print ("Your backpack contains: ", backpack)    
    print ("You can:")
    print ("1. Head through the archway to the north")
    print ("2. Head through the archway to the east")
    print ("3. Head through the archway to the south")
    try:
        backpack.index("green crystal")
    except ValueError:
        print ("4. Look closer at the vines.")
    else:
        print ("You see the spot where you found the green crystal")
    
    print ("5. Look closer at the statues.")


    choice = input("What will you do? > ")

# use these to send the player to other locations

    if choice == "1":
        print ("\nYou turn toward the northern archway and head down the path. As the path curves to the right you quickly notice how bright your surroundings are becoming. \n")
        input("<enter>")
        yellow()
    elif choice == "2":
        print ("\nYou turn toward the eastern archway and head down the path. You begin to hear crashing water coming from the other end of the path. \n")
        input("<enter>")
        clear()
    elif choice == "3":
        print ("\nYou turn toward the southern archway and head down the path. As the path curves you start see large red flowers blooming on the vines. You then come to another part of the garden. \n")
        input("<enter>")
        red()
    elif choice == "4": #crystal
        print ("\nYou look closer at the vines.  In a particularly tangled portion of the vines you find a small green crystal under a leaf.  You take the crystal and add it to your backpack.\n")
        backpack
        addToBackpack("green crystal")
        print ("You have the following crystals: ", backpack)
        input("<enter>")
        green()
    elif choice == "5":
        print ("\nThere are three statues in all. You carefully move the vines to get a better look. The first is a bird with a fish in its mouth. The second is a bear with a fish in its mouth. The third is a seal with a fish in its mouth.\n")
        input("<enter>")
        green()
    else:
        print ("\nI'm sorry, but I don't understand.\n")
        input("<enter>")
        green()

def red():
    os.system ('clear')
    print ("This part of the garden has large, red, bowl shaped flowers everywhere.  They are attached to vines that climb the walls and crisscross the ground in all directions.  There are several small statues standing in the garden as well.  Each is holding a different style container that is pouring water on their feet. There is an archway leading to the west and one to the east. To the south is a locked gate back to the forest.\n")
    print ("Your backpack contains: ", backpack)    
    print ("You can:")
    print ("1. Head through the archway to the west")
    print ("2. Head through the archway to the east")
    try:
        backpack.index("red crystal")
    except ValueError:
        print ("3. Look closer at the flowers.")
    else:
        print ("You see the spot where you found the green crystal")

    print ("4. Look closer at the statues.")


    choice = input("What will you do? > ")

# use these to send the player to other locations

    if choice == "1":
        print ("\nYou turn toward the western archway and head down the path.  After a short time the red flowers begin to become less and less leaving just the green vines. The path curves north and soon you are in another part of the garden.\n")
        input("<enter>")
        green()
    elif choice == "2":
        print ("\nYou turn toward the eastern archway and head down the path.  After a short time the red flowers begin to become less and less.  They are being replaced by vibrate blue fluted flowers. The path curves left and soon you are in another part of the garden.\n")
        input("<enter>")
        blue()
    elif choice == "3": #crystal
        print ("\nYou look closer at the red flowers.  The smell of the flowers reminds you of sweat candy treats on a beautiful summer day.  As you move from flower to flower you come across a small red crystal in one of them.  You take the crystal and add it to your backpack.\n")
        backpack
        addToBackpack("red crystal")
        print ("You have the following crystals: ", backpack)
        input("<enter>")
        red()
    elif choice == "4":
        print ("\nThere are four statues in all.  They range in age from a small girl holding a large jug to an elderly man with a tiny cup.  Each one is smiling as they pour water on to their feet.\n")
        input("<enter>")
        red()
    else:
        print ("\nI'm sorry, but I don't understand.\n")
        input("<enter>")
        red()




# Why is the start placed at the end of the program?
# All necessary functions and variables are defined before they’re used, allowing the program to execute correctly.

def enterance():
    os.system ('clear')
    print (" The Garden -- an interactive short story")
    print (" This adventure game has a simple list of commands it recognizes.\n")
    print ("After traveling through the forest for some time you unexpectedly come to a clearing filled with warm sunlight. At it's center you see a large wall that seems as if it grew there. It is made of a think tangle of flowering plants. In the center of the wall is a gate.  It is open a jar showing you that you may enter. The trail you were traveling on continues into the forest on your right.\n")
    print ("You can:")
    print ("1. Enter the gate")
    print ("2. Head off down the trail back into the forest")


    choice = input("What will you do? > ")

# use these to send the player to other locations
    if choice == "1":
        print ("\nYou take a sip of water, adjust your backpack and decide to enter the gate. As you pass through the gate it closes behind you.")
        input("<enter>")
        red()
    elif choice == "2":
        print ("\nYou came to walk in the forest, not explore mysterious gated walls. You turn from the gate and continue into the forest.")
        input("<enter>")
        exit(0)
    else:
        print ("\nI'm sorry, but I don't understand.")
        input("<enter>")
        enterance()





# this starts the script and calls the "entrance" function
enterance()
