#Người sử dụng nhập giá trị (số tự nhiên – hệ thập phân) vào.
#Khi nhấn Button Convert: tính giá trị số nhị phân tương ứng và hiển thị lên Label. 
#Nếu người sử dụng chưa nhập giá trị vào Entry thì lấy giá trị mặc định là 0
#Nếu người sử dụng nhập giá trị không phải số nguyên vào Entry, hiển thị MessageBox thông báo ‘Nhập sai định dạng giá trị’.


from tkinter import *
from tkinter import messagebox
from tkinter import font
w = Tk()
w.geometry('450x300+600+200')
w.title('BINARY CONVERSION')
w.resizable(False,False)

x = StringVar()
def tinhtoan(): 
    B.delete(0,END)      
    if D.get().isdigit() == False :
        T = messagebox.showerror(title='Thông báo',message= "Nhập sai định dạng giá trị!!")
    else :
        x = "{:b}".format(int(D.get()))
        B.insert(0,x)


D = Entry(self.master, font=18,width=13)
D.place(x=185,y=50 )
B = Entry(self.master, font=18,width=13,bg= 'white',fg= 'red')
B.place(x=185,y=90)
self.D1 = Label(self.master, text= 'DECIMAL :', font=('arial',15))
self.D1.place(x=60,y=50 )
B1 = Label(self.master, text= 'BINARY :', font=('arial',15))
B1.place(x=60,y=90)
C = Button(self.master,width=13, text= 'CONVERT', font= ('arial,16'), bg = 'blue', fg = 'white',command= tinhtoan)
C.place(x = 185, y= 140)

w.mainloop()
