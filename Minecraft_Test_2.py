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
img = Image.open("geologic_map_from_data.png")
img = img.convert('RGB')

# Resize smoothly down
img_r = img.resize((577, 426), resample=Image.Resampling.NEAREST)

#posterize image to smooth rgb values
img_p = ImageOps.posterize(img_r, 2) 
# Save image
#pixel_post.save('pixel_post.png')

#create numpy array from pixelated map
arr = np.array(img_p)

arr = arr[:,:,:3]
arr.shape

rows, cols, z = arr.shape
arr_rgb = np.empty(shape=(rows,cols), dtype = int)
for x in range(rows):  
    for y in range(cols):
        arr_rgb[x,y] = ''.join(str(n) for n in arr[x,y])

#flip array so that it is ordered properly
#arr_flip=np.flip(arr_rgb,axis=1)
#arr_flip = np.transpose(arr_rgb)
arr_flip = arr_rgb

# read the unique values from numpy array
#unique = np.unique(arr_all_p)
#print(unique)

#use the place block command to place blocks according to the array/map

#y = heightmap[x,z]-1

for x in range (0,577):
    for z in range(0,426):
        for y in range(0, heightmap[x,z]):
            if arr_flip[z,x]==192192192:
                editor.placeBlock((x,62,z), Block("water"))
            if arr_flip[z,x]==192:
                editor.placeBlock((x,y,z), Block("pink_wool"))
            if arr_flip[z,x]==19200:
                editor.placeBlock((x,y,z), Block("gray_wool"))
            if arr_flip[z,x]==19264:
                editor.placeBlock((x,y,z), Block("light_gray_wool"))
            if arr_flip[z,x]==64192:
                editor.placeBlock((x,y,z), Block("black_wool"))
            if arr_flip[z,x]==128192:
                editor.placeBlock((x,y,z), Block("red_wool"))
            if arr_flip[z,x]==128640:
                editor.placeBlock((x,y,z), Block("orange_wool"))
            if arr_flip[z,x]==192064:
                editor.placeBlock((x,y,z), Block("yellow_wool"))
            if arr_flip[z,x]==192128:
                editor.placeBlock((x,y,z), Block("green_wool"))
            if arr_flip[z,x]==192192:
                editor.placeBlock((x,y,z), Block("blue_wool"))
            if arr_flip[z,x]==192640:
                editor.placeBlock((x,y,z), Block("purple_wool"))
            if arr_flip[z,x]==640192:
                editor.placeBlock((x,y,z), Block("brown_wool"))
            if arr_flip[z,x]==1280192:
                editor.placeBlock((x,y,z), Block("lime_wool"))
            if arr_flip[z,x]==1281280:
                editor.placeBlock((x,y,z), Block("magenta_wool"))
            if arr_flip[z,x]==1286464:
                editor.placeBlock((x,y,z), Block("cyan_wool"))
            if arr_flip[z,x]==1920128:
                editor.placeBlock((x,y,z), Block("light_blue_wool"))
            if arr_flip[z,x]==1920192:
                editor.placeBlock((x,y,z), Block("white_wool"))
            if arr_flip[z,x]==1921280:
                editor.placeBlock((x,y,z), Block("terracotta"))
            if arr_flip[z,x]==1921920:
                editor.placeBlock((x,y,z), Block("white_terracotta"))
            if arr_flip[z,x]==1926464:
                editor.placeBlock((x,y,z), Block("yellow_terracotta"))
            if arr_flip[z,x]==12819264:
                editor.placeBlock((x,y,z), Block("green_terracotta"))
            if arr_flip[z,x]==19264192:
                editor.placeBlock((x,y,z), Block("blue_terracotta"))
            if arr_flip[z,x]==128128192:
                editor.placeBlock((x,y,z), Block("purple_terracotta"))
            if arr_flip[z,x]==6412864:
                editor.placeBlock((x,y,z), Block("brown_terracotta"))
            if arr_flip[z,x]==12864128:
                editor.placeBlock((x,y,z), Block("red_terracotta"))
            if arr_flip[z,x]==64128128:
                editor.placeBlock((x,y,z), Block("orange_terracotta"))
            if arr_flip[z,x]==128192128:
                editor.placeBlock((x,y,z), Block("light_blue_terracotta"))
            if arr_flip[z,x]==6419264:
                editor.placeBlock((x,y,z), Block("cyan_terracotta"))
            if arr_flip[z,x]==12864192:
                editor.placeBlock((x,y,z), Block("magenta_terracotta"))
            if arr_flip[z,x]==64128192:
                editor.placeBlock((x,y,z), Block("pink_terracotta"))
            if arr_flip[z,x]==128192192:
                editor.placeBlock((x,y,z), Block("gray_terracotta"))
            if arr_flip[z,x]==6464128:
                editor.placeBlock((x,y,z), Block("light_gray_terracotta"))
            if arr_flip[z,x]==19212864:
                editor.placeBlock((x,y,z), Block("lime_terracotta"))
            if arr_flip[z,x]==64192128:
                editor.placeBlock((x,y,z), Block("black_terracotta"))
            if arr_flip[z,x]==192128128:
                editor.placeBlock((x,y,z), Block("red_concrete"))
            if arr_flip[z,x]==6464192:
                editor.placeBlock((x,y,z), Block("orange_concrete"))
            if arr_flip[z,x]==19219264:
                editor.placeBlock((x,y,z), Block("yellow_concrete"))
            if arr_flip[z,x]==64192192:
                editor.placeBlock((x,y,z), Block("lime_concrete"))
            if arr_flip[z,x]==12812864:
                editor.placeBlock((x,y,z), Block("green_concrete"))
            if arr_flip[z,x]==192128192:
                editor.placeBlock((x,y,z), Block("light_blue_concrete"))
            if arr_flip[z,x]==19262128:
                editor.placeBlock((x,y,z), Block("pink_concrete"))
            if arr_flip[z,x]==128128128:
                editor.placeBlock((x,y,z), Block("magenta_concrete"))
            if arr_flip[z,x]==192192128:
                editor.placeBlock((x,y,z), Block("purple_concrete"))

