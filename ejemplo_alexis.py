from random import randint
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
    list_word=list()
    abc=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z')
    palabra = ''

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        
        label = ttk.Label(self, text="Ahorcado" , font=LETRA_GRA2)
        label.place(relx=0.5,y=50,anchor="center")
        
        label = ttk.Label(self, text="Tabla de letras" , font=LETRA_NOR)
        label.place(x=550,y=100, anchor="w")

        self.letra_bot()
        boton1= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton1.place(x=550,y=200, anchor="w",width=50)
        
        self.letra_bot()
        boton2= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton2.place(x=600,y=200, anchor="w",width=50)
        
        self.letra_bot()
        boton3= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton3.place(x=550,y=250, anchor="w",width=50)
        
        self.letra_bot()
        boton4= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton4.place(x=600,y=250, anchor="w",width=50)

        self.letra_bot()
        boton5= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton5.place(x=550,y=300, anchor="w",width=50)
        
        self.letra_bot()
        boton6= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton6.place(x=600,y=300, anchor="w",width=50)
        
        self.letra_bot()
        boton7= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton7.place(x=550,y=350, anchor="w",width=50)
        
        self.letra_bot()
        boton8= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton8.place(x=600,y=350, anchor="w",width=50)

        self.letra_bot()
        boton9= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton9.place(x=550,y=400, anchor="w",width=50)
        
        self.letra_bot()
        boton10= ttk.Button(self , text=self.text_bot ,
            command=quit)
        boton10.place(x=600,y=400, anchor="w",width=50)

        self.carga_txt()
        self.incognita_guiones()

        incognita = tk.Label(self,text = self.palabra, font=LETRA_NOR)
        incognita.place(x=200,y=400)

    def carga_txt(self):
        palabras = open('ahorcado_5.txt','r')
        listPalabras = palabras.readlines()
        palabras.close()
        i = randint(0,600)
        self.palabra = listPalabras[i]
        return self.palabra

    def incognita_guiones(self):
        longpalabra = len(self.palabra)
        self.palabra = '_ '*(longpalabra-1)
        return self.palabra


    def letra_bot(self):

        index=randint(0,26)
        self.text_bot=self.abc[index]
        return self.text_bot




app=Ahorcado()
app.geometry("800x600")


app.mainloop()
































# import pygame

# pygame.init()


# display_width = 800
# display_height = 600
# black = (0,0,0)
# white = (255,255,255)
# red = (200,0,0)
# green = (0,200,0)

# gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('SuperMegaEquipo')
# clock = pygame.time.Clock()
# gameDisplay.fill(white)

# def text_objects(text, font):
#     textSurface = font.render(text, True, black)
#     return textSurface, textSurface.get_rect()

# def game_intro():

#     intro = True

#     while intro:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
                
#         gameDisplay.fill(white)
#         largeText = pygame.font.SysFont("comicsansms",90)
#         TextSurf, TextRect = text_objects("Ahorcado", largeText)
#         TextRect.center = ((display_width/2),(display_height/10))
#         gameDisplay.blit(TextSurf, TextRect)



#         pygame.draw.rect(gameDisplay, green,((display_width/4),(display_height/3),400,50))
#         pygame.draw.rect(gameDisplay, green,((display_width/4),(display_height/3+100),400,50))
#         pygame.draw.rect(gameDisplay, green,((display_width/4),(display_height/3+200),400,50))
#         pygame.draw.rect(gameDisplay, green,((display_width/4),(display_height/3+300),400,50))


#         pygame.display.update()
#         clock.tick(15)
# game_intro()

# pygame.quit()
# quit()

