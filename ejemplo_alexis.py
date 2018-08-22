from random import randint
from random import shuffle
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
from pygame import *
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
        for F in (MenuJuego, PantaJuego,PantaPuntua,PantaDificult,PantaDerrota,PantaVictoria):
            frame = F(contenedor,self)
            self.frames[F] = frame
            frame.grid(row=0 , column=0 , sticky="nsew")

        self.mostrar_frame(MenuJuego)
        ###############################################################

    def mostrar_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()

    def mostrar_frame2(self, cont):

        frame=self.frames[cont]
        frame.tkraise()
        PantaJuego.muca()

#################### Pantalla de Menu #############################
class MenuJuego(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="Ahorcado" , font=LETRA_GRA)
        label.pack(pady=80)

        s = ttk.Style()
        s.configure('my.TButton', font= 15)

        boton1= ttk.Button(self , text="Jugar" ,style='my.TButton',
            command=lambda: controlador.mostrar_frame2(PantaJuego))
        boton1.pack(ipadx=50,ipady=10,pady=5)

        boton2= ttk.Button(self , text="Puntuacion" ,style='my.TButton',
            command=lambda: controlador.mostrar_frame(PantaPuntua))
        boton2.pack(ipadx=50,ipady=10,pady=5)

        boton3= ttk.Button(self , text="Dificultad" ,style='my.TButton',
            command=lambda: controlador.mostrar_frame(PantaDificult))
        boton3.pack(ipadx=50,ipady=10,pady=5)

        boton4= ttk.Button(self , text="Salir" ,style='my.TButton',
            command= PantaJuego.callback)
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
    conta_victoria=0
    dificultad="medio"
    _job=0
    remaining = 0
    

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)

        label = ttk.Label(self, text="Ahorcado" , font=LETRA_GRA2)
        label.place(relx=0.5,y=50,anchor="center")

        # BOTONES
        #################################################################
        label = ttk.Label(self, text="Tabla de letras" , font=LETRA_NOR)
        label.place(x=550,y=100, anchor="w")


        self.b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: [controlador.mostrar_frame(MenuJuego),self.destruir()])
        self.b_volver.pack(ipadx=50,ipady=10,pady=5)
        self.b_volver.place(x=400,y=550,anchor="s")
        self.b_volver.pi=self.b_volver.place_info()

        self.b_inciar= tk.Button(self , text="Inciar",font=LETRA_NOR ,
            command=lambda: self.tabladebotones())
        self.b_inciar.pack(pady=5)
        self.b_inciar.place(x=400,y=300,anchor="s",width=100,height=50)
        self.b_inciar.pi=self.b_inciar.place_info()

        self.b2_volver= ttk.Button(self , text="Perdiste" ,
            command=lambda: [controlador.mostrar_frame(PantaDerrota),self.olvidarboton(),self.destruir()])
        self.b2_volver.pack(ipadx=50,ipady=10,pady=5)
        self.b2_volver.place(x=400,y=550,anchor="s")
        self.b2_volver.pi=self.b2_volver.place_info()
        self.b2_volver.place_forget()

        self.b3_volver= ttk.Button(self , text="Ganaste" ,
            command=lambda: [controlador.mostrar_frame(PantaVictoria),self.olvidarboton(),self.destruir()])
        self.b3_volver.pack(ipadx=50,ipady=10,pady=5)
        self.b3_volver.place(x=400,y=550,anchor="s")
        self.b3_volver.pi=self.b3_volver.place_info()
        self.b3_volver.place_forget()


        self.text_score = ttk.Label(self,text="Puntuacion: ",font=13)
        self.text_score.pack()
        self.text_score.place(x=350,y=500,anchor="s")

        self.text_timer = tk.Label(self,text="",font=13)
        self.text_timer.pack()
        self.text_timer.place(x=420,y=500,anchor="s")

        self.foto1=tk.PhotoImage(file="imagenes/sonido.png")
        self.foto2=tk.PhotoImage(file="imagenes/nosonido.png")
        self.sonido= tk.Button(self ,image=self.foto1 ,
            command=lambda: self.mute())
        self.sonido.pack()
        self.sonido.place(x=100,y=100,anchor="s")
        self.sonido.config(width=50,height=50)
    
    def tabladebotones(self):
        self.list_word=[]
        self.abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
        self.palabra = ''
        self.palabra_sg=""
        self.palabra_list=[]
        self.boton_dic={1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None}
        self.conta=0
        self.conta_img=0
        self.conta_victoria=0
        self.puntos=0


        self.b_inciar.place_forget()
        self.b_inciar2= ttk.Button(self , text="Nueva palabra" ,
            command=lambda: [self.destruir(), self.tabladebotones()])
        self.b_inciar2.pack()
        self.b_inciar2.place(x=100,y=550,anchor="s")

        self.remaining=0
        
        self.asignar_puntos()

        self.countdown(self.puntos)

        self.carga_txt()

        self.letra_bot(1)
        if self.dificultad=="facil" or self.dificultad=="medio" or self.dificultad=="dificil":
            self.boton1= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(1))
            self.boton1.place(x=550,y=200, anchor="w",width=50)

            self.letra_bot(2)
            self.boton2= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(2))
            self.boton2.place(x=600,y=200, anchor="w",width=50)

            self.letra_bot(3)
            self.boton3= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(3))
            self.boton3.place(x=550,y=250, anchor="w",width=50)

            self.letra_bot(4)
            self.boton4= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(4))
            self.boton4.place(x=600,y=250, anchor="w",width=50)

            self.letra_bot(5)
            self.boton5= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(5))
            self.boton5.place(x=550,y=300, anchor="w",width=50)

            self.letra_bot(6)
            self.boton6= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(6))
            self.boton6.place(x=600,y=300, anchor="w",width=50)

            self.letra_bot(7)
            self.boton7= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(7))
            self.boton7.place(x=550,y=350, anchor="w",width=50)

            self.letra_bot(8)
            self.boton8= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(8))
            self.boton8.place(x=600,y=350, anchor="w",width=50)

            self.letra_bot(9)
            self.boton9= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(9))
            self.boton9.place(x=550,y=400, anchor="w",width=50)

            self.letra_bot(10)
            self.boton10= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                command=lambda: self.letra_Incognita(10))
            self.boton10.place(x=600,y=400, anchor="w",width=50)


            if self.dificultad=="medio" or self.dificultad=="dificil":
                self.letra_bot(11)
                self.boton11= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(11))
                self.boton11.place(x=650,y=200, anchor="w",width=50)

                self.letra_bot(12)
                self.boton12= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(12))
                self.boton12.place(x=700,y=200, anchor="w",width=50)

                self.letra_bot(13)
                self.boton13= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(13))
                self.boton13.place(x=650,y=250, anchor="w",width=50)

                self.letra_bot(14)
                self.boton14= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(14))
                self.boton14.place(x=700,y=250, anchor="w",width=50)

                self.letra_bot(15)
                self.boton15= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(15))
                self.boton15.place(x=650,y=300, anchor="w",width=50)

                self.letra_bot(16)
                self.boton16= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(16))
                self.boton16.place(x=700,y=300, anchor="w",width=50)

                self.letra_bot(17)
                self.boton17= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(17))
                self.boton17.place(x=650,y=350, anchor="w",width=50)

                self.letra_bot(18)
                self.boton18= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(18))
                self.boton18.place(x=700,y=350, anchor="w",width=50)

                self.letra_bot(19)
                self.boton19= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(19))
                self.boton19.place(x=650,y=400, anchor="w",width=50)

                self.letra_bot(20)
                self.boton20= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                    command=lambda: self.letra_Incognita(20))
                self.boton20.place(x=700,y=400, anchor="w",width=50)

            
                if self.dificultad=="dificil":

                    self.letra_bot(21)
                    self.boton21= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                        command=lambda: self.letra_Incognita(21))
                    self.boton21.place(x=750,y=200, anchor="w",width=50)

                    self.letra_bot(22)
                    self.boton22= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                        command=lambda: self.letra_Incognita(22))
                    self.boton22.place(x=750,y=250, anchor="w",width=50)

                    self.letra_bot(23)
                    self.boton23= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                        command=lambda: self.letra_Incognita(23))
                    self.boton23.place(x=750,y=300, anchor="w",width=50)

                    self.letra_bot(24)
                    self.boton24= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                        command=lambda: self.letra_Incognita(24))
                    self.boton24.place(x=750,y=350, anchor="w",width=50)

                    self.letra_bot(25)
                    self.boton25= tk.Button(self , text=self.text_bot ,font=("ComicSansMS",16, "bold"),
                        command=lambda: self.letra_Incognita(25))
                    self.boton25.place(x=750,y=400, anchor="w",width=50)

            #############################################################3

            self.incognita_guiones()

            self.incognita = tk.Label(self,text = self.palabra, font=LETRA_NOR)
            self.incognita.place(x=150,y=400)

            self.monigote = tk.PhotoImage(file="imagenes/horca.png")
            self.canvas = tk.Label(self,image=self.monigote)
            self.canvas.pack()
            self.canvas.place(x=250,y=150)

    

        # FUNCIONES
        ###############################################################3


    def carga_txt(self):

        # Carga un palabra random desde ahorcado.txt
        if self.dificultad=="facil":
            textdificultad='ahorcado_5.txt'

        elif self.dificultad=="medio":
            textdificultad='palabras_8_letras.txt'

        elif self.dificultad=="dificil":
            textdificultad='plalabras_mas_de_8_letras.txt'
            
        
        palabras = open(textdificultad,'r')
        listPalabras = palabras.readlines()
        palabras.close()
        self.palabra_sg = listPalabras[(randint(0,((len(listPalabras)-1))))]

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
        if PantaJuego.dificultad == "medio":
            cpt=20
        elif PantaJuego.dificultad == "facil":
            cpt=10
        elif PantaJuego.dificultad=="dificil":
            cpt=25
        while len(self.list_word)!=cpt:
            saca_abc= self.abc.pop()
            if saca_abc not in self.list_word:
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
        print(self.palabra)
        print(self.conta_victoria)
        print(len(self.palabra))
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

            elif a==11 and self.boton_dic[11]==True:
                self.boton11.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton11.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==12 and self.boton_dic[12]==True:
                self.boton12.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton12.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==13 and self.boton_dic[13]==True:
                self.boton13.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton13.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==14 and self.boton_dic[14]==True:
                self.boton14.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton14.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==15 and self.boton_dic[15]==True:
                self.boton15.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton15.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==16 and self.boton_dic[16]==True:
                self.boton16.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton16.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==17 and self.boton_dic[17]==True:
                self.boton17.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton17.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==18 and self.boton_dic[18]==True:
                self.boton18.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton18.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==19 and self.boton_dic[19]==True:
                self.boton19.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton19.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==20 and self.boton_dic[20]==True:
                self.boton20.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton20.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==21 and self.boton_dic[21]==True:
                self.boton21.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton21.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==22 and self.boton_dic[22]==True:
                self.boton22.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton22.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==23 and self.boton_dic[23]==True:
                self.boton23.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton23.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==24 and self.boton_dic[24]==True:
                self.boton24.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton24.config(state="disable")
                self.Cambio_De_Guio(a)

            elif a==25 and self.boton_dic[25]==True:
                self.boton25.config(bg="green",disabledforeground="snow",relief="groove")
                self.boton25.config(state="disable")
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

            elif a==11 and self.boton_dic[11]==False:
                self.boton11.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton11.config(state="disable")
                self.actuliza_img()

            elif a==12 and self.boton_dic[12]==False:
                self.boton12.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton12.config(state="disable")
                self.actuliza_img()

            elif a==13 and self.boton_dic[13]==False:
                self.boton13.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton13.config(state="disable")
                self.actuliza_img()

            elif a==14 and self.boton_dic[14]==False:
                self.boton14.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton14.config(state="disable")
                self.actuliza_img()

            elif a==15 and self.boton_dic[15]==False:
                self.boton15.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton15.config(state="disable")
                self.actuliza_img()

            elif a==16 and self.boton_dic[16]==False:
                self.boton16.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton16.config(state="disable")
                self.actuliza_img()

            elif a==17 and self.boton_dic[17]==False:
                self.boton17.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton17.config(state="disable")
                self.actuliza_img()

            elif a==18 and self.boton_dic[18]==False:
                self.boton18.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton18.config(state="disable")
                self.actuliza_img()

            elif a==19 and self.boton_dic[19]==False:
                self.boton19.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton19.config(state="disable")
                self.actuliza_img()

            elif a==20 and self.boton_dic[20]==False:
                self.boton20.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton20.config(state="disable")
                self.actuliza_img()

            elif a==21 and self.boton_dic[21]==False:
                self.boton21.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton21.config(state="disable")
                self.actuliza_img()

            elif a==22 and self.boton_dic[22]==False:
                self.boton22.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton22.config(state="disable")
                self.actuliza_img()

            elif a==23 and self.boton_dic[23]==False:
                self.boton23.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton23.config(state="disable")
                self.actuliza_img()

            elif a==24 and self.boton_dic[24]==False:
                self.boton24.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton24.config(state="disable")
                self.actuliza_img()

            elif a==25 and self.boton_dic[25]==False:
                self.boton25.config(bg="red",disabledforeground="snow",relief="groove")
                self.boton25.config(state="disable")
                self.actuliza_img()



    def Cambio_De_Guio(self,a):
        acierto=mixer.Sound("sonido/Dink.wav")
        acierto.play()
        self.mostrarvictoria()
        cambio=self.list_word.copy()
        nuevaletraindex=[i for i, x in enumerate(self.palabra_list) if x == (self.list_word[a-1])]

        if len(nuevaletraindex)>1:
            sustiindex=cambio.pop(a-1)
            self.palabra[nuevaletraindex[self.conta]]=sustiindex
            self.conta+=1
            self.incognita.configure(text=(self.palabra))
            if len(nuevaletraindex) == self.conta:
                self.conta=0 
        else:
            sustiindex=cambio.pop(a-1)
            self.palabra[nuevaletraindex[0]]=sustiindex
            self.incognita.configure(text=(self.palabra),)
        

    def actuliza_img(self):
        error=mixer.Sound("sonido/PiPiPi.wav")
        error.play()
        if self.conta_img==0:
            self.conta_img+=1
            self.monigote= tk.PhotoImage(file="imagenes/cabeza.png")
            self.canvas.configure(image=self.monigote)
            self.canvas.image=self.monigote

        elif self.conta_img==1:
            self.conta_img+=1
            self.monigote= tk.PhotoImage(file="imagenes/cuerpo.png")
            self.canvas.configure(image=self.monigote)
            self.canvas.image=self.monigote

        elif self.conta_img==2:
            self.monigote= tk.PhotoImage(file="imagenes/piernas.png")
            self.canvas.configure(image=self.monigote)
            self.canvas.image=self.monigote
            self.conta_img+=1

        elif self.conta_img==3:
            self.monigote= tk.PhotoImage(file="imagenes/extremidades.png")
            self.canvas.configure(image=self.monigote)
            self.canvas.image=self.monigote
            self.conta_img+=1

        elif self.conta_img==4:
            self.monigote= tk.PhotoImage(file="imagenes/murio.png")
            self.canvas.configure(image=self.monigote)
            self.canvas.image=self.monigote
            
            self.remaining=self.remaining-100
            if self.remaining<0:
                self.remaining=10

            self.mostrarderrota()


    def mostrarderrota(self):
        self.cancel()
        self.incognita.configure(text=(self.palabra_list)
        self.b2_volver.place(self.b2_volver.pi)
        self.b_volver.place_forget()
        mixer.music.load("sonido/derrota.mp3")
        mixer.music.play()

        if self.dificultad=="facil" or self.dificultad=="medio" or self.dificultad=="dificil":
                self.boton1.config(state="disable")
                self.boton2.config(state="disable")
                self.boton3.config(state="disable")
                self.boton4.config(state="disable")
                self.boton5.config(state="disable")
                self.boton6.config(state="disable")
                self.boton7.config(state="disable")
                self.boton8.config(state="disable")
                self.boton9.config(state="disable")
                self.boton10.config(state="disable")
                if self.dificultad=="medio" or self.dificultad=="dificil":
                    self.boton11.config(state="disable")
                    self.boton12.config(state="disable")
                    self.boton13.config(state="disable")
                    self.boton14.config(state="disable")
                    self.boton15.config(state="disable")
                    self.boton16.config(state="disable")
                    self.boton17.config(state="disable")
                    self.boton18.config(state="disable")
                    self.boton19.config(state="disable")
                    self.boton20.config(state="disable")
                    if self.dificultad=="dificil":
                        self.boton21.config(state="disable")
                        self.boton22.config(state="disable")
                        self.boton23.config(state="disable")
                        self.boton24.config(state="disable")
                        self.boton25.config(state="disable")



    def mostrarvictoria(self):
        self.conta_victoria+=1
        if self.conta_victoria == len(self.palabra_list):
            self.b3_volver.place(self.b3_volver.pi)
            self.b_volver.place_forget()
            self.cancel()
            mixer.music.load("sonido/win.mp3")
            mixer.music.play()
            if self.dificultad=="facil" or self.dificultad=="medio" or self.dificultad=="dificil":
                self.boton1.config(state="disable")
                self.boton2.config(state="disable")
                self.boton3.config(state="disable")
                self.boton4.config(state="disable")
                self.boton5.config(state="disable")
                self.boton6.config(state="disable")
                self.boton7.config(state="disable")
                self.boton8.config(state="disable")
                self.boton9.config(state="disable")
                self.boton10.config(state="disable")
                if self.dificultad=="medio" or self.dificultad=="dificil":
                    self.boton11.config(state="disable")
                    self.boton12.config(state="disable")
                    self.boton13.config(state="disable")
                    self.boton14.config(state="disable")
                    self.boton15.config(state="disable")
                    self.boton16.config(state="disable")
                    self.boton17.config(state="disable")
                    self.boton18.config(state="disable")
                    self.boton19.config(state="disable")
                    self.boton20.config(state="disable")
                    if self.dificultad=="dificil":
                        self.boton21.config(state="disable")
                        self.boton22.config(state="disable")
                        self.boton23.config(state="disable")
                        self.boton24.config(state="disable")
                        self.boton25.config(state="disable")


    def destruir(self):
        self.b_inciar.place(self.b_inciar.pi)
        try:
            self.cancel()
        except ValueError:
            pass
        
        try:
            self.canvas.destroy()
            self.incognita.destroy()
            self.boton1.destroy()
            self.boton2.destroy()
            self.boton3.destroy()
            self.boton4.destroy()
            self.boton5.destroy()
            self.boton6.destroy()
            self.boton7.destroy()
            self.boton8.destroy()
            self.boton9.destroy()
            self.boton10.destroy()
            self.boton11.destroy()
            self.boton12.destroy()
            self.boton13.destroy()
            self.boton14.destroy()
            self.boton15.destroy()
            self.boton16.destroy()
            self.boton17.destroy()
            self.boton18.destroy()
            self.boton19.destroy()
            self.boton20.destroy()
            self.boton21.destroy()
            self.boton22.destroy()
            self.boton23.destroy()
            self.boton24.destroy()
            self.boton25.destroy()
        except AttributeError:
            pass

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.text_timer.configure(text="Perdiste")
            self.mostrarderrota()
        else:
            self.text_timer.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self._job= self.after(1000, self.countdown)

    def cancel(self):
        if self._job is not None:
            self.after_cancel(self._job)
            self._job = None
            PantaJuego.remaining=self.remaining

    def asignar_puntos(self):
        if self.dificultad=="facil":
            self.puntos=120
        elif self.dificultad=="medio":
            self.puntos=240
        elif self.dificultad=="dificil":
            self.puntos=300

    def muca():
        mixer.init()
        mixer.music.load("sonido/theme.mp3")
        mixer.music.play(-1)

    def mute(self):
        if mixer.music.get_busy() == True:
            mixer.music.stop()
            self.sonido.config(image=self.foto2,width=50,height=50)
        else:
            mixer.init()
            mixer.music.load("sonido/theme.mp3")
            mixer.music.play(-1)
            self.sonido.config(image=self.foto1,width=50,height=50)
    
    def callback():
        if messagebox.askokcancel("Salir", "¿Realmente desea salir?"):
            app.destroy()

    def olvidarboton(self):
        self.b2_volver.place_forget()
        self.b3_volver.place_forget()
        self.b_volver.place(self.b_volver.pi)



class PantaPuntua(tk.Frame):

    puntajes=[]

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="PUNTUACIONES" , font=LETRA_GRA2)
        label.pack(pady=50)

        self.lista=[]

        self.cajadepuntos=tk.Listbox(self,font=("ComicSansMS",20,"bold"),width=30,relief="sunken",bg="lightblue",bd=5)
        self.cajadepuntos.pack()


        b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: [controlador.mostrar_frame(MenuJuego),print(self.lista)])
        b_volver.pack(ipadx=50,ipady=10,pady=5)
        b_volver.place(x=400,y=550,anchor="s")

        self.leerpuntajes()
        self.actualiza()
        


    def leerpuntajes(self):
        self.puntajes = []
        with open("puntajes.txt") as f:
            for line in f:
                score, name = line.split('---')
                score = int(score)
                self.puntajes.append((name[0:3],("-"*20),score))

        self.puntajes.sort(key=lambda s: s[2],reverse=True)


    def actualiza(self):
        self.lista=[]
        self.leerpuntajes()
        for i in range(10):
            self.lista.append((i+1,")_",self.puntajes[i]))
        self.cajadepuntos.delete(0,"end")
        for i in self.lista:
            self.cajadepuntos.insert("end",i)
        self.after(100,self.actualiza)

class PantaDificult(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="DIFICULTADES" , font=LETRA_GRA2)
        label.pack(pady=50)

        facil= ttk.Button(self,text="FACIL",command=lambda:[controlador.mostrar_frame2(PantaJuego),self.cambiadificultad(1)])
        facil.pack(pady=20,ipady=20,ipadx=40)

        normal= ttk.Button(self,text="NORMAL",command=lambda:[controlador.mostrar_frame2(PantaJuego),self.cambiadificultad(2)])
        normal.pack(pady=20,ipady=20,ipadx=40)

        dificil= ttk.Button(self,text="DIFICIL",command=lambda:[controlador.mostrar_frame2(PantaJuego),self.cambiadificultad(3)])
        dificil.pack(pady=20,ipady=20,ipadx=40)

        b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        b_volver.pack(ipadx=50,ipady=10,pady=5)
        b_volver.place(x=400,y=550,anchor="s")
    
    def cambiadificultad(self,cont):
        if cont == 1:
            PantaJuego.dificultad="facil"
        elif cont == 2:
            PantaJuego.dificultad="medio"
        elif cont == 3:
            PantaJuego.dificultad="dificil"

class PantaDerrota(tk.Frame):
    
    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="DERROTA" , font=LETRA_GRA2)
        label.pack()

        self.canvas=tk.Canvas(self,width=310,height=330)
        self.canvas.pack()
        self.secuencia = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(r"imagenes/082.gif"))]
        self.image = self.canvas.create_image(155,165,image=self.secuencia[0])

        self.puntuacion = ttk.Label(self, text="%d" % PantaJuego.remaining , font=LETRA_NOR)
        self.puntuacion.pack()
        self.puntuacion.place(x=480,y=450,anchor="e")

        label = ttk.Label(self, text="Tu nombre" , font=LETRA_NOR)
        label.pack()
        label.place(x=410,y=400,anchor="e")

        label1 = ttk.Label(self, text="Tus puntos:" , font=LETRA_NOR)
        label1.pack()
        label1.place(x=410,y=450,anchor="e")
        
        self.animate(1)

        self.entrada_nombre = tk.Entry(self)
        self.entrada_nombre.pack()
        self.entrada_nombre.place(x=410,y=400,anchor="w")
        self.entrada_nombre.focus_set()


        self.b_entrada= ttk.Button(self , text="Guardar" ,
            command=lambda: [self.guarda_puntaje(), controlador.mostrar_frame(PantaPuntua)])
        self.b_entrada.pack()
        self.b_entrada.place(x=400,y=500,anchor="s")

        b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        b_volver.pack(ipadx=50,ipady=10,pady=5)
        b_volver.place(x=400,y=550,anchor="s")
        
        self.actualizapunatuacion()
    
        b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        b_volver.pack(ipadx=50,ipady=10,pady=5)
        b_volver.place(x=400,y=550,anchor="s")

    def guarda_puntaje(self):
        try:
            baseda=open("puntajes.txt",'r')
            baseda.close()
        except IOError:
            baseda=open("puntajes.txt",'w')
            baseda.close()

        baseda=open("puntajes.txt",'a')
        baseda.write(str(PantaJuego.remaining)+"---"+self.entrada_nombre.get()+"\n")
        baseda.close()

    def actualizapunatuacion(self,cont=None):
        if cont==None:
            self.puntuacion.configure(text="%d" % PantaJuego.remaining,font=LETRA_NOR)
            self.after(1000, self.actualizapunatuacion)

        
    def animate(self,a):
        self.canvas.itemconfig(self.image, image=self.secuencia[a])
        self.after(100,lambda: self.animate((a+1) % len(self.secuencia)))

class PantaVictoria(tk.Frame):
    
    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        # gif1 = tk.PhotoImage(file = 'imagenes/victoria.gif',format="gif -index 2")
        self.canvas=tk.Canvas(self,width=500,height=400)
        self.canvas.pack()
        self.secuencia = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(r"imagenes/victoria.gif"))]
        self.image = self.canvas.create_image(250,200,image=self.secuencia[0])
        
        label = ttk.Label(self, text="Tu nombre" , font=LETRA_NOR)
        label.pack()
        label.place(x=410,y=400,anchor="e")

        label1 = ttk.Label(self, text="Tus puntos:" , font=LETRA_NOR)
        label1.pack()
        label1.place(x=410,y=450,anchor="e")


        self.puntuacion = ttk.Label(self, text="%d" % PantaJuego.remaining , font=LETRA_NOR)
        self.puntuacion.pack()
        self.puntuacion.place(x=480,y=450,anchor="e")
        
        self.animate(1)

        self.entrada_nombre = tk.Entry(self)
        self.entrada_nombre.pack()
        self.entrada_nombre.place(x=410,y=400,anchor="w")
        self.entrada_nombre.focus_set()


        self.b_entrada= ttk.Button(self , text="Guardar" ,
            command=lambda: [self.guarda_puntaje(), controlador.mostrar_frame(PantaPuntua)])
        self.b_entrada.pack()
        self.b_entrada.place(x=400,y=500,anchor="s")

        b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        b_volver.pack(ipadx=50,ipady=10,pady=5)
        b_volver.place(x=400,y=550,anchor="s")
        
        self.actualizapunatuacion()
    
    def guarda_puntaje(self):
        try:
            baseda=open("puntajes.txt",'r')
            baseda.close()
        except IOError:
            baseda=open("puntajes.txt",'w')
            baseda.close()

        baseda=open("puntajes.txt",'a')
        baseda.write(str(PantaJuego.remaining)+"---"+self.entrada_nombre.get()+"\n")
        baseda.close()
        
    def animate(self,a):
        self.canvas.itemconfig(self.image, image=self.secuencia[a])
        self.after(250,lambda: self.animate((a+1) % len(self.secuencia)))

    def actualizapunatuacion(self,cont=None):
        if cont==None:
            self.puntuacion.configure(text="%d" % PantaJuego.remaining,font=LETRA_NOR)
            self.after(1000, self.actualizapunatuacion)


        
        
        

app=Ahorcado()
app.geometry("800x600")
app.resizable(False, False)
app.protocol("WM_DELETE_WINDOW", PantaJuego.callback)


app.mainloop()
