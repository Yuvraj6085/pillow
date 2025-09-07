from tkinter import *
from tkinter import filedialog as fd 
import os 
from PIL import Image 
from tkinter import messagebox 

root = Tk() 
root.title("Image_Conversion_App") 

# Function: GIF -> BMP
def gif_to_bmp():
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".gif"):
        im = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension=".bmp")
        im.save(export_filename)
        messagebox.showinfo("Success", "File converted to .bmp")
    else:
        messagebox.showerror("Fail!!", "Please select a .gif file")

# Function: BMP -> GIF
def bmp_to_gif():
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".bmp"):
        im = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension=".gif")
        im.save(export_filename)
        messagebox.showinfo("Success", "File converted to .gif")
    else:
        messagebox.showerror("Fail!!", "Please select a .bmp file")

# Function: JPG -> PNG
def jpg_to_png():
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".jpg") or import_filename.endswith(".jpeg"):
        im = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension=".png")
        im.save(export_filename)
        messagebox.showinfo("Success", "File converted to .png")
    else:
        messagebox.showerror("Fail!!", "Please select a .jpg file")

# Buttons
button1 = Button(root, text="GIF_to_BMP",
                 width=20, height=2, 
                 bg="green", fg="white", 
                 font=("helvetica", 12, "bold"), 
                 command=gif_to_bmp) 
button1.place(x=120, y=100) 

button2 = Button(root, text="BMP_to_GIF",
                 width=20, height=2, 
                 bg="green", fg="white", 
                 font=("helvetica", 12, "bold"), 
                 command=bmp_to_gif) 
button2.place(x=120, y=180) 

button3 = Button(root, text="JPG_to_PNG",
                 width=20, height=2, 
                 bg="blue", fg="white", 
                 font=("helvetica", 12, "bold"), 
                 command=jpg_to_png) 
button3.place(x=120, y=260) 

# Window size and position
root.geometry("500x500+400+200") 
root.mainloop()
