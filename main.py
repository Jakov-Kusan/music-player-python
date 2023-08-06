from playsound import playsound
from tkinter import filedialog
from tkinter import *
import os




for i in range(100):
                print("\n")


#Checking if linux or windows
if os.name == 'nt':
    slash = "\ "
    slash = slash[0]
else:
      slash = "/"


while True:
    #Asking for directory
    path= filedialog.askdirectory()

    #Making array of all files in directory
    files = os.listdir(path)
    files.sort()

    for i in range(len(files)):
        #Checking if file is a sound file 
        if files[i][len(files[i])-4:] == ".mp3" or files[i][len(files[i])-4:] == ".wav" or files[i][len(files[i])-4:] == ".aac" or files[i][len(files[i])-4:] == ".wma":
            print("Playing:",files[i][:len(files[i])-4])
            print("Type:",files[i][len(files[i])-3:])

            try:
                playsound(path+slash+files[i])
            except:
                print("Error: Courrupted File")

            for i in range(100):
                print("\n")
