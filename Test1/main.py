"""from Car import *

car1 = Car("Tesla","Electric",2400,38999)
car2 = Car("Toros","LPG",450,2900)

c =1
while c<=10:
    Car.ShowDetail(car1,c)
    c+=1

print('******************************')

print(f'Car-1 > Name : {car1.name}  |  Engine : {car1.engine}  |  HP : {car1.hp}  |  Price : {car1.price}')
print(f'Car-2 > Name : {car2.name}  |  Engine : {car2.engine}  |  HP : {car2.hp}  |  Price : {car2.price}')
"""


"""
from Car import *
car1 = Car("Tesla","Electric",2400,38999)
car2 = Car("Toros","LPG",450,2900)

liste=[car1,car2]
a=1
for i in liste:
    Car.ShowDetail(i,a)


MainGame = Tk()
MainGame.title("Car Game")
canvas = Canvas(MainGame, height=1350, width=2550, bg='#418FEC')
canvas.pack()
#Road
Road = Frame(MainGame, height=1350, width=900, bg='black')
Road.place(relx=0.35, relheight=1)

RoadW1=Frame(Road, height=30, width=15, bg='White')
RoadW1.place(relx=0.32, relheight=1)
RoadW2=Frame(Road, height=30, width=15, bg='White')
RoadW2.place(relx=0.65, relheight=1)
#RoadNear
RoadNL =Frame(MainGame, height=1350 , width=170, bg='Blue')
RoadNL.place(relx=0.3,relheight=1)
RoadNR =Frame(MainGame, height=1350 , width=170, bg='Blue')
RoadNR.place(relx=0.7,relheight=1)
#
#Tree
Tree1_Oak = Frame(RoadNL, height=100, width=40, bg='Brown')
Tree1_Oak.place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1)

Tree1_Leaves=Frame(RoadNL, height=60, width=60, bg="Green")
Tree1_Leaves.place(relx=0.27,rely=0.75,relwidth=0.35, relheight=0.08)

Tree2_Oak = Frame(RoadNR, height=100, width=40, bg='Brown')
Tree2_Oak.place(relx=0.52, rely=0.8, relwidth=0.1, relheight=0.1)

Tree2_Leaves=Frame(RoadNR, height=60, width=60, bg="Green")
Tree2_Leaves.place(relx=0.39,rely=0.75,relwidth=0.35, relheight=0.08)

#
#Car
Car_Body = Frame(MainGame, height=300, width=200, bg='#40B145')
Car_Body.place(relx=0.484, rely=0.7, relwidth=0.08, relheight=0.25)
#Car Parts
Car_HeadLight1 =Frame(Car_Body, height=30, width=50, bg='Yellow')
Car_HeadLight1.place(relx=0.87, rely=0.1, relwidth=0.1, relheight=0.1)

Car_RearLight1 =Frame(Car_Body, height=30, width=50, bg='Yellow')
Car_RearLight1.place(relx=0.03, rely=0.1, relwidth=0.1, relheight=0.1)

Car_HeadLight2 =Frame(Car_Body, height=30, width=50, bg='Red')
Car_HeadLight2.place(relx=0.87, rely=0.8, relwidth=0.1, relheight=0.1)

Car_RearLight2 =Frame(Car_Body, height=30, width=50, bg='Red')
Car_RearLight2.place(relx=0.03, rely=0.8, relwidth=0.1, relheight=0.1)
#
#


print("Hello")


MainGame.mainloop()




ainGame = Tk()
canvas = Canvas(MainGame, height=1350, width=2550, bg='#418FEC')
canvas.pack()
#Road
Road = Frame(MainGame, height=400, width=2550, bg='black')
Road.place(rely=0.075, relheight=0.49)

RoadW1=Frame(Road, height=30, width=2550, bg='White')
RoadW1.place(rely=0.30, relheight=0.015)
RoadW2=Frame(Road, height=30, width=2550, bg='White')
RoadW2.place(rely=0.65, relheight=0.015)
#
#Car
Car_Body = Frame(MainGame, height=300, width=300, bg='#40B145')
Car_Body.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)
#Car Parts
Car_HeadLight1 =Frame(Car_Body, height=30, width=50, bg='Yellow')
Car_HeadLight1.place(relx=0.87, rely=0.1, relwidth=0.1, relheight=0.1)

Car_HeadLight2 =Frame(Car_Body, height=30, width=50, bg='Yellow')
Car_HeadLight2.place(relx=0.87, rely=0.8, relwidth=0.1, relheight=0.1)

Car_RearLight1 =Frame(Car_Body, height=30, width=50, bg='Red')
Car_RearLight1.place(relx=0.03, rely=0.1, relwidth=0.1, relheight=0.1)

Car_RearLight2 =Frame(Car_Body, height=30, width=50, bg='Red')
Car_RearLight2.place(relx=0.03, rely=0.8, relwidth=0.1, relheight=0.1)
#
#

"""
from tkinter import *
import random
import time
from PIL import ImageTk


class Ufo:
    def __init__(self, Inek, UfoResim, canvas):
        self.canvas = canvas
        self.Ineks = Inek
        self.UfoResim = UfoResim
        self.skor = 0
        self.hiz = 0

        # Ufomuz
        self.idUFO = canvas.create_image(50, 100, image=UfoResim)  # Ufomuzu Canvas Uzerine Yerlestiriyoruz

        # Sokurumuzun ve Anlik Hizimizin Yazacagi Textler
        self.textSkor = self.canvas.create_text(610, 30, text="Skor : 0", font=("Arial", 16), fill="red")
        self.textHiz = self.canvas.create_text(510, 30, text="Hız : 0", font=("Arial", 16), fill="blue")

        self.x = 0  # X eksenindeki baslangic hizimiz
        self.y = 0  # Y eksenindeki baslangic hizimiz

        # Klavye kontrol ayarlarimiz
        self.canvas.bind_all('<KeyPress-Left>',
                             self.hareket_sag)  # Sag yon tusuna basinca hareket_sag fonksiyonunu calistir
        self.canvas.bind_all('<KeyPress-Right>',
                             self.hareket_sol)  # Sol yon tusuna basinca hareket_sol fonksiyonunu calistir
        self.canvas.bind_all('<KeyPress-Up>',
                             self.hareket_ust)  # Ust yon tusuna basinca hareket_ust fonksiyonunu calistir
        self.canvas.bind_all('<KeyPress-Down>',
                             self.hareket_alt)  # Alt yon tusuna basinca hareket_alt fonksiyonunu calistir

    # Ufo Nesnemizi Ciziyoruz
    def Ciz(self):
        self.canvas.move(self.idUFO, self.x,
                         self.y)  # Baslangic olarak yukarida verdigimiz default hiz parametrelerini tanimliyoruz
        Koordinat = self.canvas.coords(self.idUFO)  # Ufomuzun anlik ekran uzerindeki koordinatlarini aliyoruz
        # Ufomuz ekranin koselerine gelirse ne yapilacagini belirtiyoruz
        if Koordinat[0] < 10:  # X ekseninde en sag
            self.Kaybettin()  # Eger belirtilen degere gelirse calisacak fonksiyonumuz
        if Koordinat[0] > 670:  # X ekseninde en sol
            self.Kaybettin()  # Eger belirtilen degere gelirse calisacak fonksiyonumuz
        if Koordinat[1] < 10:  # Y ekseninde en ust
            self.Kaybettin()  # Eger belirtilen degere gelirse calisacak fonksiyonumuz
        if Koordinat[1] > 364:  # Y ekseninde en asagisi
            self.Kaybettin()  # Eger belirtilen degere gelirse calisacak fonksiyonumuz
        # Eger Ufomuz ile inegimiz ayni koordinata gelirse uygulancak islemler
        if self.InekKacir(Koordinat) == True:
            self.skor = self.skor + 1  # Skoru 1 arttiriyoruz
            startsX = float(
                random.randint(50, 620))  # Inek nesnemizi x eksenindeki yeni koordinatini rastgele belirliyoruz
            startsY = float(
                random.randint(50, 320))  # Inek nesnemizi y eksenindeki yeni koordinatini rastgele belirliyoruz
            self.canvas.coords(self.Ineks.idInek, startsX, startsY)  # Inek nesnemixi yeni koordinatina tasiyoruz
            self.hiz = self.hiz + 1  # Ufomuzun hizini her inek yediginde 1 arttiriyoruz
            self.canvas.itemconfig(self.textSkor, text="Skor : %s" % self.skor)  # Skor textimizi guncelliyoruz
            self.canvas.itemconfig(self.textHiz, text="Hız : %s" % self.hiz)  # Hiz textimizi guncelliyoruz

    # Yon tuslari icin aragimiz fonksiyonlar. Kacirilan inek sayisina göre ufomuz hizleniyor.
    def hareket_sag(self, event):
        self.x = -1 - (self.hiz / 100)
        self.y = 0

    def hareket_sol(self, event):
        self.x = 1 + (self.hiz / 100)
        self.y = 0

    def hareket_ust(self, event):
        self.x = 0
        self.y = -1 - (self.hiz / 100)

    def hareket_alt(self, event):
        self.x = 0
        self.y = 1 + (self.hiz / 100)

    # Ufomuz ile inek ayni koordinata geldigini belirledigimiz fonskiyon.
    def InekKacir(self, pos):
        InekKoordinat = self.canvas.coords(self.Ineks.idInek)
        if pos[0] >= InekKoordinat[0] and pos[0] <= InekKoordinat[0] + 50:
            if pos[1] >= InekKoordinat[1] and pos[1] <= InekKoordinat[1] + 50:
                return True

        return False

    # Kaybetme fonksiyonumuz
    def Kaybettin(self):
        self.x = 0  # Hizimizi 0 liyoruz.
        self.y = 0
        self.canvas.coords(self.idUFO, 700, 700)  # Ufomuzu ekranin disina tasiyoruz
        self.textid = self.canvas.create_text(350, 150, text="Kaybettin", font=("Arial", 25),
                                              fill="red")  # Ekrana kirmizi yazilar ile Kaybettin yaziyoruz.


class Inek:
    def __init__(self, canvas, InekResim):
        self.canvas = canvas
        self.idInek = canvas.create_image(10, 10, image=InekResim)  # Inegimii 10x10 koordinatlarinda olustiriyoruz.
        self.canvas.move(self.idInek, 150, 20)

    def Ciz(self):
        self.canvas.move(self.idInek, 0, 0)


tk = Tk()
tk.title('Inek Kacirma Oyunu')  # Oyun basligimiz
canvas = Canvas(tk, width=679, height=374, bd=0,
                highlightthickness=0)  # Oyun ekranimizi 679x374 boyutlarinda olusturuyoruz

UFO = PhotoImage(file='Ufo.png')  # Ufo Resmimiz
INEK = PhotoImage(file='Cow.png')  # Inek Resmimiz
ArkaPlan = ImageTk.PhotoImage(file="MainBackground.png")  # Arkaplan resmimiz
canvas.create_image(0, 0, image=ArkaPlan, anchor=NW)  # Ekranimizin arkaplanini belirliyoruz
canvas.pack()
tk.update()

Inek = Inek(canvas, INEK)  # Inek Nesnemize Gerekli Parametreleri Yolluyoruz.
Ufo = Ufo(Inek, UFO, canvas)  # Ufo Nesnemize Gerekli Parametreleri Yolluyoruz.

while 1:
    Inek.Ciz()
    Ufo.Ciz()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)







































