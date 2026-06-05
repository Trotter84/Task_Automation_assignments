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

LOWER_BOUND = 50
UPPER_BOUND = 250

thumbnail_amt = (75, 75)
CROP_AMT = (20, 0, 220, 200)
ROTATION_DEG = -90


# ************************* Original Script ************************* 
def edit_image():
    global src_path, dst_path, id, isSuccessful, thumbnail_amt, CROP_AMT, ROTATION_DEG
    try:
        original_images = sorted(os.listdir(src_path))
        for image in tqdm(original_images, desc="Finding and processing images"):
            
            if not image.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
                continue
            
            if folderEntry.get():
                dst_path = folderEntry.get()
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
                    im.thumbnail(thumbnail_amt)
                    if var_gry.get() == 1:
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
# ^^^^^^^^^^^^^^^^^^^^^^^^^ Original Script ^^^^^^^^^^^^^^^^^^^^^^^^^ 


def about_section():
    top = Toplevel()
    top.title("About")
    top.geometry('500x200+800-600')
    tk.Label(top, text="Application created by Daniel Trotter", font=(default_font, 15)).grid()
    tk.Label(top, text="© 2026 Daniel Trotter", font=(default_font, 10)).grid()


def slider_handler(value):
    global thumbnail_amt
    thumbnail_amt = (int(value), int(value))


root = tk.Tk()
root.geometry('500x300+500-400')
root.title("Simple Image Editor")

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)

menubar.add_cascade(label="File", menu=file_menu, underline=0)
file_menu.add_command(label="About", command=about_section)
file_menu.add_command(label="Exit", command=root.destroy)


# ************************* Layout Section ************************* 
titleLbl = tk.Label(root, text="Basic Image Editor", fg="darkred", font=(default_font, 30, "bold"), borderwidth=1, relief="solid")
titleLbl.grid(row=0, column=0, rowspan=1, columnspan=4)

thumbnailLbl = tk.Label(root, text="Thumbnail Size:", font=(default_font, 15))
thumbnailLbl.grid(row=1, column=0, rowspan=1, columnspan=2)
horizontalScale = Scale(root, from_=LOWER_BOUND, to=UPPER_BOUND, orient=HORIZONTAL, command=slider_handler)
horizontalScale.grid(row=1, column=2, rowspan=1, columnspan=2)

var_gry = tk.IntVar()
grysclChckbx = tk.Checkbutton(root, text="Grayscale", variable=var_gry)
grysclChckbx.grid(row=2, column=0, rowspan=1, columnspan=4)

folderLbl = tk.Label(root, text="Folder Name:", font=(default_font, 15))
folderLbl.grid(row=3, column=0, rowspan=1, columnspan=2)

folderEntry = tk.Entry(root)
folderEntry.grid(row=3, column=2, rowspan=1, columnspan=2)

convertBtn = tk.Button(root, text="Convert Images", command=edit_image)
convertBtn.grid(row=4, column=0, rowspan=1, columnspan=4)

# ^^^^^^^^^^^^^^^^^^^^^^^^^ Layout Section ^^^^^^^^^^^^^^^^^^^^^^^^^ 

tk.mainloop()