import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = PIL.Image.open(file_path)
myWidth, myHeight = img.size

img=img.resize((myWidth, myHeight),PIL.Image.LANCZOS)
save_path = asksaveasfilename()

if save_path:
    img.save(save_path + ".jpg") 
