import tkinter as tk
from tkinter import *
#from tkinter.ttk import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root=Tk()
root.title("Sarath Project")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#305065")


engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_dropdown.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()

        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if (text):
        if(speed =="Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate',120)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

            

            
def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_dropdown.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(Text,'text.mp3')
            engine.runAndWait()
            
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(Text,'text.mp3')
            engine.runAndWait()
        if (text):
            if(speed =="Fast"):
                engine.setProperty('rate', 250)
                setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate',120)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def quit():
    root.destroy()


#for title icon .sk
image_icon=PhotoImage(file="title img.png")
root.iconphoto(False,image_icon)


#top frame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)


#main logo
Logo=PhotoImage(file="speaker logo.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)


Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)


#text box
text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)


#title of dropdown
Label(root,text="VOICE",font="arial 15 bold" ,bg="#305065",fg="white").place(x=575,y=160)
Label(root,text="SPEED",font="arial 15 bold" ,bg="#305065",fg="white").place(x=760,y=160)


#Dropdown 1
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 13",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Choose')


#Dropdown 2
speed_dropdown=Combobox(root,values=['Fast','Normal','Slow'],font="arial 13",state='r',width=10)
speed_dropdown.place(x=730,y=200)
speed_dropdown.set('Select')


imageicon=PhotoImage(file="speak.png")
btn=Button(root,text=" speak ",compound=LEFT,image=imageicon,font="arial 13 bold",command=speaknow)
btn.place(x=550,y=280)

imageicon1=PhotoImage(file="download.png")
save=Button(root,text=" Save ",compound=LEFT,image=imageicon1,bg="#39c790",font="arial 13 bold",command=download)
save.place(x=730,y=280)

close=Button(root,text=" Exit ",compound=LEFT,bg="#39c790",font="arial 13 bold",command=quit)
close.place(x=672,y=370)


root.mainloop()
