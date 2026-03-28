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
img = Image.open("maps/geologic_map_from_data.png")
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
        if (np.array_equal(arr[x,y],[  0, 166, 166])
        or np.array_equal(arr[x,y],[  0, 238, 238])
        or np.array_equal(arr[x,y],[  0,  64,   0])
        or np.array_equal(arr[x,y],[  0,  64, 128])
        or np.array_equal(arr[x,y],[101, 229, 101])
        or np.array_equal(arr[x,y],[112, 124, 109])
        or np.array_equal(arr[x,y],[116,  85,  75])
        or np.array_equal(arr[x,y],[119, 119, 255])
        or np.array_equal(arr[x,y],[125, 125, 125])
        or np.array_equal(arr[x,y],[135, 140, 160])
        or np.array_equal(arr[x,y],[152, 183, 106])
        or np.array_equal(arr[x,y],[155, 124, 100])
        or np.array_equal(arr[x,y],[168, 136,  87])
        or np.array_equal(arr[x,y],[172, 203, 141])
        or np.array_equal(arr[x,y],[176, 164, 140])
        or np.array_equal(arr[x,y],[177, 158,  92])
        or np.array_equal(arr[x,y],[186, 130, 118])
        or np.array_equal(arr[x,y],[186, 165, 150])
        or np.array_equal(arr[x,y],[187, 125, 160])
        or np.array_equal(arr[x,y],[188, 121, 255])
        or np.array_equal(arr[x,y],[194, 194, 194])
        or np.array_equal(arr[x,y],[202, 184, 166])
        or np.array_equal(arr[x,y],[206, 187, 170])
        or np.array_equal(arr[x,y],[209, 202, 156])
        or np.array_equal(arr[x,y],[210,  45, 186])
        or np.array_equal(arr[x,y],[219, 165, 104])
        or np.array_equal(arr[x,y],[219, 181, 100])
        or np.array_equal(arr[x,y],[221,  68, 137])
        or np.array_equal(arr[x,y],[222,  89,  33])
        or np.array_equal(arr[x,y],[224, 210, 163])
        or np.array_equal(arr[x,y],[229, 101, 101])
        or np.array_equal(arr[x,y],[229, 127,   0])
        or np.array_equal(arr[x,y],[230, 205, 132])
        or np.array_equal(arr[x,y],[230, 205, 142])
        or np.array_equal(arr[x,y],[230,  91, 182])
        or np.array_equal(arr[x,y],[238, 119,   0])
        or np.array_equal(arr[x,y],[247, 136, 169])
        or np.array_equal(arr[x,y],[255,   0, 255])
        or np.array_equal(arr[x,y],[255,   0,  50])
        or np.array_equal(arr[x,y],[255, 128,   0])
        or np.array_equal(arr[x,y],[255, 128, 192])
        or np.array_equal(arr[x,y],[255, 153,  50])
        or np.array_equal(arr[x,y],[255, 229, 255])
        or np.array_equal(arr[x,y],[255, 255,   0])
        or np.array_equal(arr[x,y],[255,  50, 204])
        or np.array_equal(arr[x,y],[  6, 128, 249])
        or np.array_equal(arr[x,y],[ 62, 128, 128])
        or np.array_equal(arr[x,y],[ 71, 173,  86])
        or np.array_equal(arr[x,y],[ 83, 193, 193])
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

for x in range (0,1153):
    for z in range(0,852):
        for y in range(0, heightmap[x,z]):
            if arr_rgb[z,x]==255255255:
                if heightmap[x,z]==64:
                    editor.placeBlock((x,heightmap[x,z]-1,z), Block("water"))
                else:
                    editor.placeBlock((x,heightmap[x,z]-2,z), Block("water"))
                    editor.placeBlock((x,heightmap[x,z]-1,z), Block("air"))

#place blocks according to map array
for x in range (0,1153):
    for z in range(0,852):
        for y in range(0, heightmap[x,z]):
            if arr_rgb[z,x]==640:
                editor.placeBlock((x,y,z), Block("blackstone"))
            if arr_rgb[z,x]==64128:
                editor.placeBlock((x,y,z), Block("stone"))
            if arr_rgb[z,x]==166166:
                editor.placeBlock((x,y,z), Block("blackstone"))
            if arr_rgb[z,x]==238238:
                editor.placeBlock((x,y,z), Block("calcite"))
            if arr_rgb[z,x]==255050:
                editor.placeBlock((x,y,z), Block("granite"))
            if arr_rgb[z,x]==1168575:
                editor.placeBlock((x,y,z), Block("stone"))
            if arr_rgb[z,x]==2228933:
                editor.placeBlock((x,y,z), Block("granite"))
            if arr_rgb[z,x]==2381190:
                editor.placeBlock((x,y,z), Block("sandstone"))
            if arr_rgb[z,x]==2550255:
                editor.placeBlock((x,y,z), Block("granite"))
            if arr_rgb[z,x]==2551280:
                editor.placeBlock((x,y,z), Block("stone"))
            if arr_rgb[z,x]==2552550:
                editor.placeBlock((x,y,z), Block("andesite"))
            if arr_rgb[z,x]==6128249:
                editor.placeBlock((x,y,z), Block("stone"))
            if arr_rgb[z,x]==7117386:
                editor.placeBlock((x,y,z), Block("blackstone"))
            if arr_rgb[z,x]==16813687:
                editor.placeBlock((x,y,z), Block("packed_mud"))
            if arr_rgb[z,x]==17715892:
                editor.placeBlock((x,y,z), Block("tuff"))
            if arr_rgb[z,x]==21045186:
                editor.placeBlock((x,y,z), Block("blackstone"))
            if arr_rgb[z,x]==22168137:
                editor.placeBlock((x,y,z), Block("granite"))
            if arr_rgb[z,x]==23091182:
                editor.placeBlock((x,y,z), Block("granite"))
            if arr_rgb[z,x]==62128128:
                editor.placeBlock((x,y,z), Block("blackstone"))
            if arr_rgb[z,x]==83193193:
                editor.placeBlock((x,y,z), Block("stone"))
            if arr_rgb[z,x]==112124109:
                editor.placeBlock((x,y,z), Block("light_gray_glazed_terracotta"))
            if arr_rgb[z,x]==119119255:
                editor.placeBlock((x,y,z), Block("calcite"))
            if arr_rgb[z,x]==125125125:
                editor.placeBlock((x,y,z), Block("sandstone"))
            if arr_rgb[z,x]==135140160:
                editor.placeBlock((x,y,z), Block("sandstone"))
            if arr_rgb[z,x]==152183106:
                editor.placeBlock((x,y,z), Block("andesite"))
            if arr_rgb[z,x]==155124100:
                editor.placeBlock((x,y,z), Block("sandstone"))
            if arr_rgb[z,x]==172203141:
                editor.placeBlock((x,y,z), Block("andesite"))
            if arr_rgb[z,x]==176164140:
                editor.placeBlock((x,y,z), Block("cobblestone"))
            if arr_rgb[z,x]==186130118:
                editor.placeBlock((x,y,z), Block("packed_mud"))
            if arr_rgb[z,x]==186165150:
                editor.placeBlock((x,y,z), Block("sandstone"))
            if arr_rgb[z,x]==187125160:
                editor.placeBlock((x,y,z), Block("blackstone"))
            if arr_rgb[z,x]==188121255:
                editor.placeBlock((x,y,z), Block("sandstone"))
            if arr_rgb[z,x]==194194194:
                editor.placeBlock((x,y,z), Block("stone"))
            if arr_rgb[z,x]==202184166:
                editor.placeBlock((x,y,z), Block("stone"))
            if arr_rgb[z,x]==206187170:
                editor.placeBlock((x,y,z), Block("sandstone"))
            if arr_rgb[z,x]==209202156:
                editor.placeBlock((x,y,z), Block("andesite"))
            if arr_rgb[z,x]==219165104:
                editor.placeBlock((x,y,z), Block("cobblestone"))
            if arr_rgb[z,x]==219181100:
                editor.placeBlock((x,y,z), Block("cobblestone"))
            if arr_rgb[z,x]==224210163:
                editor.placeBlock((x,y,z), Block("light_gray_glazed_terracotta"))
            if arr_rgb[z,x]==230205132:
                editor.placeBlock((x,y,z), Block("light_gray_glazed_terracotta"))
            if arr_rgb[z,x]==230205142:
                editor.placeBlock((x,y,z), Block("sandstone"))
            if arr_rgb[z,x]==247136169:
                editor.placeBlock((x,y,z), Block("granite"))
            if arr_rgb[z,x]==255128192:
                editor.placeBlock((x,y,z), Block("granite"))
            if arr_rgb[z,x]==255229255:
                editor.placeBlock((x,y,z), Block("stone"))
            

