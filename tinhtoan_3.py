from tkinter import *

tinhtoan = Tk()
tinhtoan.title('chương trình tính toán')
tinhtoan.iconbitmap('abc.ico')
tinhtoan.geometry('800x400+650+150')

tongtien = IntVar()
my = IntVar()
com = IntVar()
pho = IntVar()
F1 = Frame(master= tinhtoan)
F1.place(x =150, y= 150)

A = ['Phở : 50.000','Mỳ: 80.000','Cơm hộp: 20.000']
A1 = [50000,80000,20000]
B = StringVar(value= A)
def tinhtien() :
    tongtien = 0
    x = C1.curselection()
    print(x)
    for i in x :
        tongtien = tongtien +A1[i]
    L1.configure(text= 'Tổng tiền nà :' + str(tongtien))

C1 = Listbox(master = F1 ,font= ('arial', 15), listvariable=B, selectmode=MULTIPLE)
C1.grid(row=0, column=0,rowspan= 3, pady=30 , sticky='w')
C2 = Listbox(master = F1,font= ('arial', 15), listvariable=B, selectmode=MULTIPLE)
C2.grid(row=0, column=1,rowspan= 3, pady=30 , sticky='w')

B1 = Button(master = tinhtoan,text='OK', font=('arial', 20), command= tinhtien)
B1.grid(row=1, column=1, padx=50, sticky='s')

L1 = Label(master = tinhtoan,text=('Tong tien : '), font=('arial', 20, 'bold'), fg = 'green')
L1.grid(row=2, column=1, padx=50, sticky='n')



tinhtoan.mainloop()