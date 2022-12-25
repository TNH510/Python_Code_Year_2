#Thêm Menu File: bao gồm 3 tùy chọn Stats, self.Delete All và Exit
#Khi nhấn Stats: hiển thị Giá trị điểm trung bình lên Messagebox (info messagebox)
#Khi nhấn self.Delete All: hiển thị MessageBox xác nhận (Yes/No) – Nếu người sử dụng chọn Yes: xóa toàn bộ 2 Listbox, nếu chọn No: không xóa
#Khi nhấn Exit: thoát chương trình

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
    x = self.H3.curselection()
    self.H3.delete(x)
    self.D3.delete(x)

def stats() :
    if self.D3.size() == 0 :
        T4 = messagebox.showerror(title='Error',message='Danh sách điểm trống!!')
    x = self.D3.curselection()
    Tong = 0
    for i in range(0,int(self.D3.size())) :        
        Tong = Tong + float(self.D3.get(i))
    t = Tong/float(self.D3.size())
    K1 = messagebox.showinfo(title='Điểm trung bình', message= 'Điểm trung bình : {}'.format(t))

def deleteall() :
    K2 = messagebox.askyesno(title='Cảnh báo', message= 'Bạn có muốn xóa tất cả không ?')
    if K2 == 1 :
        self.H3.delete(0,END)
        self.D3.delete(0,END)


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

M = Menu(self.master)
w.configure(menu= M)

M_File = Menu(master=M,tearoff= False)
M.add_cascade(label= 'File',menu= M_File )

M_File.add_command(label= 'Stats',command=stats)
M_File.add_command(label= 'self.Delete All', command=deleteall)
M_File.add_command(label= 'Exit',command= lambda :w.destroy() )

w.mainloop()
