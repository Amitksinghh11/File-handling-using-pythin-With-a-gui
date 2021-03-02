
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import os
import shutil

# Starting of the interface
root = tk.Tk()

#change background
root.config(background = "white")


#title
root.title('Sweet Sort')

#icon
root.iconbitmap("icon.ico")

#logo
my_logo = Image.open("logo.png")
resized = my_logo.resize((600, 160), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(resized)
my_label = tk.Label(image = my_img)
my_label.grid(columnspan = 2, column=1, row=0)

#instruction
instruction = tk.Label(root, text = "Select a folder :", bg = "orange", font = "Arial 14 italic bold")
instruction.grid(column = 0, row=2, pady = 50)

#browse a file
def open_file():
    browse_text.set("Loading...")
    path = askdirectory()
    video = ("Video", "webm", "mov","avi","flv","mkv","wmv","mpeg","3gp","arf","asf","avi","m4v","mpg","rec","m4a","mp4")
    music = ("Music", "mp3","rec", "wav","aa","aa3","aiff","flac","ogg","wave","pcm","flp_")
    photo = ("Photos","jpeg", "png","ico", "bmp","gif","webp","tif","tiff","psd","raw","heif","jp2","j2k","jpf","jpg","jpm","mj2","ind", "indd", "indt","")
    doc  = ("Documents", "pdf", "xlsx", "rtf","pptx", "txt","doc","docx","html","htm","odt","xls","ods","ppt","srt")
    inst = ("Setup,Compressed files","exe", "rar", "zip", "msi")
    try:
        if path:
            os.chdir(path) #Change the current working dir to path
            source = os.walk(path)
            for path_name, dir_name, file_name in source:
                for files in file_name:
                    ext = files.split('.')
                    ext_len = len(ext)
                    extension = ext[ext_len - 1]
                    if extension in video:
                        if os.path.exists(video[0]):
                            shutil.move(files, video[0])
                        else:
                             os.makedirs(video[0])
                             shutil.move(files,video[0])
                    elif extension in music:
                        if os.path.exists(music[0]):
                            shutil.move(files, music[0])
                        else:
                            os.makedirs(music[0])
                            shutil.move(files,music[0])
                    elif extension in photo:
                        if os.path.exists(photo[0]):
                            shutil.move(files, photo[0])
                        else:
                            os.makedirs(photo[0])
                            shutil.move(files,photo[0])
                    elif extension in doc:
                        if os.path.exists(doc[0]):
                            shutil.move(files, doc[0])
                        else:
                            os.makedirs(doc[0])
                            shutil.move(files,doc[0])
                    elif extension in inst:
                        if os.path.exists(inst[0]):
                            shutil.move(files, inst[0])
                        else:
                            os.makedirs(inst[0])
                            shutil.move(files,inst[0])
                    else:
                        if os.path.exists(extension):
                            shutil.move(files, extension)
                        else:
                            os.makedirs(extension)
                            shutil.move(files,extension)
                browse_text.set("Your files looks sweet now..")
        else:
            browse_text.set("Browse")
    except (shutil.Error):
        browse_text.set("Your files are already sugar sweet")
    except Exception:
        browse_text.set("Try Again")

# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvar = browse_text, command = open_file ,padx = 250, bg = "orange", font = "Arial 11 bold")
browse_text.set("Browse")
browse_btn.grid(column = 1, row=2)

#exit button
exit_btn = tk.Button(root, text = "Exit", command = root.quit ,height= 1, width = 3, bg = "red", font = "Arial 11 bold")
exit_btn.grid(column = 1,row=3, pady = 10)

#credits
credit = tk.Label(root, text = "Made By Amit Kumar Singh", bg = "white", height = 1, width = 21, font = "Arial 14 italic bold")
credit.grid(column = 1, row= 4)

root.mainloop()
 