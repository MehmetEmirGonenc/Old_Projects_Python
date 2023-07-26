from tkinter import *
from PIL import ImageTk,Image

master =Tk()
master.title('Design App')
canvas = Canvas(master, width=400, height=900, bg='#26C5D2')
canvas.pack()
class Design():
    def __init__(self, model):
        self.model = model

    def NewModel(self):
        self.model = Tk()
        self.model.title('New Model')
        modelcanvas = Canvas(self.model, width=1600, height=900)
        modelcanvas.pack()

NewModel = Button(master,text="New Model" ,width=10 ,height=1,
           command=Design.NewModel()
)
NewModel.place(relx=0.1, rely=0.03,)




master.mainloop()