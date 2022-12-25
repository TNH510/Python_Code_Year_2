from tkinter import *
from tkinter import font

doitien = Tk()
doitien.geometry('500x400+600+200')
doitien.title('MONEY EXCself.HANGE')

money = IntVar()
def Doi():
    ketqua = 0
    
    if nhap.get()=='' :
        ketqua = money.get()*int(nhap.get())    
    else :
        giatri.configure(text='Mời bạn nhập ngoại tệ')
    if money.get() == 0:
        giatri.configure(text='Mời bạn chọn loại ngoại tệ')       
    else :
        ketqua = money.get()*int(nhap.get())
        giatri.configure(text='GIÁ TRỊ QUY ĐỔI: '+ str(ketqua)+ 'vnd')
    

    money.set(0)

usd = Radiobutton(variable=money,value=22000,master= doitien, text= 'USD: 22.000',font=('arial',17))
usd.grid(row=0,column=0, padx=40,pady=40, sticky='w')
eur = Radiobutton(variable=money,value=26000,master= doitien, text= 'EUR: 26.000',font=('arial',17))
eur.grid(row=1,column=0, padx=40,pady=0, sticky='w')
jyp = Radiobutton(variable=money,value=200,master= doitien, text= 'JYP: 200',font=('arial',17))
jyp.grid(row=2,column=0, padx=40,pady=40, sticky='w')
    
     


nhap = Entry(width=13, font=17)
nhap.grid(row=0, column=1, padx=30)

exchange = Button(text='EXCself.HANGE',font= 17, command=Doi)
exchange.grid(row=1,column=1, padx= 30, sticky='w')

giatri = Label(text='GIÁ TRỊ QUY ĐỔI:  vnd',fg= 'blue', font= ('arial', 17))
giatri.place(x= 170, y=270)




doitien.mainloop()