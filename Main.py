#--------------------------------[Imports]--------------------------------#
import pygame
import sys
import random
import time
import math
#--------------------------------[Funciones]--------------------------------#
def animacionLogo(timer_animation,text_y_pos):
    timer_animation += 1
    if text_y_pos == 70 and timer_animation < 15:
        text_y_pos= 65
    elif text_y_pos == 65 and timer_animation > 15 and timer_animation < 30:
        text_y_pos = 60
    elif text_y_pos == 60 and timer_animation > 30 and timer_animation < 45:
        text_y_pos = 65
    elif text_y_pos == 65 and timer_animation > 45:
        text_y_pos = 70
    elif timer_animation >= 60:
        timer_animation = 0
    return timer_animation, text_y_pos

def imageChoice(Lista,i):
    imagen_oculta = Lista[i][1]
    return imagen_oculta
#--------------------------------[Pre-Game]--------------------------------#
pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Quiz Logo")
clock = pygame.time.Clock()
Font_Daydream_30 = pygame.font.Font("Media/Font_Daydream.ttf", 30)
Font_Daydream_100 = pygame.font.Font("Media/Font_Daydream.ttf", 100)
Font_Minecraft = pygame.font.Font("Media/Font_Minecraft.ttf",50)
text_x_pos = 230
text_y_pos = 70

# Logos completos:
Pepsi = pygame.image.load("Media/Marcas/pepsi.png").convert_alpha()
McDonalds = pygame.image.load("Media/Marcas/mcdonalds.png").convert_alpha()
BurgerKing = pygame.image.load("Media/Marcas/burger-king.png").convert_alpha()
logitech = pygame.image.load("Media/Marcas/logitech.png").convert_alpha()
spotify = pygame.image.load("Media/Marcas/spotify.png").convert_alpha()
starbucks = pygame.image.load("Media/Marcas/starbucks.png").convert_alpha()
youtube = pygame.image.load("Media/Marcas/youtube.png").convert_alpha()
python = pygame.image.load("Media/Marcas/python.png").convert_alpha()
apple = pygame.image.load("Media/Marcas/apple.png").convert_alpha()
_3m = pygame.image.load("Media/Marcas/3m.png").convert_alpha()

# Logos incompletos:
Pepsi_Incompleto = pygame.image.load("Media/Marcas_Incompletas/pepsi.png").convert_alpha()
McDonalds_Incompleto = pygame.image.load("Media/Marcas_Incompletas/mcdonalds.png").convert_alpha()
BurgerKing_Incompleto = pygame.image.load("Media/Marcas_Incompletas/burger-king.png").convert_alpha()
logitech_Incompleto = pygame.image.load("Media/Marcas_Incompletas/logitech.png").convert_alpha()
spotify_Incompleto = pygame.image.load("Media/Marcas_Incompletas/spotify.png").convert_alpha()
starbucks_Incompleto = pygame.image.load("Media/Marcas_Incompletas/starbucks.png").convert_alpha()
youtube_Incompleto = pygame.image.load("Media/Marcas_Incompletas/youtube.png").convert_alpha()
python_Incompleto = pygame.image.load("Media/Marcas_Incompletas/python.png").convert_alpha()
apple_Incompleto = pygame.image.load("Media/Marcas_Incompletas/apple.png").convert_alpha()
_3m_Incompleto = pygame.image.load("Media/Marcas_Incompletas/3m.png").convert_alpha()

# Setup
Lista=[[Pepsi,Pepsi_Incompleto],[McDonalds,McDonalds_Incompleto],[BurgerKing,BurgerKing_Incompleto],[logitech,logitech_Incompleto],[spotify,spotify_Incompleto],[starbucks,starbucks_Incompleto],[youtube,youtube_Incompleto],[python,python_Incompleto],[apple,apple_Incompleto],[_3m,_3m_Incompleto]]
Fondo = pygame.image.load("Media/Fondo.png").convert()
guess1 = Font_Minecraft.render("PEPSI",False,"White")
guess2 = Font_Minecraft.render("SPOTIFY",False,"White")
guess3 = Font_Minecraft.render("FORD",False,"White")
Opciones = Font_Daydream_30.render("Elija su respuesta:",False,"aquamarine")
Logo = Font_Daydream_100.render("Logo",False,"aquamarine")
timer_animation = 0
point = 0
guess1_button = pygame.Rect(1125,190,200,60)
guess2_button = pygame.Rect(1125,290,200,60)
guess3_button = pygame.Rect(1125,390,200,60)
level=1
exitosas=0
random.shuffle(Lista)

'''
'''

#si el usuario es admin se abre la configuracion, si es cualquier otra cosa se abre el juego
USER="admin"

'''
'''


# Admin
Nivel_text = Font_Daydream_30.render("Nivel:",False,"aquamarine")

CantLogos_text = Font_Daydream_30.render("Logos:",False,"aquamarine")
tiempo_text = Font_Daydream_30.render("Tiempo:",False,"aquamarine")
Config_text = Font_Daydream_30.render("CONFIGURACION",False,"aquamarine")
tiempo_button=pygame.Rect(225,250,150,40)
CantLogos_button=pygame.Rect(660,250,150,40)


# --------------------------------[Game]--------------------------------#
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if guess1_button.collidepoint(event.pos):
                exitosas += 1
            elif guess2_button.collidepoint(event.pos):
                exitosas -= 1
            elif guess3_button.collidepoint(event.pos):
                exitosas -= 1
    
    if USER=="admin":
        screen.blit(Fondo,(0,0))
        screen.blit(Config_text, (300,100))
        screen.blit(tiempo_text,(200,200))
        screen.blit(CantLogos_text, (650,200))
        
        pygame.draw.rect(screen,(80,104,242),tiempo_button, 3)
        pygame.draw.rect(screen,(80,104,242),CantLogos_button, 3)
        
        
    else:
        if exitosas <= 10 and exitosas >= 0:
            imagen = imageChoice(Lista, exitosas)
            screen.blit(Fondo, (0, 0))
            screen.blit(imagen, (text_x_pos, text_y_pos))
            pygame.draw.rect(screen, (80, 104, 242), guess1_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess2_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess3_button, 0)
            screen.blit(guess1, (1150, 200))
            screen.blit(guess2, (1150, 300))
            screen.blit(guess3, (1150, 400))
            screen.blit(Opciones, (1080, 30))
            screen.blit(Logo, (320, 750))
            point_render = Font_Minecraft.render(f"{exitosas}", False, "White")
            screen.blit(point_render, (1500, 700))
            timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)

        elif exitosas > 10 and exitosas <= 30:
            imagen = imageChoice(Lista, exitosas)
            screen.blit(Fondo, (0, 0))
            screen.blit(imagen, (text_x_pos, text_y_pos))
            pygame.draw.rect(screen, (80, 104, 242), guess1_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess2_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess3_button, 0)
            screen.blit(guess1, (1150, 200))
            screen.blit(guess2, (1150, 300))
            screen.blit(guess3, (1150, 400))
            screen.blit(Opciones, (1080, 30))
            screen.blit(Logo, (320, 750))
            point_render = Font_Minecraft.render(f"{exitosas}", False, "White")
            screen.blit(point_render, (1500, 700))
            timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)

        elif exitosas > 30 and exitosas <= 60:
            imagen = imageChoice(Lista, exitosas)
            screen.blit(Fondo, (0, 0))
            screen.blit(imagen, (text_x_pos, text_y_pos))
            pygame.draw.rect(screen, (80, 104, 242), guess1_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess2_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess3_button, 0)
            screen.blit(guess1, (1150, 200))
            screen.blit(guess2, (1150, 300))
            screen.blit(guess3, (1150, 400))
            screen.blit(Opciones, (1080, 30))
            screen.blit(Logo, (320, 750))
            point_render = Font_Minecraft.render(f"{exitosas}", False, "White")
            screen.blit(point_render, (1500, 700))
            timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)

        elif exitosas > 60 and exitosas <= 100:
            imagen = imageChoice(Lista, exitosas)
            screen.blit(Fondo, (0, 0))
            screen.blit(imagen, (text_x_pos, text_y_pos))
            pygame.draw.rect(screen, (80, 104, 242), guess1_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess2_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess3_button, 0)
            screen.blit(guess1, (1150, 200))
            screen.blit(guess2, (1150, 300))
            screen.blit(guess3, (1150, 400))
            screen.blit(Opciones, (1080, 30))
            screen.blit(Logo, (320, 750))
            point_render = Font_Minecraft.render(f"{exitosas}", False, "White")
            screen.blit(point_render, (1500, 700))
            timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)

        elif exitosas > 100 and exitosas <= 150:
            imagen = imageChoice(Lista, exitosas)
            screen.blit(Fondo, (0, 0))
            screen.blit(imagen, (text_x_pos, text_y_pos))
            pygame.draw.rect(screen, (80, 104, 242), guess1_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess2_button, 0)
            pygame.draw.rect(screen, (80, 104, 242), guess3_button, 0)
            screen.blit(guess1, (1150, 200))
            screen.blit(guess2, (1150, 300))
            screen.blit(guess3, (1150, 400))
            screen.blit(Opciones, (1080, 30))
            screen.blit(Logo, (320, 750))
            point_render = Font_Minecraft.render(f"{exitosas}", False, "White")
            screen.blit(point_render, (1500, 700))
            timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)

    pygame.display.update()
    clock.tick(60)

    #Cambio necesario, se puede borrar esta linea de codigo
    javier = "god"
    steven="god"
    josue="god"
    lun="god"