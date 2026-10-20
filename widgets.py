from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window= Tk()
window.title("My photo album")
window.geometry('400x420')


title=Label(window, text='my photo album', bg='purple', fg='white', width=40)
title.pack(pady=10)
img_file=Image.open('cat.jpg')
img_file=img_file.resize((300,180))
photo=ImageTk.PhotoImage(img_file)

pic=Label(window,image=photo)
pic.pack(pady=5)

def show_message():
    messagebox.showinfo('great, you clicked the photo')
msg_btn =Button(window, text='click to react', bg='blue', fg='white', command=show_message)
msg_btn.pack(pady=5)



def show_details():
    top=Toplevel()
    top.title('photo details')
    top.geometry('200x100')
    info=Label(top, text='taken on :1 june 2026')
    info.pack(pady=10)

    place=Label(top, text='Location:My garden')
    place.pack(pady=10)

    top.mainloop()

details_btn=Button(window,text='see details', bg='green', fg='white', command= show_details)
details_btn.pack(pady=5)

window.mainloop()


