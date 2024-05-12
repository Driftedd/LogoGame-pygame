#--------------------------------[Imports]--------------------------------#
import pygame
import sys
import random
import time
import math

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

# Logos incompletos:
Pepsi_Incompleto = pygame.image.load("Media/Marcas_Incompletas/pepsi.png").convert_alpha()
McDonalds_Incompleto = pygame.image.load("Media/Marcas_Incompletas/mcdonalds.png").convert_alpha()
BurgerKing_Incompleto = pygame.image.load("Media/Marcas_Incompletas/burger-king.png").convert_alpha()
logitech_Incompleto = pygame.image.load("Media/Marcas_Incompletas/logitech.png").convert_alpha()
spotify_Incompleto = pygame.image.load("Media/Marcas_Incompletas/spotify.png").convert_alpha()
starbucks_Incompleto = pygame.image.load("Media/Marcas_Incompletas/starbucks.png").convert_alpha()
youtube_Incompleto = pygame.image.load("Media/Marcas_Incompletas/youtube.png").convert_alpha()


Lista=[[Pepsi,Pepsi_Incompleto],[McDonalds,McDonalds_Incompleto],[BurgerKing,BurgerKing_Incompleto],[logitech,logitech_Incompleto],[spotify,spotify_Incompleto],[starbucks,starbucks_Incompleto],[youtube,youtube_Incompleto]]
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
    random.shuffle(Lista)
    imagen_oculta = Lista[i][1]
    return imagen_oculta


#--------------------------------[Game]--------------------------------#
while True:
    Mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Mouse[0] > 1125 and Mouse[0] < 1325 and Mouse[1] > 190 and Mouse[1] < 250:
                point += 1
                level = 2
            if Mouse[0] > 1125 and Mouse[0] < 1325 and Mouse[1] > 290 and Mouse[1] < 350:
                point -= 1
            if Mouse[0] > 1125 and Mouse[0] < 1325 and Mouse[1] > 390 and Mouse[1] < 450:
                point -= 1


    if level == 1:
        screen.blit(Fondo,(0,0))
        screen.blit(Pepsi_Incompleto,(text_x_pos,text_y_pos))
        pygame.draw.rect(screen, (80,104,242), guess1_button, 0)
        pygame.draw.rect(screen, (80,104,242), guess2_button, 0)
        pygame.draw.rect(screen, (80,104,242), guess3_button, 0)
        screen.blit(guess1,(1150,200))
        screen.blit(guess2,(1150,300))
        screen.blit(guess3,(1150,400))
        screen.blit(Opciones,(1080,30))
        screen.blit(Logo,(320,750))
        point_render = Font_Minecraft.render(f"{point}",False,"White")
        screen.blit(point_render,(1500,700))
        timer_animation, text_y_pos = animacionLogo(timer_animation,text_y_pos)

    elif level == 2:
        screen.blit(Fondo,(0,0))
        screen.blit(McDonalds_Incompleto,(text_x_pos,text_y_pos))
        screen.blit(Opciones,(1080,30))
        screen.blit(Logo,(320,750))
        point_render = Font_Minecraft.render(f"{point}",False,"White")
        screen.blit(point_render,(1500,700))
        timer_animation, text_y_pos = animacionLogo(timer_animation,text_y_pos)

    elif level == 3:
        screen.blit(Fondo,(0,0))
        screen.blit(McDonalds_Incompleto,(text_x_pos,text_y_pos))
        screen.blit(Opciones,(1080,30))
        screen.blit(Logo,(320,750))
        point_render = Font_Minecraft.render(f"{point}",False,"White")
        screen.blit(point_render,(1500,700))
        timer_animation, text_y_pos = animacionLogo(timer_animation,text_y_pos)

    elif level == 4:
        screen.blit(Fondo,(0,0))
        screen.blit(McDonalds_Incompleto,(text_x_pos,text_y_pos))
        screen.blit(Opciones,(1080,30))
        screen.blit(Logo,(320,750))
        point_render = Font_Minecraft.render(f"{point}",False,"White")
        screen.blit(point_render,(1500,700))
        timer_animation, text_y_pos = animacionLogo(timer_animation,text_y_pos)

    elif level == 5:
        screen.blit(Fondo,(0,0))
        screen.blit(McDonalds_Incompleto,(text_x_pos,text_y_pos))
        screen.blit(Opciones,(1080,30))
        screen.blit(Logo,(320,750))
        point_render = Font_Minecraft.render(f"{point}",False,"White")
        screen.blit(point_render,(1500,700))
        timer_animation, text_y_pos = animacionLogo(timer_animation,text_y_pos)



    pygame.display.update()
    clock.tick(60)#