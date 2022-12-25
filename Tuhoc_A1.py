from tkinter  import *
from tkinter.font import Font


A = Tk()

A.geometry('360x640+750+100')
def changeposition():
    A.geometry('360x640+100+100')
def exit() :
    A.destroy()
    

a = Button(master = A,fg = 'black', text= 'X', font= ('timenewroman', 12), command= exit)
a.place(x = 300 , y = 290, width= 50 , height= 50)
b = Button(master = A,fg = 'black', text= '9', font= ('timenewroman', 12,) )
b.place(x = 250 , y = 290, width= 50 , height= 50)
c = Button(master = A,fg = 'black', text= '8', font= ('timenewroman', 12), )
c.place(x = 200 , y = 290, width= 50 , height= 50)
d = Button(master = A,fg = 'black', text= '7', font= ('timenewroman', 12), )
d.place(x = 150 , y = 290, width= 50 , height= 50)
e = Button(master = A,fg = 'black', text= '6', font= ('timenewroman', 12), )
e.place(x = 300 , y = 240, width= 50 , height= 50)
f = Button(master = A,fg = 'black', text= '5', font= ('timenewroman', 12), )
f.place(x = 250 , y = 240, width= 50 , height= 50)
g = Button(master = A,fg = 'black', text= '4', font= ('timenewroman', 12), )
g.place(x = 200 , y = 240, width= 50 , height= 50)
h = Button(master = A,fg = 'black', text= '3', font= ('timenewroman', 12), )
h.place(x = 300 , y = 190, width= 50 , height= 50)
i = Button(master = A,fg = 'black', text= '2', font= ('timenewroman', 12), )
i.place(x = 250 , y = 190, width= 50 , height= 50)
j = Button(master = A,fg = 'black', text= '1', font= ('timenewroman', 12), )
j.place(x = 200 , y = 190, width= 50 , height= 50)


l = Button(master = A,fg = 'black', text= 'hehe', font= ('timenewroman', 12), command= changeposition)
l.place(x = 200 , y = 190, width= 50 , height= 50)

A.mainloop()
