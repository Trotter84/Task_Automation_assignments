import os, sys
from PIL import Image


src_path = "images_old"
dst_path = "images_new"

os.makedirs(dst_path, exist_ok=True)

for image in os.listdir(src_path):
    f, e = os.path.splitext(image)
    newImage = f + ".png"
    
    src_file = os.path.join(src_path, image)
    dst_file = os.path.join(dst_path, newImage)
    
    try:
        with Image.open(src_file) as im:
            im.save(dst_file)
    except OSError:
        print("Cannot convert", image)


    
#******************************   TASKS   ******************************#
# In one pass (a single loop over the files), do all of the following to each image:

#✅     Convert from jpg to png format

#     Crop the edges to be a square (height and width should match)

#     Rotate so the faces of the people are oriented correctly, there should be no black edges showing

#     Make the new thumbnails size 75x75 pixels

#     Convert to gray scales

#     Save the results in a directory called 'new_images' at the same directory level as 'images'

#     Rename the files to be sequentially numbered with a prefix of 'pic' and always having four digits (e.g. pic0001.png, pic0002.png, ... pic0010.png, ... pic0284.png)
