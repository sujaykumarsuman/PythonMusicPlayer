import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer

root = Tk()
mixer.init(buffer=1)

menubar = Menu(root)
root.configure(menu=menubar)

SubMenu = Menu(menubar, tearoff=0)


def browse_file():
    global file
    file = filedialog.askopenfilename()
    mixer.music.load(file)
    status['text'] = f"Loaded file: {os.path.basename(file)}"


menubar.add_cascade(label="File", menu=SubMenu)
SubMenu.add_command(label="Open", command=browse_file)
SubMenu.add_command(label="Exit", command=root.quit)


def about_us():
    project_credit = "tkinter/pygame learning project\nProject by @buildwithpython on YouTube"
    tkinter.messagebox.showinfo('About', project_credit)


SubMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=SubMenu)
SubMenu.add_command(label="About", command=about_us)

root.title("Music")
root.geometry("300x200")
root.iconbitmap(r"res/icons/music.ico")
text = Label(root, text="Let's play some music!\n")
text.pack(padx=15, pady=10)

paused = False


def play_btn():
    if not paused:
        try:
            mixer.music.play()
            status['text'] = f"Playing: {os.path.basename(file)}"
        except:
            tkinter.messagebox.showerror("File not found", "File could not be loaded! Please load a file and try again.")
    else:
        mixer.music.unpause()
        status['text'] = f"Playing: {os.path.basename(file)}"


def pause_btn():
    global paused
    paused = True
    mixer.music.pause()
    status['text'] = f"Music Paused"


def stop_btn():
    mixer.music.stop()
    status['text'] = f"Stopped Music"
    global paused
    paused = False


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)


controls_frame = Frame(root)
controls_frame.pack()

play_img = PhotoImage(file="res/icons/play.png")
play = Button(controls_frame, image=play_img, command=play_btn)
play.grid(row=0, column=0, padx=10)

stop_img = PhotoImage(file="res/icons/stop.png")
stop = Button(controls_frame, image=stop_img, command=stop_btn)
stop.grid(row=0, column=1, padx=10)

pause_img = PhotoImage(file="res/icons/pause.png")
pause = Button(controls_frame, image=pause_img, command=pause_btn)
pause.grid(row=0, column=2, padx=10)

slider = Scale(root, from_=0, to=100, command=set_vol, orient=HORIZONTAL)
slider.set(65)
set_vol(65)
slider.pack(pady=15)

status = Label(root, text="Welcome to the world of Music!", anchor=W, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
