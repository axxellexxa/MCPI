import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

# To get the player's position
pos = mc.player.getTilePos()

# To make space for the gameboard
mc.setBlocks(pos.x - 1, pos.y - 1, pos.z - 1,
             pos.x + 1, pos.y - 1, pos.z + 1,
             0)
# To make the gameboard
mc.setBlocks(pos.x - 1, pos.y - 2, pos.z - 1,
             pos.x + 1, pos.y - 2, pos.z + 1,
             block.STONE.id)
mc.setBlock(pos.x, pos.y - 2, pos.z, 2)
