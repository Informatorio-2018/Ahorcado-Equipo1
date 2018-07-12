from tkinter import *
#Crear ventana con botones jugar dificultad, puntuacion, salir

app=Tk()
app.resizable(False,False)
app.geometry("800x600")

class Menu():
    menu=Frame(app).pack()
    titulo=Label(menu,text="AHORCADO",font=("",90)).pack(padx=20,pady=20)
    jugar=Button(menu,text="Jugar",width=10,font=("",30)).pack(pady=10)
    dificultad=Button(menu,text="Dificultad",width=10,font=("",30)).pack(pady=10)
    puntuacion=Button(menu,text="Puntuación",width=10,font=("",30)).pack(pady=10)
    salir=Button(menu,text="Salir",width=10,font=("",30)).pack(pady=10)

menu=Menu()
mainloop()
