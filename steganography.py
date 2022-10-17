import os
from base64 import encode
from tkinter import *
from turtle import width
from stegano import lsbset
from stegano.lsbset import generators

message="hi"
def encrypt(message):
    root.destroy()
    filename = 'encode.py'
    os.system(filename)

    '''hide=lsbset.hide("C:\\Users\\aravi\\Desktop\\abc.png",message,generators.eratosthenes())
    hide.save("C:\\Users\\aravi\\Desktop\\abc11.png")'''
def decrypt():
    pass
    '''un_hide=lsbset.reveal("C:\\Users\\aravi\\Desktop\\abc11.png",generators.eratosthenes())
    print(un_hide)'''

root=Tk()
root.geometry("500x500")
root.title("Image hiding")

frame_1 = Frame(root)
frame_1.grid(row=0,column=0,padx=20,pady=50)

label_encode = Label(frame_1,text="ENCODE : ",font=("times",16,"bold"))
label_encode.grid(row=3,column=0,pady=40)
button_encode = Button(frame_1,width=30,height=5,text="Encode",command=encrypt(message),background="#6FEDD6")
button_encode.grid(row=3,column=1)

label_decode = Label(frame_1,text="DECODE : ",font=("times",16,"bold"))
label_decode.grid(row=4,column=0,pady=40)
button_decode = Button(frame_1,width=30,height=5,text="Decode",command=decrypt(),background="#781C68")
button_decode.grid(row=4,column=1)


root.mainloop()