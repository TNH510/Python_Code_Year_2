from tkinter import *
from tkinter import filedialog


w = Tk()
w.geometry('800x600+400+200')
w.title('soan thao')

T1 = Text(font=('times new roman', 13))
T1.place(x=0, y=0, width=600, height=600)

def Open() :
    x = filedialog.askopenfile(mode='r') #read
    with open(file=x.name, mode= 'r', encoding = 'utf-16' ) as f:
        A = f.read()
        T1.delete('1.0',END)
        T1.insert('1.0',A)
        f.close()
def Save() :
    x2 = filedialog.asksaveasfile(mode='w') #read
    with open(file=x2.name, mode= 'w', encoding = 'utf-16' ) as f:
        A = T1.get('1.0',END)
        f.write(A)
        f.close()


B1 =Button(font= ('arial',15), text= 'Open', width =12, command=Open)
B1.place(x=630, y=50)
B1 =Button(font= ('arial',15), text= 'Save', width =12, command=Save)
B1.place(x=630, y=100)

w.mainloop()

