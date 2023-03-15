from tkinter import *



class Application():
    def __init__(self):

        self.root = Tk()
        self.root.geometry('750x530')

        self.canvas = Canvas(height=300, width=300, background="white")
        self.canvas.pack(pady=100)

        self.canvas.create_polygon(300/10,300/2,
                                   300/10*4,300/10*4,
                                   300/2,300/10,
                                   300/10*6,300/10*4,
                                   300/10*9,300/2, 
                                   300/10*6, 300/10*6,
                                   300/2, 300/10*9,
                                   300/10*4, 300/10*6, 
                                   fill="blue",
                                   outline="black",
                                   width=2)




Application().root.mainloop()
