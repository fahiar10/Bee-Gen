from tkinter import *
from tkinter.ttk import Progressbar
from imagecapture import captureimg
from PIL import Image, ImageTk
import os
from inference import infer, init_api
import shutil
import time


def show_images():
    os.startfile("C:/Users/Lenovo/Desktop/Code/FY Proj/gui/images")

def start(loadwin,bar,percent,text):
    model = init_api()
    path = "C:/Users/Lenovo/Desktop/Code/FY Proj/gui/images"
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.jpg'):
                infer(dirpath, filename, model)
                # time.sleep(1)
                ifilename = filenames.index(filename)
                print(str(ifilename + 1) + " " + str(len(filenames)))
                c = int((ifilename + 1) / len(filenames) * 100)
                print(c)
                bar['value'] = c
                percent.set(str(int(ifilename + 1) / len(filenames) * 100) + "%")
                text.set(str(ifilename + 1) + "/" + str(len(filenames)) + " Images completed")
                loadwin.update_idletasks()

def inferimg():
    loadwin = Tk()
    bar = Progressbar(loadwin,orient=HORIZONTAL,length=300)
    bar.pack()
    percent = StringVar()
    text = StringVar()
    percentLabel = Label(loadwin, textvariable=percent).pack()
    taskLabel = Label(loadwin, textvariable=text).pack()

    button = Button(loadwin, text="Start", command=lambda: start(loadwin,bar,percent,text)).pack()
    loadwin.mainloop()

def menuoptions(window):
    frame = Frame(window, bg="orange", bd=5, relief=RAISED)
    frame.pack()

    button1 = Button(frame,
                     text="Capture Image",
                     # command=click,
                     fg="red",
                     bg="orange",
                     activeforeground="red",
                     activebackground="orange",
                     state=ACTIVE,
                     command=captureimg)
    button1.pack(side=TOP)
    button2 = Button(frame,
                     text="Inference",
                     command=inferimg,
                     fg="red",
                     bg="orange",
                     activeforeground="red",
                     activebackground="orange",
                     state=ACTIVE)
    button2.pack(side=LEFT)
    button3 = Button(frame,
                     text="Options",
                     #command=click,
                     fg="red",
                     bg="orange",
                     activeforeground="red",
                     activebackground="orange",
                     state=ACTIVE)
    button3.pack(side=LEFT)
    button4 = Button(frame,
                     text="Show Images",
                     command=show_images,
                     fg="red",
                     bg="orange",
                     activeforeground="red",
                     activebackground="orange",
                     state=ACTIVE)
    button4.pack(side=LEFT)



def mainapp():
    window = Tk()
    window.geometry("420x420")
    window.title("Bee-Gen")
    # icon = PhotoImage(file='logo.png')
    # window.iconphoto(True,icon)
    window.config(background="#FFCE30")
    label = Label(window,
                  text="BEE-GEN",
                  font=('Arial', 40, 'bold'),
                  fg='black',
                  bg='orange',
                  relief=RAISED,
                  bd=10,
                  padx=20,
                  pady=20,
                  # image=photo,
                  # compound='bottom'
                  )
    # label.place(x=100,y=100)
    label.pack()
    menuoptions(window)


    window.mainloop()


if __name__ == '__main__':
    print('PyCharm')
    mainapp()