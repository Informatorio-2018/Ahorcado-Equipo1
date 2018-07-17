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
        #Poener aqui el nombre de la clase de para cambiar de pantalla
        #############################################################
        for F in (MenuJuego, PantaJuego):
            frame = F(contenedor,self)
            self.frames[F] = frame
            frame.grid(row=0 , column=0 , sticky="nsew")
        
        self.mostrar_frame(MenuJuego)
        ###############################################################
        
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
    list_word=[]
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    palabra = ''
    palabra_sg=""
    palabra_list=[]
    boton_dic=[1,2,3,4,5,6,7,8,9,10]
    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        
        label = ttk.Label(self, text="Ahorcado" , font=LETRA_GRA2)
        label.place(relx=0.5,y=50,anchor="center")
        
        self.carga_txt()
        
        # BOTONES
        #################################################################
        label = ttk.Label(self, text="Tabla de letras" , font=LETRA_NOR)
        label.place(x=550,y=100, anchor="w")
        
        self.letra_bot(1)
        self.boton1= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(1))
        self.boton1.place(x=550,y=200, anchor="w",width=50)
        
        self.letra_bot(2)
        self.boton2= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(2))
        self.boton2.place(x=600,y=200, anchor="w",width=50)
        
        self.letra_bot(3)
        self.boton3= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(3))
        self.boton3.place(x=550,y=250, anchor="w",width=50)
        
        self.letra_bot(4)
        self.boton4= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(4))
        self.boton4.place(x=600,y=250, anchor="w",width=50)

        self.letra_bot(5)
        self.boton5= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(5))
        self.boton5.place(x=550,y=300, anchor="w",width=50)
        
        self.letra_bot(6)
        self.boton6= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(6))
        self.boton6.place(x=600,y=300, anchor="w",width=50)
        
        self.letra_bot(7)
        self.boton7= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(7))
        self.boton7.place(x=550,y=350, anchor="w",width=50)
        
        self.letra_bot(8)
        self.boton8= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(8))
        self.boton8.place(x=600,y=350, anchor="w",width=50)

        self.letra_bot(9)
        self.boton9= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(9))
        self.boton9.place(x=550,y=400, anchor="w",width=50)
        
        self.letra_bot(10)
        self.boton10= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",10, "bold"),
            command=lambda: self.letra_Incognita(10))
        self.boton10.place(x=600,y=400, anchor="w",width=50)

        b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        b_volver.pack(ipadx=50,ipady=10,pady=5)
        b_volver.place(x=400,y=550,anchor="s")

        #############################################################3

        self.incognita_guiones()

        self.incognita = tk.Label(self,text = self.palabra, font=LETRA_NOR)
        self.incognita.place(x=200,y=400)
        

        # FUNCIONES
        ###############################################################3

    
    def carga_txt(self):
        palabras = open('ahorcado_5.txt','r')
        listPalabras = palabras.readlines()
        palabras.close()
        i = randint(0,600)
        self.palabra_sg = listPalabras[i]
        strip = self.palabra_sg.strip()
        join = ",".join(strip)
        self.palabra_list = join.split(",")
        copia_list=self.palabra_list.copy()
        shuffle(copia_list)
        self.list_word= copia_list+self.list_word
        cpt=5
        shuffle(self.abc)
        while cpt!=0:
            cpt-=1
            saca_abc= self.abc.pop()
            self.list_word.append(saca_abc)
        shuffle(self.list_word)

    
    def incognita_guiones(self):
        longpalabra = len(self.palabra_sg)
        guion=["_"]
        self.palabra = guion*(longpalabra-1)

    def letra_bot(self,a):
        # index=randint(0,26)
        # self.text_bot=self.abc[index]
        self.text_bot=self.list_word[a-1]

    # cambia el color del boton si esta e la incognita
    # nota: no se como cambiar para q cambie la variable del boton
    # con en argumento q pide la funcion
    def letra_Incognita(self,a):
        print(self.list_word)
        print(self.palabra_list)
        print(self.palabra)
        if self.list_word[a-1] in self.palabra_list:
            self.boton1.config(bg="green",disabledforeground="snow",relief="groove")
            self.boton1.config(state="disable")
            cambio=self.list_word.copy()
            nuevaletraindex=self.palabra_list.index(self.list_word[a-1])
            sustiindex=cambio.pop(a-1)
            self.palabra[nuevaletraindex]=sustiindex
            self.incognita.configure(text=(self.palabra),)
        else:
            self.boton1.config(bg="red",disabledforeground="snow",relief="groove")
            self.boton1.config(state="disable")
        
        
            
app=Ahorcado()
app.geometry("800x600")
app.resizable(False, False)

app.mainloop()