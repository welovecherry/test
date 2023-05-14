from minecraft import *

'''
print(False or False or False or False)
print(False or False or False or True)
'''
'''
x = 109
y = 300
z = -74
setpos(x, y, z)

hw = 5
hl = 6
hh = 8
woodblock = 5
airblock = 0

setblocks(x-hw, y, z-hl, x+hw, y+hh, z+hl, woodblock)


def AND_gate(input1, input2):
    if input1 and input2:
        return True
    else:
        return False

print(AND_gate(1, 0))

print(1 and 0) '''

'''
mw = Minecraft.create()
position = mw.player.getTilePos()
x = position.x
y = position.y
z = position.z

agree = input("Create a crater? yes or no")
if agree == "yes" :
    mw.setBlocks(x-1, y-1, z-1, x+1, y+1, z+1, 0)
else :
    print("hi")

'''


from mcpi.minecraft import Minecraft
mw = Minecraft.create()
position = mw.player.getTilePos()
x = position.x
y = position.y
z = position.z
agree = input("Are you hungry?\n")
if agree == "yes" :
    mw.setBlock(x, y, z, 92)
else :
    mw.postToChat("I'm not hungry") '''

'''
from mcpi.minecraft import Minecraft
mw = Minecraft.create()
position = mw.player.getTilePos()
x = position.x
y = position.y
z = position.z
block = mw.getBlock(x, y-1, z)
answer = input("square, cross, circle\n")
if answer == "square" :
    mw.setBlocks(x-1, y, z-1, x+1, y, z+1, block)
elif answer == "cross" :
    mw.setBlocks(x-1, y, z, x+1, y, z, block)
    mw.setBlocks(x, y, z-1, x, y, z+1, block)
elif answer == "circle" :
    mw.setBlocks(x-1, y, z, x+1, y, z, block)
    mw.setBlocks(x, y, z-1, x, y, z+1, block)
    mw.setBlock(x, y, z, 0)
else :
    mw.postToChat("sorry, I can't build that")'''




from mcpi.minecraft import Minecraft
mw = Minecraft.create()
position = mw.player.getTilePos()
x = position.x
y = position.y
z = position.z

mw.setBlocks(x-6, y-3, z-4, x+6, y, z+4, 57)
mw.setBlocks(x-5, y, z-3, x+5, y, z+3, 0)
mw.setBlocks(x+3, y, z, x+3, y+7, z, 57)
mw.setBlocks(x, y+7, z, x+2, y+7, z, 42)
mw.setBlocks(x-1, y+6, z-1, x+1, y+6, z+1, 42)




