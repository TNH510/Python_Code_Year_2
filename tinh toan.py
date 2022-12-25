from tkinter import *

tinhtoan = Tk()
tinhtoan.title('chương trình tính toán')
tinhtoan.iconbitmap('abc.ico')
tinhtoan.geometry('800x400+650+150')

tongtien = IntVar()
my = IntVar()
com = IntVar()
pho = IntVar()

def tinhtien() :
    tongtien = my.get() + com.get() + pho.get() 
    L1.configure(text= 'Tong tien :' + str(tongtien))

C1 = Radiobutton(variable= my,value= 50000 ,text= ('Mỳ tôm :50.000'), font= ('arial', 20))
C1.grid(row=0, column=0, pady=30 , sticky='w')
C2 = Radiobutton(variable= com,value= 30000,text= ('Cơm hộp  :30.000'), font= ('arial', 20))
C2.grid(row=1, column=0, pady= 10 , sticky='w')
C3 = Radiobutton(variable= pho,value= 80000,text= ('Phở :80.000'), font= ('arial', 20))
C3.grid(row=2, column=0, pady=30 , sticky='w')

B1 = Button(text='OK', font=('arial', 20), command= tinhtien)
B1.grid(row=1, column=1, padx=50, sticky='ewsn')

L1 = Label(text=('Tong tien :'), font=('arial', 20, 'bold'), fg = 'green')
L1.grid(row=2, column=1, padx=50, sticky='ewsn')





tinhtoan.mainloop()