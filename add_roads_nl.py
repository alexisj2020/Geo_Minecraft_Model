from PIL import Image
from PIL import ImageOps
import numpy as np
import pandas as pd
import sys

from gdpc import __url__, Editor, Block

editor = Editor(buffering=True)
buildArea = editor.getBuildArea()
editor.loadWorldSlice(cache=True)
heightmap = editor.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

# Open image
img = Image.open("maps/roads_map.png")
img = img.convert('RGB')

# Resize smoothly down
img_r = img.resize((1153, 852), resample=Image.Resampling.NEAREST)

#create numpy array from resized map
arr = np.array(img_r)

arr = arr[:,:,:3]

#remove unwanted RGB values
rows, cols, z = arr.shape
arr_fix = np.empty(shape=(rows,cols,z), dtype = int)
for x in range(rows):
    for y in range(cols):
        if (np.array_equal(arr[x,y],[ 0, 0, 0])
        or np.array_equal(arr[x,y],[255, 255, 255])):
            arr_fix[x,y] = arr[x,y]
        else:
            arr_fix[x,y] = arr_fix[x-1,y]

#combine R, G, and B values into single rgb string
rows, cols, z = arr.shape
arr_rgb = np.empty(shape=(rows,cols), dtype = int)
for x in range(rows):  
    for y in range(cols):
        arr_rgb[x,y] = ''.join(str(n) for n in arr_fix[x,y])

#place blocks according to map array
for x in range (0,1153):
    for z in range(0,852):
        if arr_rgb[z,x]==000:
            editor.placeBlock((x,heightmap[x,z],z), Block("bricks"))