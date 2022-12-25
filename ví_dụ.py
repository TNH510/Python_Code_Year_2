
from tkinter import *
class StartPage(Frame):

    def __init__(self, parent, controller):
        
        StartPage.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="s")
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is the start page" )
        label.pack()

        button1 = Button(self, text="Go to Page One",
                            command=lambda: show_frame(StartPage,"PageOne"))
        button2 = Button(self, text="Go to Page Two",
                            command=lambda: show_frame(StartPage,"PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(Frame):

    def __init__(self, parent, controller):
        
        PageOne.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="s")
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 1")
        label.pack()
        button = Button(self, text="Go to the start page",
                           command=lambda: show_frame(PageOne,"StartPage"))
        button.pack()


class PageTwo(Frame):

    def __init__(self, parent, controller):
        
        PageTwo.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="s")
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 2")
        label.pack()
        button = Button(self, text="Go to the start page",
                           command=lambda: show_frame(PageTwo,"StartPage"))
        button.pack()

def show_frame(self, page_name):
    #Show a frame for the given page name
    frame = self.frames[page_name]
    frame.tkraise()

app = Tk()

container = Frame(master = app)
container.pack()
        
app.frames = {}
for F in (StartPage, PageOne, PageTwo):
    page_name = F.__name__
    frame = F(parent=container, controller=app)
    app.frames[page_name] = frame
    frame.grid(row=0, column=0, sticky="s")

    show_frame(app,"StartPage")
        






app.mainloop()