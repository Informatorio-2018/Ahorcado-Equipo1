from tkinter import *
#Crear ventana con botones jugar dificultad, puntuacion, salir

app=Tk()
class Menu():
    menu=Frame(app).grid()
    jugar=Button(menu,text="Jugar",width=50,font=30).grid(padx=10, pady=10)
    dificultad=Button(menu,text="Dificultad",width=50,font=30).grid(padx=10, pady=10)
    puntuacion=Button(menu,text="Puntuación",width=50,font=30).grid(padx=10, pady=10)
    salir=Button(menu,text="Salir",width=50,font=30).grid(padx=10, pady=10)

menu=Menu()
mainloop()
