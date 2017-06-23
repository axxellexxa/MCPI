
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

# Instructions
mc = minecraft.Minecraft.create()
mc.postToChat("Minecraft Whac-a-Block")
mc.postToChat("              ")
time.sleep(2)
mc.postToChat("Instructions (Read it all before starting):")
time.sleep(1)
mc.postToChat("1.) Right click blue blocks to score a point")
time.sleep(1)
mc.postToChat("2.) Don't let all of the blocks turn blue")
time.sleep(1)
mc.postToChat("3.) Right click to select the options")
time.sleep(1)
mc.postToChat("Have fun!")
time.sleep(5)

# To get the your position
pos = mc.player.getTilePos()

# Variables for the blocks
green = block.IRON_BLOCK.id
yellow = block.GOLD_BLOCK.id
red = block.DIAMOND_BLOCK.id
death = block.GLOWING_OBSIDIAN.id
white = block.WOOL.id
black = block.OBSIDIAN.id

# To make the gameboard
mc.setBlocks(pos.x - 1, pos.y, pos.z + 4,
             pos.x + 1, pos.y + 2, pos.z + 4,
             block.GLOWSTONE_BLOCK.id)

# To make the settings
mc.setBlock(pos.x + 1, pos.y - 1, pos.z + 1, green)
mc.setBlock(pos.x, pos.y - 1, pos.z + 1, yellow)
mc.setBlock(pos.x - 1, pos.y - 1, pos.z + 1, red)
mc.setBlock(pos.x, pos.y - 1, pos.z + 2, death)
mc.setBlock(pos.x - 2, pos.y, pos.z + 1, white)
mc.setBlock(pos.x + 2, pos.y, pos.z + 1, black)

# Misc. variables
blocksLit = 0
points = 0
nap = 0
penalties = 0
mode = "None"
penalty = "None"
modeSelect = False
modeChoose = False
modeDeath = False

# The configuration of all the 4 difficulties
mc.postToChat("              ")
mc.postToChat("Now, select your difficulty level using the blocks below")
while modeSelect == False:
    for hitBlock in mc.events.pollBlockHits():
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == green:
            nap = 0.5
            mode = "Easy Iron"
            mc.postToChat("Your difficulty is now Easy Iron")
            time.sleep(3)
            modeSelect = True
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == yellow:
            nap = 0.2
            mode = "Great Gold"
            mc.postToChat("Your difficulty is now Great Gold")
            time.sleep(3)
            modeSelect = True
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == red:
            nap = 0.08
            mode = "Difficult Diamond"
            mc.postToChat("Your difficulty is now Difficult Diamond")
            time.sleep(3)
            modeSelect = True
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == death:
            nap = 1
            mode = "???"
            mc.postToChat("Your difficulty is unknown")
            time.sleep(3)
            modeDeath = True
            modeSelect = True

# The choice of having a penalty
mc.postToChat("              ")
mc.postToChat("Then, turn on or off the penalty, using the white and")
mc.postToChat("black blocks beside you, respectively")
while modeChoose == False:
    for hitBlock in mc.events.pollBlockHits():
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == white:
            penalty = "On"
            mc.postToChat("Penalty is on") 
            modeChoose = True
            time.sleep(3)
            mc.postToChat("Get ready ...")
            time.sleep(1)
            mc.postToChat("Go!")
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == black:
            penalty = "Off"
            mc.postToChat("Penalty is off")
            modeChoose = True
            time.sleep(3)
            mc.postToChat("Get ready ...")
            time.sleep(1)
            mc.postToChat("Go!")
            
# For modeDeath == True
if modeSelect == True & modeChoose == True & modeDeath == True:            
    while blocksLit < 9:
        nap = nap - 0.01 # This incrases the difficulty over time
        time.sleep(nap)
        blocksLit = blocksLit + 1
        lightCreated = False
        while not lightCreated:
            xPos = pos.x + random.randint(-1,1)
            yPos = pos.y + random.randint(0,2)
            zPos = pos.z + 4
            if mc.getBlock(xPos, yPos, zPos) == block.GLOWSTONE_BLOCK.id:
                mc.setBlock(xPos, yPos, zPos, block.NETHER_REACTOR_CORE.id)
                lightCreated = True
        for hitBlock in mc.events.pollBlockHits():
            if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.NETHER_REACTOR_CORE.id:
                mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.GLOWSTONE_BLOCK.id)
                blocksLit = blocksLit - 1
                points = points + 1
                print("Points +1")
            else:
                if penalty == "On":
                    if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
                        mc.setBlock(xPos, yPos, zPos, block.NETHER_REACTOR_CORE.id)
                        blocksLit = blocksLit + 1
                        penalties = penalties + 1
                        print("Penalty given")
else: # For modeDeath == False          
    while blocksLit < 9:
        time.sleep(nap) # This has a fixed difficulty
        blocksLit = blocksLit + 1
        lightCreated = False
        while not lightCreated:
            xPos = pos.x + random.randint(-1,1)
            yPos = pos.y + random.randint(0,2)
            zPos = pos.z + 4
            if mc.getBlock(xPos, yPos, zPos) == block.GLOWSTONE_BLOCK.id:
                mc.setBlock(xPos, yPos, zPos, block.NETHER_REACTOR_CORE.id)
                lightCreated = True
        for hitBlock in mc.events.pollBlockHits():
            if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.NETHER_REACTOR_CORE.id:
                mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.GLOWSTONE_BLOCK.id)
                blocksLit = blocksLit - 1
                points = points + 1
                print("Points +1")
            else:
                if penalty == "On":
                    if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
                        mc.setBlock(xPos, yPos, zPos, block.NETHER_REACTOR_CORE.id)
                        blocksLit = blocksLit + 1
                        penalties = penalties + 1
                        print("Penalty given")

# Tells you your score, difficulty, penalty mode and penalties, if any
mc.postToChat("          -=<Game Over>=-")
mc.postToChat("Your Score was " + str(points))
mc.postToChat("Your Difficulty was " + str(mode))
mc.postToChat("Your Penalty was " + str(penalty))
if penalty == "On":
    mc.postToChat("You had " + str(penalties) + " penalties")

print("          -=<Game Over>=-")
print("Your Score was " + str(points))
print("Your Difficulty was " + str(mode))
print("Your Penalty was " + str(penalty))
if penalty == "On":
    print("You had " + str(penalties) + " penalties")

