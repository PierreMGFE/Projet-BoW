import tkinter as tk
#import files_names as fn
from tkinter import filedialog

# ======== Select a directory:
root = tk.Tk("1000","1000","1000","1000")
root.title("WBO Bag of Words predictions")

tk.Button(root, text="").grid()

root.mainloop()

root = tk.Tk()
# dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
# if len(dirname ) > 0:
#     print("You chose "+str(dirname))

# fp = fn.filepaths(dirname)
#
# filenames = []
#
# for files, path in fp:
#     if path.find('.pdf.txt') != -1:
#         filenames.append(path)



        # # ======== Select a file for opening:
#
# root = tk.Tk()
# file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
# if file != None:
#     data = file.read()
#     file.close()
#     print("I got "+str(len(data))+" bytes from this file.")
#
#
# # ======== "Save as" dialog:
#
# myFormats = [
#     ('Windows Bitmap','*.bmp'),
#     ('Portable Network Graphics','*.png'),
#     ('JPEG / JFIF','*.jpg'),
#     ('CompuServer GIF','*.gif'),
#     ]
#
# root = tk.Tk()
# fileName = filedialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the image as...")
# if len(fileName ) > 0:
#     print("Now saving under "+str(fileName))


# voir http://code.activestate.com/recipes/438123/