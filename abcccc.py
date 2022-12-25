from tkinter import *



BMI = Tk()
BMI.title('Phần mềm tính BMI')
BMI.geometry('500x400+400+200')
BMI.resizable(False,False)


bmi = DoubleVar()


ketqua = Label( text = ( ' BMI = '+ str(round(bmi.get(),2))), font= 16, fg = 'green')
ketqua.place(x= 200,y=260)
def tinhtoan() :
    
    if cao2.get() == '' :
        
        ketqua = Label( text = 'Mời bạn nhập chiều cao và cân nặng !! ', font= 16, fg = 'green')
        ketqua.place(x= 10,y=260)
    else:
        ketqua = Label( text = ' ', font= 16, fg = 'green')
        ketqua.place(x= 10,y=260)

        if x.get()== 1:
            bmi.set(float(nang2.get())/(float(cao2.get())/100)**2)
            print(bmi.get())
 
            ketqua = Label( text = ( ' BMI = '+ str(round(bmi.get(),2))), font= 16, fg = 'green')
            ketqua.place(x= 200,y=260)

        if x.get()==2 :
            bmi.set((float(nang2.get())/(float(cao2.get()))**2)*703)
            print(bmi.get())
 
            ketqua = Label( text = ( ' BMI = '+ str(round(bmi.get(),2))), font= 16, fg = 'green')
            ketqua.place(x= 200,y=260)
        
        
    

   
def hienthi():

    if x.get()== 1:
        cao1.configure(text='Cself.HIỀU CAO : (cm)')
        nang1.configure(text='CÂN NẶNG :(kg)')
    if x.get()==2 :
        cao1.configure(text='Cself.HIỀU CAO : (Inches)')
        nang1.configure(text='CÂN NẶNG :(Pounds)')


cao1 = Label(text= 'Cself.HIỀU CAO : ', font = ('arial', 16))
cao1.grid(row= 0, column= 0, padx= 50,sticky= 'w', pady=20)
cao2 = Entry(width= 15, font= 16)
cao2.grid(row= 2, column= 0,padx= 50, sticky= 'w', pady=5)

nang1 = Label(text= 'CÂN NẶNG : ', font = ('arial', 16))
nang1.grid(row= 3, column= 0,padx= 50,sticky= 'w', pady=5)
nang2 = Entry(width= 15, font= 16)
nang2.grid(row= 4, column= 0,padx= 50, sticky= 'w', pady=5)

tinh = Button(text= 'CACULATE', font = ('arial', 16), command= tinhtoan )
tinh.place(x= 200,y=200)

x = IntVar()
metric = Radiobutton(command=hienthi,variable = x,value=1,text= 'Metric',font= 17)
metric.place(x=300,y=70)
english = Radiobutton(command=hienthi,variable = x,value=2,text= 'Enlish',font= 17)
english.place(x=300,y=110)

 

BMI.mainloop()