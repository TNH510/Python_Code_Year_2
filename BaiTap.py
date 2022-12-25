from tkinter import *
from tkinter import messagebox

class giaodien :
    def __init__(self,master_1):
        self.master = master_1
        self.H1 = Label(self.master,text='HỌ VÀ TÊN:',font='arial,13',fg= 'blue')
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
        self.A = Button(self.master,text='ADD', font= 'arial,13',width='10',command=self.nhap)
        self.A.place(x=450,y= 130)
        self.De = Button(self.master,text='DELETE', font= 'arial,13',width='10',command=self.xoa)
        self.De.place(x=450,y= 180)
        self.H1 = Label(self.master,text='HỌ VÀ TÊN:',font='arial,13',fg= 'blue')     
        
        self.menu_bar = Menu(master_1)
        self.master.configure(menu = self.menu_bar)
        self.Help = Menu(master = self.menu_bar, tearoff= False)
        self.menu_bar.add_cascade(label='Help',menu=self.Help)
        self.Help.add_command(label='About', command = self.about)


    def nhap(self) :  
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
            T2 = messagebox.showerror(title='Error',message='Hãy nhập đủ giá trị trước khi bấm ADD')

    def xoa(self) :
        i = self.H3.curselection()
        self.H3.delete(i)
        self.D3.delete(i)
    
    def about() :
        w2 = Toplevel()
        w2.geometry('500x500+100+200')
        w2.title('About')
        w2.resizable(False,False)
        app_1 = about(w2)


class about() :
    def __init__(self,master_2) :
        self.master = master_2
        self.H = Label(self.master, text='Bạn có điểm số cao nhất lớp là :')
        self.H.place(x=100,y=100)
        self.D = Label(self.master, text= 'Điểm trung bình của cả lớp là :')
        self.H.place(x=200,y=100)       

        

def main() :
    w = Tk()
    w.geometry('600x370+600+200')
    w.title('BẢNG ĐIỂM')
    w.resizable(False,False)
    app = giaodien(w)
    w.mainloop()

if __name__ == '__main__' :
    main()



