from tkinter import *

Nhapthongtin = Tk()

Nhapthongtin.geometry('1000x500+300+200')
Nhapthongtin.title('chuong trinh 1')


hoten = Entry(width= 20, font= 20)
hoten.grid(row= 0, column=1, sticky='ewsn')
xacnhan = Button(master= Nhapthongtin, text= 'Xac nhan', font=('arial', 14), fg= 'red')
xacnhan.grid(row=5, column=2)
sex = Radiobutton(master= Nhapthongtin, text= 'select', font=('arial',15))
sex.grid(row= 1, column=1)


Nhapthongtin.mainloop()