from tkinter import *
from PIL import *

Nhapthongtin = Tk()

Nhapthongtin.geometry('800x300+700+200')

T1 = Label(text='self.Họ và tên :', font= ('arial',15))
T1.grid(row=0, column=0)
T2 = Entry( width= 30, font= 20, fg= 'red')
T2.grid(row=1, column=0)
T3 = Label(text='Tuổi :', font= ('arial',15))
T3.grid(row=2, column=0)
T4 = Entry( width= 30, font= 20, fg= 'red')
T4.grid(row=3, column=0)

self.H5 = Label(master= Nhapthongtin,image= 'hcmute.png')
self.H5.grid(row=1, column=2)

Nhapthongtin.mainloop()