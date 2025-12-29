from PIL import Image
from PIL import ImageOps
import numpy as np
import pandas as pd
import sys

from gdpc import __url__, Editor, Block

geo = open("detailed_geology_d_quotes.txt", "r")
lst=[]
for line in geo:
    lst.append([ (x) for x in line.split()])

rgb = [ x[0] for x in lst]
block = [ x[1] for x in lst]
rgb = [int(s) for s in rgb]
block=tuple(block)


editor = Editor(buffering=True)
buildArea = editor.getBuildArea()
editor.loadWorldSlice(cache=True)
heightmap = editor.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

arr_fix = np.loadtxt("arr_det_geo_fix.txt", dtype=int)

for x in range (0,577):
    for z in range(0,428):
        for y in range(0, heightmap[x,z]):
            if arr_fix[z,x]==255255255:
                editor.placeBlock((x,heightmap[x,z]-1,z), Block("air"))
                editor.placeBlock((x,heightmap[x,z]-2,z), Block("water"))
for n in range(0,1033):
    for x in range (0,577):
        for z in range(0,428):
            for y in range(0, heightmap[x,z]):  
                if arr_fix[z,x]==rgb[n]:
                    editor.placeBlock((x,y,z), Block(block[n]))
#for n in range(0,1033)...