from tkinter import *

BMI = Tk()
BMI.title('BMI CACULATOR')
BMI.geometry('500x400+400+200')
BMI.resizable(False,False)
bmi = DoubleVar()


#self.Hàm xử lí các thao tác
def tinhtoan() :
    #self.Hiển thị thông báo nếu người dùng chưa nhập thông tin
    
    
    if cao2.get() != '' or nang2.get() != '':
        try :
            bmi.set(float(nang2.get())/(float(cao2.get())/100)**2)
        except ValueError: 
            thongbao3.configure( text = 'Mời bạn nhập chính xác chiều cao và cân nặng !! ', font= 10, fg = 'snow',bg = 'red')
    if cao2.get() == '' and nang2.get() == '':
        thongbao1.configure( text = 'Mời bạn nhập chiều cao và cân nặng!! ', font= 10, fg = 'green')
        thongbao3.configure( text = '', font= 10, fg = 'green') 
    else :      
        if cao2.get() == '' and nang2.get() != '':
            thongbao1.configure( text = ' Mời bạn nhập chiều cao !! ', font= 11, fg = 'red')
            thongbao3.configure( text = '', bg='snow')
            ketqua.configure(text='')
        if cao2.get() != '' and nang2.get() == '':
            thongbao1.configure( text = ' Mời bạn nhập cân nặng !! ', font= 11, fg = 'red')
            thongbao3.configure( text = '', bg='snow')
            ketqua.configure(text='')
    if x.get()   == 0 :
        thongbao2.configure( text = 'Mời bạn chọn hệ đơn vị đo !! ', font= 10, fg = 'green')
        if x.get()   == 0  and cao2.get() != '' and nang2.get() != '':
            thongbao2.configure( text = 'Mời bạn chọn hệ đơn vị đo !! ', font= 10, fg = 'green') 
            thongbao1.configure( text = '')
    else:
        thongbao2.configure(text='')
    #Thực hiện tính toán khi đã người dùng đã nhập thông tin đầy đủ và chính xác
    
    if  x.get()  != 0  and   cao2.get() != '' and nang2.get() != ''   :
        thongbao1.configure(text='')
        thongbao2.configure(text='')
        if x.get()== 1:
            bmi.set(float(nang2.get())/(float(cao2.get())/100)**2)
            print(bmi.get())
            thongbao3.configure( text = '', bg='snow') 
            ketqua.configure( text = ( ' BMI = '+ str(round(bmi.get(),2))), font= 16, fg = 'green')
            
        if x.get()==2 :
            bmi.set((float(nang2.get())/(float(cao2.get()))**2)*703)
            print(bmi.get()) 
            thongbao3.configure( text = '', bg='snow')
            ketqua.configure( text = ( ' BMI = '+ str(round(bmi.get(),2))), font= 16, fg = 'green')
     
                     
def hienthi():
#self.Hiển thị đơn vị đo theo từng hệ
    if x.get()== 1:
        cao1.configure(text='CHIỀU CAO : (cm)')
        nang1.configure(text='CÂN NẶNG : (kg)')
    if x.get()==2 :
        cao1.configure(text='Cself.HIỀU CAO : (Inches)')
        nang1.configure(text='CÂN NẶNG : (Pounds)')

#Tạo ô nhập chiều cao
cao1 = Label(text= 'Cself.HIỀU CAO : ', font = ('arial', 16))
cao1.grid(row= 0, column= 0, padx= 50,sticky= 'w', pady=20)
cao2 = Entry(width= 15, font= 16)
cao2.grid(row= 2, column= 0,padx= 50, sticky= 'w', pady=5)
#Tạo ô nhập cân nặng
nang1 = Label(text= 'CÂN NẶNG : ', font = ('arial', 16))
nang1.grid(row= 3, column= 0,padx= 50,sticky= 'w', pady=5)
nang2 = Entry(width= 15, font= 16)
nang2.grid(row= 4, column= 0,padx= 50, sticky= 'w', pady=5)
#Tạo nút Thực hiện tính toán BMI
tinh = Button(bg= 'blue',fg= 'snow',text= 'CACULATE', font = ('arial', 16), command= tinhtoan )
tinh.place(x= 200,y=200)

#Tạo các Radiobutton để chọn hệ đơn vị đo
x = IntVar()
metric = Radiobutton(command=hienthi,variable = x,value=1,text= 'Metric',font= 17)
metric.place(x=300,y=70)
english = Radiobutton(command=hienthi,variable = x,value=2,text= 'English',font= 17)
english.place(x=300,y=110)
ketqua = Label( text = ( ' BMI = '+ str(round(bmi.get(),2))), font= 16, fg = 'green')
ketqua.place(x= 200,y=260)

#Tạo các ô thông báo khi người dùng chưa nhập thông tin (mặc định là ẩn đi)
thongbao1 = Label( text = ( ''), font= 16, fg = 'green')
thongbao1.place(x= 55,y=260)
thongbao2 = Label( text = ( ''), font= 16, fg = 'green')

thongbao2.place(x= 55,y=300)
thongbao3 = Label( text = ( ''), font= 16, fg = 'green')
thongbao3.place(x= 40,y=260)
#Lặp chương trình
BMI.mainloop()
