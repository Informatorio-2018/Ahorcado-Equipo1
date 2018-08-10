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
        for F in (MenuJuego, PantaJuego,PantaPuntua,PantaDificult,PantaDerrota,ConfirmarSalida):
            frame = F(contenedor,self)
            self.frames[F] = frame
            frame.grid(row=0 , column=0 , sticky="nsew")

        self.mostrar_frame(MenuJuego)
        ###############################################################

    def mostrar_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()

#################### Pantalla de Menu #############################
class MenuJuego(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="Ahorcado" , font=LETRA_GRA)
        label.pack(pady=80)

        s = ttk.Style()
        s.configure('my.TButton', font= 15)

        boton1= ttk.Button(self , text="Jugar" ,style='my.TButton',
            command=lambda: controlador.mostrar_frame(PantaJuego))
        boton1.pack(ipadx=50,ipady=10,pady=5)

        boton2= ttk.Button(self , text="Puntuacion" ,style='my.TButton',
            command=lambda: controlador.mostrar_frame(PantaPuntua))
        boton2.pack(ipadx=50,ipady=10,pady=5)

        boton3= ttk.Button(self , text="Dificultad" ,style='my.TButton',
            command=lambda: controlador.mostrar_frame(PantaDificult))
        boton3.pack(ipadx=50,ipady=10,pady=5)

        boton4= ttk.Button(self , text="Salir" ,style='my.TButton',
            command=lambda: controlador.mostrar_frame(ConfirmarSalida))
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

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)

        label = ttk.Label(self, text="Ahorcado" , font=LETRA_GRA2)
        label.place(relx=0.5,y=50,anchor="center")

        self.carga_txt()

        self.remaining = 0

        # BOTONES
        #################################################################
        label = ttk.Label(self, text="Tabla de letras" , font=LETRA_NOR)
        label.place(x=550,y=100, anchor="w")

        self.letra_bot(1)
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

        self.b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        self.b_volver.pack(ipadx=50,ipady=10,pady=5)
        self.b_volver.place(x=400,y=550,anchor="s")

        #############################################################3

        self.incognita_guiones()

        self.incognita = tk.Label(self,text = self.palabra, font=LETRA_NOR)
        self.incognita.place(x=200,y=400)

        self.monigote = tk.PhotoImage(file="imagenes/horca.png")
        self.canvas = tk.Label(self,image=self.monigote)
        self.canvas.pack()
        self.canvas.place(x=250,y=150)

        text_score = ttk.Label(self,text="Puntuacion: ",font=13)
        text_score.pack()
        text_score.place(x=350,y=500,anchor="s")

        self.text_timer = tk.Label(self,text="",font=13)
        self.text_timer.pack()
        self.text_timer.place(x=420,y=500,anchor="s")

        self.countdown(10)

        self.b2_volver= ttk.Button(self , text="Perdiste" ,
            command=lambda: controlador.mostrar_frame(PantaDerrota))
        self.b2_volver.pack(ipadx=50,ipady=10,pady=5)
        self.b2_volver.place(x=400,y=550,anchor="s")
        self.b2_volver.pi=self.b2_volver.place_info()
        self.b2_volver.place_forget()

        # FUNCIONES
        ###############################################################3


    def carga_txt(self):

        # Carga un palabra random desde ahorcado.txt
        palabras = open('ahorcado_5.txt','r')
        listPalabras = palabras.readlines()
        palabras.close()
        i = randint(0,30)
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
        while len(self.list_word)!=25:
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
                self.Cambio3De_Guio(a)

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
            self.mostrarderrota()

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.text_timer.configure(text="Perdiste")
        else:
            self.text_timer.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def mostrarderrota(self):
        self.b2_volver.place(self.b2_volver.pi)
        self.b_volver.place_forget()

class PantaPuntua(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="PUNTUACIONES" , font=LETRA_GRA2)
        label.pack(pady=50)


        for i in range(10):
            tk.Label(self,text="text-1000000",font=20).pack(pady=5)


        b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        b_volver.pack(ipadx=50,ipady=10,pady=5)
        b_volver.place(x=400,y=550,anchor="s")

class PantaDificult(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="DIFICULTADES" , font=LETRA_GRA2)
        label.pack(pady=50)

        facil= ttk.Button(self,text="FACIL")
        facil.pack(pady=20,ipady=20,ipadx=40)

        normal= ttk.Button(self,text="NORMAL")
        normal.pack(pady=20,ipady=20,ipadx=40)

        dificil= ttk.Button(self,text="DIFICIL")
        dificil.pack(pady=20,ipady=20,ipadx=40)

        b_volver= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        b_volver.pack(ipadx=50,ipady=10,pady=5)
        b_volver.place(x=400,y=550,anchor="s")

class ConfirmarSalida(tk.Frame):
        def __init__(self, padre, controlador):
            tk.Frame.__init__(self,padre)
            label = ttk.Label(self, text="¿ESTA SEGURO DE QUE DESEA SALIR?" , font=LETRA_GRA2)
            label.pack(pady=50)
            b_si=tk.Button(self , text="SI" , command= quit,font=LETRA_GRA2,width=5)
            b_si.pack(pady=50)
            b_no=tk.Button(self , text="NO" , command= lambda: controlador.mostrar_frame(MenuJuego),font=LETRA_GRA2,width=5)
            b_no.pack(pady=50)

class PantaDerrota(tk.Frame):
    
    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="DERROTA" , font=LETRA_GRA2)
        label.pack(pady=50)

        label2 = ttk.Label(self, text="DERROTA" , font=LETRA_NOR)
        label2.pack()

        label3 = ttk.Label(self, text="DERROTA" , font=LETRA_NOR)
        label3.pack()


app=Ahorcado()
app.geometry("800x600")
app.resizable(False, False)

app.mainloop()
