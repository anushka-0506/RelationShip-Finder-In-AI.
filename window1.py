from tkinter import *
from tkinter.ttk import*
from gtts import gTTS 
from playsound import playsound
import tkinter as tk
import os 

window = tk.Tk()
window.configure(bg="black")
window.geometry('1950x1900')
playsound('voice.mp3')
def delete_Relation():
    q="Hello . "
    t="     .  Now Please click on close button."
    k=variable.get()
    if k =="Male":w ="MR. "
    elif k=="Female":w="MRs. "
    p=texts.get()
    mytext = q +w+p+t
    language = 'en'
    myobj = gTTS(text=mytext, lang=language) 
    myobj.save("welcome.mp3") 
    playsound('welcome.mp3')
l1 = Label(window, text=" P  ",font= ('helvetica',40,'bold'), background="black")
l1.grid(row=1,column=1,padx=20)
img = PhotoImage(file='oo4.png')  
ll=Label(image=img)
ll.grid(row=1,column=2)


l1 = Label(window, text=" P  ",font= ('helvetica',50,'bold'), background="black")
l1.grid(row=3,column=0,padx=20)
texts = StringVar()
e1 = Entry(window, textvariable= texts,)
e1.grid(row=11, column=2)
OptionList = ["Male",
"Female",
]
variable = tk.StringVar(window)
variable.set(OptionList[0])

opt = tk.OptionMenu(window, variable, *OptionList)
opt.config(width=20, font=('Helvetica', 12))
opt.grid(row=11,column=1)
b5 =Button(window, text= "Enter", width=40,compound = LEFT,command=delete_Relation)
b5.grid(row=12, column=2)
l1 = Label(window, text=" P  ",font= ('helvetica',40,'bold'), background="black")
l1.grid(row=13,column=1,padx=20)
b6 =Button(window, text= "Close", width=40, compound = LEFT, command=window.destroy)
b6.grid(row=14, column=2)
window.mainloop()