from tkinter import *
import cx_Freeze

class giaodien_1 :
    def __init__(self,master_1) :
        self.master = master_1
        self.cao1 = Label(self.master,text= 'Cself.HIỀU CAO : ', font = ('arial', 16))
        self.cao1.grid(row= 0, column= 0, padx= 50,sticky= 'w', pady=20)
        self.cao2 = Entry(self.master,width= 15, font= 16)
        self.cao2.grid(row= 2, column= 0,padx= 50, sticky= 'w', pady=5)
        self.nang1 = Label(self.master,text= 'CÂN NẶNG : ', font = ('arial', 16))
        self.nang1.grid(row= 3, column= 0,padx= 50,sticky= 'w', pady=5)
        self.nang2 = Entry(self.master,width= 15, font= 16)
        self.nang2.grid(row= 4, column= 0,padx= 50, sticky= 'w', pady=5)
        self.tinh = Button(self.master,bg= 'blue',fg= 'snow',text= 'CACULATE', font = ('arial', 16), command= self.tinhtoan )
        self.tinh.place(x= 200,y=200)
        self.x = IntVar()
        self.bmi = DoubleVar()
        self.metric = Radiobutton(self.master,command=self.hienthi,variable =self.x,value=1,text= 'Metric',font= 17)
        self.metric.place(x=300,y=70)
        self.english = Radiobutton(self.master,command=self.hienthi,variable = self.x,value=2,text= 'English',font= 17)
        self.english.place(x=300,y=110)
        self.ketqua = Label(self.master, text = ( ' BMI = '+ str(round(self.bmi.get(),2))), font= 16, fg = 'green')
        self.ketqua.place(x= 200,y=260)
        self.thongbao1 = Label(self.master, text = ( ''), font= 16, fg = 'green')
        self.thongbao1.place(x= 55,y=260)
        self.thongbao2 = Label(self.master, text = ( ''), font= 16, fg = 'green')
        self.thongbao2.place(x= 55,y=300)
        self.thongbao3 = Label(self.master, text = ( ''), font= 16, fg = 'green')
        self.thongbao3.place(x= 40,y=260)       
        self.bmi = DoubleVar()
    
    def hienthi(self):
        if self.x.get()== 1:
            self.cao1.configure(text='Cself.HIỀU CAO : (cm)')
            self.nang1.configure(text='CÂN NẶNG : (kg)')
        if self.x.get()==2 :
            self.cao1.configure(text='Cself.HIỀU CAO : (Inches)')
            self.nang1.configure(text='CÂN NẶNG : (Pounds)')     
    
    def tinhtoan(self) :  
        if self.cao2.get() != '' or self.nang2.get() != '':
            try :
                self.bmi.set(float(self.nang2.get())/(float(self.cao2.get())/100)**2)
            except ValueError: 
                self.thongbao3.configure( text = 'Mời bạn nhập chính xác chiều cao và cân nặng !! ', font= 10, fg = 'snow',bg = 'red')
        if self.cao2.get() == '' and self.nang2.get() == '':
            self.thongbao1.configure( text = 'Mời bạn nhập chiều cao và cân nặng!! ', font= 10, fg = 'green')
            self.thongbao3.configure( text = '', font= 10, fg = 'green') 
        else :      
            if self.cao2.get() == '' and self.nang2.get() != '':
                self.thongbao1.configure( text = ' Mời bạn nhập chiều cao !! ', font= 11, fg = 'red')
                self.thongbao3.configure( text = '', bg='snow')
                self.ketqua.configure(text='')
            if self.cao2.get() != '' and self.nang2.get() == '':
                self.thongbao1.configure( text = ' Mời bạn nhập cân nặng !! ', font= 11, fg = 'red')
                self.thongbao3.configure( text = '', bg='snow')
                self.ketqua.configure(text='')
        if self.x.get()   == 0 :
            self.thongbao2.configure( text = 'Mời bạn chọn hệ đơn vị đo !! ', font= 10, fg = 'green')
            if self.x.get()   == 0  and self.cao2.get() != '' and self.nang2.get() != '':
                self.thongbao2.configure( text = 'Mời bạn chọn hệ đơn vị đo !! ', font= 10, fg = 'green') 
                self.thongbao1.configure( text = '')
        else:
            self.thongbao2.configure(text='')
        #Thực hiện tính toán khi đã người dùng đã nhập thông tin đầy đủ và chính xác
        
        if  self.x.get()  != 0  and   self.cao2.get() != '' and self.nang2.get() != ''   :
            self.thongbao1.configure(text='')
            self.thongbao2.configure(text='')
            if self.x.get()== 1:
                self.bmi.set(float(self.nang2.get())/(float(self.cao2.get())/100)**2)
                print(self.bmi.get())
                self.thongbao3.configure( text = '', bg='snow') 
                self.ketqua.configure( text = ( ' BMI = '+ str(round(self.bmi.get(),2))), font= 16, fg = 'green')
                
            if self.x.get()==2 :
                self.bmi.set((float(self.nang2.get())/(float(self.cao2.get()))**2)*703)
                print(self.bmi.get()) 
                self.thongbao3.configure( text = '', bg='snow')
                self.ketqua.configure( text = ( ' BMI = '+ str(round(self.bmi.get(),2))), font= 16, fg = 'green')

class giaodien_2 :
    def __init__(self,master_2) :
        self.master = master_2
        self.cao1 = Label(self.master,text= 'Cself.HIỀU CAO : ', font = ('arial', 16))
        self.cao1.grid(row= 0, column= 0, padx= 50,sticky= 'w', pady=20)
        
def main() :
    BMI = Tk()
    BMI.title('BMI CACULATOR')
    BMI.geometry('500x400+400+200')
    BMI.resizable(False,False)
    app = giaodien_1(BMI)
    BMI.mainloop()
    
if __name__ == '__main__' :
    main()
