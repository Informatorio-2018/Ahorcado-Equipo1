from random import randint
from random import shuffle
import tkinter as tk
from tkinter import ttk
import time

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
#################### Pantalla de Menu #############################
    
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
    tiempo=0
    list_word=[]
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    palabra = ''
    palabra_sg=""
    palabra_list=[]
    boton_dic={1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None}
    conta=0
    conta_img=0
    imagenes="imagenes/horca.png"    

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
        
        self.canvas = tk.Canvas(self, width = 300, height = 300)      
        self.canvas.pack()
        self.canvas.place(x=150,y=100) 
        self.monigote = tk.PhotoImage(file=self.imagenes)
        self.canvas.create_image(100,100,image=self.monigote)

        # FUNCIONES
        ###############################################################3

    
    def carga_txt(self):
        
        # Carga un palabra random desde ahorcado.txt
        palabras = open('ahorcado_5.txt','r')
        listPalabras = palabras.readlines()
        palabras.close()
        i = randint(0,600)
        self.palabra_sg = listPalabras[i]
        
        # transforma la palabra en lista y la guarda en palabra_list
        # y la copia
        strip = self.palabra_sg.strip()
        join = ",".join(strip)
        self.palabra_list = join.split(",")
        copia_list=self.palabra_list.copy()
        shuffle(copia_list)
        
        # list_word es donde se guarda las letras para los botones
        self.list_word= copia_list+self.list_word
        shuffle(self.abc)
        cpt=0
        while cpt!=5:
            saca_abc= self.abc.pop()
            if saca_abc not in self.list_word:
                cpt+=1
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
        if self.list_word[a-1] in self.palabra_list:
            self.boton_dic[a]=True
        else:
            self.boton_dic[a]=False

    # cambia el color del boton si esta e la incognita
    # nota: buscar manera de simplificar
    def letra_Incognita(self,a):
        print(self.list_word)
        print(self.palabra_list)
        print(self.boton_dic)
        if self.list_word[a-1] in self.palabra_list and self.boton_dic[a]==True:
            
            if a==1 and self.boton_dic[1]==True:
                self.boton1.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton1.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==2 and self.boton_dic[2]==True:
                self.boton2.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton2.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==3 and self.boton_dic[3]==True:
                self.boton3.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton3.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==4 and self.boton_dic[4]==True:
                self.boton4.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton4.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==5 and self.boton_dic[5]==True:
                self.boton5.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton5.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==6 and self.boton_dic[6]==True:
                self.boton6.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton6.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==7 and self.boton_dic[7]==True:
                self.boton7.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton7.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==8 and self.boton_dic[8]==True:
                self.boton8.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton8.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==9 and self.boton_dic[9]==True:
                self.boton9.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton9.config(state="disable")
                self.Cambio_De_Guio(a)
            
            elif a==10 and self.boton_dic[10]==True:
                self.boton10.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton10.config(state="disable")
                self.Cambio_De_Guio(a)

        elif self.boton_dic[a]==False:
            
            if a==1 and self.boton_dic[1]==False:
                self.boton1.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton1.config(state="disable")
                self.actuliza_img()
            
            elif a==2 and self.boton_dic[2]==False:
                self.boton2.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton2.config(state="disable")
                self.actuliza_img()

            elif a==3 and self.boton_dic[3]==False:
                self.boton3.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton3.config(state="disable")
                self.actuliza_img()

            elif a==4 and self.boton_dic[4]==False:
                self.boton4.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton4.config(state="disable")
                self.actuliza_img()

            elif a==5 and self.boton_dic[5]==False:
                self.boton5.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton5.config(state="disable")
                self.actuliza_img()

            elif a==6 and self.boton_dic[6]==False:
                self.boton6.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton6.config(state="disable")
                self.actuliza_img()

            elif a==7 and self.boton_dic[7]==False:
                self.boton7.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton7.config(state="disable")
                self.actuliza_img()

            elif a==8 and self.boton_dic[8]==False:
                self.boton8.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton8.config(state="disable")
                self.actuliza_img()

            elif a==9 and self.boton_dic[9]==False:
                self.boton9.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton9.config(state="disable")
                self.actuliza_img()

            elif a==10 and self.boton_dic[10]==False:
                self.boton10.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton10.config(state="disable")
                self.actuliza_img()

    def Cambio_De_Guio(self,a):
        cambio=self.list_word.copy()
        nuevaletraindex=[i for i, x in enumerate(self.palabra_list) if x == (self.list_word[a-1])]
        
        if len(nuevaletraindex)>1:
            sustiindex=cambio.pop(a-1)
            self.palabra[nuevaletraindex[self.conta]]=sustiindex
            self.conta+=1
            self.incognita.configure(text=(self.palabra),)    
        else:
            sustiindex=cambio.pop(a-1)
            self.palabra[nuevaletraindex[0]]=sustiindex
            self.incognita.configure(text=(self.palabra),)
    
    def actuliza_img(self):
        if conta_img==0:
            self.imagenes="imagenes/horca.png"
            self.canvas.itemconfig(self, image=self.monigote)
            conta_img+=1

        elif conta_img==1:
            self.imagenes="imagenes/cabeza.png"
        elif conta_img==2:
            self.imagenes="imagenes/cuerpo.png"

            
app=Ahorcado()
app.geometry("800x600")
app.resizable(False, False)

app.mainloop()