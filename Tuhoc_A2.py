from tkinter import *
 
class program(Tk):
    def __init__(self):
        Tk.__init__(self)

        
        l1 = Label(master= self, text= 'xin chào', font= ('arial',16,'bold '), fg= 'blue' )
        l1. grid(row= 1, column= 0, padx= '20')
        l4 = Label(master= self, text= 'xin chào', font= ('arial',16,'bold '), fg= 'blue' )
        l4. grid(row=1 , column= 1, padx= '20')
        



        x = IntVar()
        x.set(0)
        def b1_click():
            x.set(x.get()+1)
            if x.get() == 1 :
                l4.configure(fg = a3.get())
            if x.get() == 2:
                l4.configure(fg = a4.get())
                x.set(0)
            

        a1= Button(master= self,command= b1_click, text= 'màu chữ', width= 15, fg = 'red')
        a1.grid(row = 2, column= 0)
        a1= Button(master= self, text= 'màu nền', width= 15, fg = 'red')
        a1.grid(row = 2, column= 1)
        a3 = Entry(master= self, font= 'arial', width= 12)
        a3.grid(row= 3, column= 0 )
        a4 = Entry(master= self, font= 'arial', width= 12)
        a4.grid(row= 3, column= 1 )


if __name__ == '__main__':
    app = program()
    app.mainloop() 
