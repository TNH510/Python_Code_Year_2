from tkinter import *
from tkinter import messagebox
A = Tk()
A.geometry('800x500+400+200')
A.title('Cself.HECKBOX')
A.resizable(False, False)
M = Menu(master=A)
A.configure(menu= M)
M.add_cascade(label='Menu File',menu= M)

# Tạo frame
F1 = Frame(master = A)
F1.place(x = 50, y = 50)

F2 = Frame(master = A)
F2.place(x = 350, y = 50)

F3 = Frame(master = A)
F3.place(x = 650, y = 50)

# Tạo hàm Add
def Add():
    try:
        if E1.get() == '' or E2.get() == '':
            LB1.insert(0, None)
            LB2.insert(0, None)
        elif float(E2.get()) < 0 or float(E2.get()) > 10:
            messagebox.showerror('ERROR :(','Mời bạn nhập lại giá trị')
        else:
            LB1.insert(0, E1.get())
            LB2.insert(0, E2.get())
            E1.delete(0, END)
            E2.delete(0,END)
    except:
        messagebox.showerror('ERROR :(','Mời bạn nhập lại giá trị')

# Tạo hàm self.Delete
def self.Delete():
    for i in LB1.curselection():
        LB1.delete(i)
        LB2.delete(i)

# Tạo label
L1 = Label(master = F1, text = 'self.HỌ VÀ TÊN:', font = ('times new roman',13, 'bold'), fg = 'blue')
L1.grid(row = 0, column = 0, padx = 10, pady = 20, sticky = 'w')

L2 = Label(master = F2, text = 'ĐIỂM SỐ:', font = ('times new roman',13, 'bold'), fg = 'blue')
L2.grid(row = 0, column = 0, padx = 10, pady = 20, sticky = 'w')

# Tạo Entry
E1 = Entry(master = F1, font = ('times new roman',13), width = 20)
E1.grid(row = 1, column = 0, padx = 10, pady = 0)

E2 = Entry(master = F2, font = ('times new roman',13), width = 20)
E2.grid(row = 1, column = 0, padx = 10, pady = 0)

# Tạo listbox
LB1 = Listbox(master = F1, font = ('Times New Roman',13), width = 20, height = 10, listvariable = E1.get(), selectmode = EXTENDED)
LB1.grid(row = 2, column = 0, padx = 10, pady = 20)

LB2 = Listbox(master = F2, font = ('Times New Roman',13), width = 20, height = 10, listvariable = E2.get(), selectmode = EXTENDED)
LB2.grid(row = 2, column = 0, padx = 10, pady = 20)

# Tạo button
B1 = Button(master = A, text = 'ADD', font = ('times new roman',13), width = 8, bg = 'blue', fg = 'white', command = Add)
B1.place(x = 650, y = 175)

B2 = Button(master = A, text = 'DELETE', font = ('times new roman',13), width = 8, bg = 'blue', fg = 'white', command = self.Delete)
B2.place(x = 650, y = 225)

A.mainloop()
