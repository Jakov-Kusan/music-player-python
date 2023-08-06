from playsound import playsound
import os



for i in range(100):
                print("\n")



while True:
    files = os.listdir()
    files.sort()

    for i in range(len(files)):
        if files[i][len(files[i])-4:] == ".mp3" or files[i][len(files[i])-4:] == ".wav" or files[i][len(files[i])-4:] == ".aac" or files[i][len(files[i])-4:] == ".wma":
            print("Playing:",files[i][:len(files[i])-4])
            print("Type:",files[i][len(files[i])-3:])

            try:
                playsound(files[i])
            except:
                print("Error: Courrupted File")

            for i in range(100):
                print("\n")
