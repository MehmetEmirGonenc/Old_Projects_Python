from tkinter import *

master = Tk()
canvas =Canvas(master, height=900, width=1400, bg='Pink')
canvas.pack()

frame_top = Frame(master, height=300, width=300,bg='#00bdca')
frame_top.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)

frame_bottom = Frame(master, height=300, width=300,bg='#00bdca')
frame_bottom.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.7)



###################Master Objects/###################
title_label = Label(frame_top, bg='#00bdca', text="Check In", font="Verdana 20 underline bold")
title_label.pack()
CheckInType_label = Label(frame_top, bg='#00bdca', text="Check In Type :", font="Verdana 12 bold")
CheckInType_label.pack(side=LEFT)
CheckInType_Option = StringVar(frame_top)
CheckInType_Option.set("\t")
CheckInType_Option_Menu = OptionMenu(frame_top,CheckInType_Option,
    "Normal",
    "Reservation",
    "Internet")
CheckInType_Option_Menu.pack(padx=10,pady=10,side=LEFT)


###################\Master Objects###################

###################Top Objects/###################




###################\Top Objects###################

###################Bottom Objects/###################




###################\Bottom Objects###################

master.mainloop()

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























