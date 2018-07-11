import tkinter as tk
from tkinter import ttk

LETRA_GRA=("Verdana",113)



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
            frame.grid(row=0 , column=0 , sticky="NSEW")
        
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
    def __init__(self, padre, controlador):
        tk.Frame.__init__(self,padre)
        label = ttk.Label(self, text="Ahorcado" , font=LETRA_GRA)
        label.pack(pady=30,padx=30)

        boton5= ttk.Button(self , text="Volver" ,
            command=lambda: controlador.mostrar_frame(MenuJuego))
        boton5.pack()



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