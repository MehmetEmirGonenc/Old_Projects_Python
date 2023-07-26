from tkinter import *
from PIL import ImageTk
import time

class Car:
    def __init__(self, CarIMG, canvas):
        self.CarIMG = CarIMG
        self.canvas = canvas
        self.score  = 0
        self.speed  = 0

        self.CarId  = canvas.create_image(50, 100, image=CarIMG)

        self.textSkor = self.canvas.create_text(610, 30, text="Skor : 0", font=("Arial", 16), fill="red")
        self.textHiz = self.canvas.create_text(510, 30, text="Hız : 0", font=("Arial", 16), fill="blue")

        self.x = 0  # X eksenindeki baslangic hizimiz
        self.y = 0  # Y eksenindeki baslangic hizimiz

        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
    def Drow(self):
        self.canvas.move(self.CarId, self.x, self.y)
        coord=self.canvas.coords(self.CarId)
    def move_left(self, event):
        self.x = -1 - (self.speed / 100)
        self.y = 0

    def move_right(self, event):
        self.x = 1 + (self.speed / 100)
        self.y = 0

    def move_up(self, event):
        self.x = 0
        self.y = -1 - (self.speed / 100)

    def move_down(self, event):
        self.x = 0
        self.y = 1 + (self.speed / 100)

Tk = Tk()
Tk.title('Car Game')  # Oyun basligimiz
canvas = Canvas(Tk, width=679, height=374, bd=0,
                highlightthickness=0)  # Oyun ekranimizi 679x374 boyutlarinda olusturuyoruz

car = PhotoImage(file='Car.png')  # Ufo Resmimiz
canvas.pack()
Tk.update()

Car = Car(car, canvas)  # Ufo Nesnemize Gerekli Parametreleri Yolluyoruz.

while 1:
    Car.Drow()
    Tk.update_idletasks()
    Tk.update()
    time.sleep(0.005)











