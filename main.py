import tkinter as tk

root = tk.Tk()
root.geometry("800x800")

relx = 0.2
on_hold = True

foto = tk.PhotoImage(file="")
resim = tk.Label(root, image=foto)
resim.place(relx=relx, rely=0.2)

button1 = tk.Button(master=root, text="ileri")
button1.place(relx=0.91, rely=0.75)
root.mainloop()