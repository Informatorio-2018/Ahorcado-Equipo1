from random import randint
from random import shuffle
import tkinter as tk
from tkinter import ttk

LETRA_GRA=("Verdana",113)
LETRA_GRA2=("Verdana",30)
LETRA_NOR=("Verdana",20)


class Ahorcado(tk.Tk):
    
    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)

        tk.Tk.wm_title(self,"Juego Ahorcado")
        
        contenedor = tk.Frame(self)
        contenedor.pack(side="top" , fill="both" , expand=True)
        contenedor.grid_rowconfigure(0, weight = 1)
        contenedor.grid_columnconfigure(0, weight = 1)

        self.frames= {}

        for F in (MenuJuego, PantaJuego):
            frame = F(contenedor,self)
            self.frames[F] = frame
            frame.grid(row=0 , column=0 , sticky="nsew")
        
        self.mostrar_frame(MenuJuego)

    def mostrar_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()

class MenuJuego(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="Menu" , font=LETRA_GRA)
        label.pack(pady=80)

        boton1= ttk.Button(self , text="Jugar" ,
            command=lambda: controlador.mostrar_frame(PantaJuego))
        boton1.pack(ipadx=50,ipady=10,pady=5)

        boton2= ttk.Button(self , text="Puntuacion" ,
            command=lambda: controlador.mostrar_frame(PantaJuego))
        boton2.pack(ipadx=50,ipady=10,pady=5)

        boton3= ttk.Button(self , text="Dificultad" ,
            command=lambda: controlador.mostrar_frame(PantaJuego))
        boton3.pack(ipadx=50,ipady=10,pady=5)

        boton4= ttk.Button(self , text="Salir" ,
            command=quit)
        boton4.pack(ipadx=50,ipady=10,pady=5)

class PantaJuego(tk.Frame):
    
    text_bot=0
    list_word={}
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    palabra = ''
    palabra_sg=""
    palabra_list=[]
    
    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        
        label = ttk.Label(self, text="Ahorcado" , font=LETRA_GRA2)
        label.place(relx=0.5,y=50,anchor="center")
        
        # BOTONES
        #################################################################
        label = ttk.Label(self, text="Tabla de letras" , font=LETRA_NOR)
        label.place(x=550,y=100, anchor="w")
        
        self.letra_bot(1)
        self.boton1= tk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(1))
        self.boton1.place(x=550,y=200, anchor="w",width=50)

        self.letra_bot(2)
        self.boton2= tk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(2))
        self.boton2.place(x=600,y=200, anchor="w",width=50)
        
        self.letra_bot(3)
        self.boton3= tk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(3))
        self.boton3.place(x=550,y=250, anchor="w",width=50)
        
        self.letra_bot(4)
        self.boton4= ttk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(4))
        self.boton4.place(x=600,y=250, anchor="w",width=50)

        self.letra_bot(5)
        self.boton5= ttk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(5))
        self.boton5.place(x=550,y=300, anchor="w",width=50)
        
        self.letra_bot(6)
        self.boton6= ttk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(6))
        self.boton6.place(x=600,y=300, anchor="w",width=50)
        
        self.letra_bot(7)
        self.boton7= ttk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(7))
        self.boton7.place(x=550,y=350, anchor="w",width=50)
        
        self.letra_bot(8)
        self.boton8= ttk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(8))
        self.boton8.place(x=600,y=350, anchor="w",width=50)

        self.letra_bot(9)
        self.boton9= ttk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(9))
        self.boton9.place(x=550,y=400, anchor="w",width=50)
        
        self.letra_bot(10)
        self.boton10= ttk.Button(self , text=self.text_bot ,
            command=lambda: self.letra_Incognita(10))
        self.boton10.place(x=600,y=400, anchor="w",width=50)

        #############################################################3

        self.carga_txt()
        self.incognita_guiones()

        incognita = tk.Label(self,text = self.palabra, font=LETRA_NOR)
        incognita.place(x=200,y=400)

    
    def carga_txt(self):
        palabras = open('ahorcado_5.txt','r')
        listPalabras = palabras.readlines()
        palabras.close()
        i = randint(0,600)
        self.palabra_sg = listPalabras[i]
        join = ",".join(self.palabra_sg)
        self.palabra_list = join.split(",")
        return self.palabra_sg

    
    def incognita_guiones(self):
        longpalabra = len(self.palabra_sg)
        self.palabra = '_ '*(longpalabra-1)
        return self.palabra

    # a es igual al numero del boton
    # shuffle ordena la lista radom y pop saca un valor asi no se repiten
    # y los guarda en un dicccioario
    def letra_bot(self,a):
        shuffle(self.abc)
        self.text_bot= self.abc.pop()
        # index=randint(0,26)
        # self.text_bot=self.abc[index]
        self.list_word[a]=self.text_bot

    # cambia el color del boton si esta e la incognita
    # nota nose como cambiar para q cambie la variable del boton
    # con en argumento q pide la funcion
    def letra_Incognita(self,a):
        print(self.palabra_sg)
        if self.list_word[a] in self.palabra_list:
            self.boton1.configure(bg="green")
            self.boton1.config(state="disable")
        else:
            self.boton1.configure(bg="red")
            self.boton1.config(state="disable")

app=Ahorcado()
app.geometry("800x600")
app.resizable(False, False)

app.mainloop()