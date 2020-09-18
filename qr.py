#pyqrcode pypng
import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox

main = Tk()
main.title("QR Generator")
main.geometry("250x400")
main.resizable(False,FALSE)
ic=ImageTk.PhotoImage(Image.open('img\\qr-code.png'))
main.iconphoto(FALSE,ic)

lo=Image.open('img\\qr.jpg')
ren=ImageTk.PhotoImage(lo)
Label(main,image=ren,bg='grey').place(x=-2.5,y=-2.5)


def exc():
    reset()
    # generate qr
    if len(t.get(1.0,'end-1c'))!=0 :
        global qr,photo
        qr = pyqrcode.create(t.get(1.0,'end-1c'))
        photo = BitmapImage(data = qr.xbm(scale=2))
    else:
        messagebox.showinfo("Please Enter some Subject")
    try:
        showcode()
    except:
        pass
    
file_path=''
def dirt():
    global file_path
    file_path = filedialog.askdirectory()
    
def showcode():
    imageLabel = Label(labelframe)
    imageLabel.pack(anchor=CENTER)
    imageLabel.config(image = photo)

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def reset():
    widget_list = all_children(labelframe)
    for item in widget_list:
        item.pack_forget()

def save():
    # saving
    try:
        if len(t1.get(1.0,'end-1c'))!=0:
            qr.png(file_path+'//'+t1.get(1.0,'end-1c')+'.png',scale=8)
        else:
            messagebox.showinfo("Please enter a File Name")
    except:
        messagebox.showinfo("Generate the QR code first!")

Label(main, text="QRCode Generator",bg='black',fg='white').pack(pady=2)

t = Text(main, height = 2, width = 20,bg='aquamarine',fg='grey36')
t.pack(pady=2)

btn = Button(main, text = "Generate", 
            command = lambda: exc())
btn.pack(pady=2)

labelframe = LabelFrame(main,bg='black',fg='white',height=200,width=200)
labelframe.pack_propagate(False)
labelframe.pack()


btn0 = Button(main, text = "Browse Directory", 
            command = lambda: dirt())
btn0.pack(pady=2)

t1 = Text(main, height = 2, width = 20,bg='aquamarine',fg='grey36')
t1.pack(pady=2)

btn1 = Button(main, text = "Save as Png", 
            command = lambda: save())
btn1.pack(pady=2)

main.mainloop()
