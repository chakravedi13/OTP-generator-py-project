import random
from tkinter import *
import tkinter 
from tkinter import PhotoImage



window = Tk()
window.title('TechDC-OTP_Generator')
window.geometry('925x500+300+200')
logo = PhotoImage(file = "icon.png")
window.iconphoto(False, logo)
window.resizable(width=False, height=False)
window.configure(bg='white')



Label(window,font=('bold',30),text='OTP GENERATOR',bg='white',fg='black').pack()

img = PhotoImage(file='otp-banner-image.png')
Label(window,image=img,bg='white').place(x=50,y=50)

#frame1=Frame(window,width=410,height=390,bg='#f5f6fa')
#frame1.place(x=485,y=95)
frame=Frame(window,width=390,height=370,bg='white')
frame.place(x=490,y=100)





len=tkinter.IntVar()


def password_generate(leng):
    valid_char='0123456789'
    #ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$*
    password=''.join(random.sample(valid_char,leng))
    code = Label(frame,width=15,text = password,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',20,'bold'))
    code.place(x=70,y=80)
    
    #l =Label(window, text = password, font=('bold', 20),bg='white',fg='black',) 
    #l.place(x=150,y=150)
    print('OTP ',password)

def get_len():
    if len.get() == 4:
        password_generate(4)
    elif len.get() == 6:
        password_generate(6)
    elif len.get() == 8:
        password_generate(8)
    else:
        password_generate(6)    

Frame(frame,width=280,height=2,bg='black').place(x=60,y=150)


Button(frame,width=15,pady=5,fg='black', text='Generate', bg='#57a1f8', border=0,font=12, command=get_len).place(x=110,y=190)
 
Label(frame,font=('normal',14),text='Please choose length of OTP',fg='black',bg='white').place(x=70,y=250) 
Radiobutton(frame,text='4 Length',value=4,variable=len,font=('normal',12),fg='black',bg='white').place(x=150,y=280)
Radiobutton(frame,text='6 Length',value=6,variable=len,font=('normal',12),fg='black',bg='white').place(x=150,y=310)
Radiobutton(frame,text='8 Length',value=8, variable=len,font=('normal',12),fg='black',bg='white').place(x=150,y=340)


window.mainloop()