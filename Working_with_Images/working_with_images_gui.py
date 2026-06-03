import os
from tkinter import *
import tkinter as tk
from tqdm import tqdm
import subprocess
from PIL import Image, ImageOps


default_font = "Courier"
src_path = "images"
dst_path = "new_images"

id = 1
isSuccessful = False

THUMBNAIL_AMT = (75, 75)
CROP_AMT = (20, 0, 220, 200)
ROTATION_DEG = -90

def edit_image():
    global src_path, dst_path, id, isSuccessful, THUMBNAIL_AMT, CROP_AMT, ROTATION_DEG
    try:
        original_images = sorted(os.listdir(src_path))
        for image in tqdm(original_images, desc="Finding and processing images"):
            
            if not image.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
                continue
            
            os.makedirs(dst_path, exist_ok=True)

            f, e = os.path.splitext(image)
            f = f"pic{str(id).zfill(4)}"
            id += 1
            newImage = f + ".png"
            
            src_file = os.path.join(src_path, image)
            dst_file = os.path.join(dst_path, newImage)
            
            try:
                with Image.open(src_file) as im:
                    im = im.crop(CROP_AMT)
                    im = im.rotate(ROTATION_DEG)
                    im.thumbnail(THUMBNAIL_AMT)
                    im = ImageOps.grayscale(im)
                    im.save(dst_file)
                    isSuccessful = True
            except OSError:
                print("Cannot convert", image)
        print("Finished")
        
        print("Opening folder location...")
        subprocess.Popen(f'explorer /select, "{os.getcwd()}\\{dst_path}\\"')
    except OSError:
        print("Edits were not successful")


def about_section():
    top = Toplevel()
    top.title("About")
    top.geometry('500x200+800-600')
    tk.Label(top, text="Application created by Daniel Trotter", font=(default_font, 15)).pack()
    tk.Label(top, text="© 2026 Daniel Trotter", font=(default_font, 10)).pack()



root = tk.Tk()
root.geometry('1000x600+500-400')
root.title("Simple Image Editor")

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)

menubar.add_cascade(label="File", menu=file_menu, underline=0)
file_menu.add_command(label="About", command=about_section)
file_menu.add_command(label="Exit", command=root.destroy)


convertBtn = tk.Button(root, text="Convert Images", command=edit_image)
convertBtn.pack()





tk.mainloop()