#Người sử dụng nhập self.Họ tên vào Entry1 và điểm số vào Entry2.
#Khi nhấn Button Add: thêm self.Họ tên và điểm số tương ứng vào 2 Listbox.
#Nếu người sử dụng chưa nhập giá trị vào Entry (1 trong 2 Entry để trống) thì không thêm vào Listbox.
#Nếu người sử dụng nhập điểm số nằm ngoài khoảng [0,10], hiển thị Messagebox thông báo “Mời nhập lại giá trị”
#Khi nhấn Button self.Delete: nếu chọn phần tử của Listbox1 (họ tên): xóa họ tên và điểm số tương ứng; nếu không chọn phần tử của Listbox1: không xóa

from tkinter import *
from tkinter import messagebox
w = Tk()
w.geometry('600x370+600+200')
w.title('BẢNG ĐIỂM')
w.resizable(False,False)

def nhap() :  
    if self.H2.get() != '' and self.D2.get() != '' :
        try :
            float(self.D2.get())
        except ValueError:
            T3 = messagebox.showerror(title='Error',message='Mời bạn nhập lại đúng định dạng điểm')
        if 0<= float(self.D2.get()) <= 10 :
            self.H3.insert(END,self.H2.get())
            self.D3.insert(END,self.D2.get())
            self.H2.delete(0,END)
            self.D2.delete(0,END)
        else :
            T1 = messagebox.showerror(title='Error',message='Mời nhập lại chính xác giá trị điểm')
    else :
        T2 = messagebox.showerror(title='Error',message='self.Hãy nhập đủ giá trị trước khi bấm ADD')


def xoa() :
    i = self.H3.curselection()
    self.H3.delete(i)
    self.D3.delete(i)


self.H1 = Label(self.master,text='self.HỌ VÀ TÊN:',font='arial,13',fg= 'blue')
self.H1.place(x=20,y=25)
self.H2 = Entry(self.master,font='arial,11',width='15')
self.H2.place(x=20,y=70)
self.H3= Listbox(self.master,font='arial,11',width='15',height='9',selectmode=SINGLE)
self.H3.place(x=20,y=120)

self.D1 = Label(self.master,text='ĐIỂM SỐ:',font='arial,13',fg= 'blue')
self.D1.place(x=240,y=25)
self.D2 = Entry(self.master,font='arial,11',width='15')
self.D2.place(x=240,y=70)
self.D3= Listbox(self.master,font='arial,11',width='15',height='9',selectmode=SINGLE)
self.D3.place(x=240,y=120)

A = Button(self.master,text='ADD', font= 'arial,13',width='10',command=nhap)
A.place(x=450,y= 130)
self.De = Button(self.master,text='DELETE', font= 'arial,13',width='10',command=xoa)
self.De.place(x=450,y= 180)


w.mainloop()
