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
    text_oculto = Lista[i][2]
    return imagen_oculta, text_oculto

def textoRandomizador(opcion,Lista,lugar,lugar2,lugar3):
    if lugar == 1:
        guess1 = opcion
        guess2 = Lista[lugar2][2]
        guess3 = Lista[lugar3][2]
        tr1 = 1
        tr2 = -1
        tr3 = -1
    elif lugar == 2:
        guess2 = opcion
        guess1 = Lista[lugar2][2]
        guess3 = Lista[lugar3][2]
        tr1 = -1
        tr2 = 1
        tr3 = -1
    else:
        guess3 = opcion
        guess1 = Lista[lugar2][2]
        guess2 = Lista[lugar3][2]
        tr1 = -1
        tr2 = -1
        tr3 = 1
    return guess1,guess2,guess3,tr1,tr2,tr3

def randomizer(exitosas):
    lugar = random.randint(1,3)
    lugar2 = random.randint(0,8)
    lugar3 = random.randint(0,8)
    while lugar3 == exitosas or lugar2 == exitosas or lugar3 == lugar2:
        lugar2 = random.randint(0,8)
        lugar3 = random.randint(0,8)
    return lugar,lugar2,lugar3


#--------------------------------[Pre-Game]--------------------------------#
pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Quiz Logo")
clock = pygame.time.Clock()
Font_Daydream_20 = pygame.font.Font("Media/Font_Daydream.ttf", 20)
Font_Daydream_30 = pygame.font.Font("Media/Font_Daydream.ttf", 30)
Font_Daydream_50 = pygame.font.Font("Media/Font_Daydream.ttf", 50)
Font_Daydream_100 = pygame.font.Font("Media/Font_Daydream.ttf", 100)
Font_Minecraft = pygame.font.Font("Media/Font_Minecraft.ttf",50)
text_x_pos = 230
text_y_pos = 70

# Logos completos:
# 1
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
# 2
_7up = 0
adidas = 0
amazon = 0.
bmw = 0
duckduckgo = 0
ea = 0
fanta = 0
hasbro = 0
jacks = 0
kfc = 0
lego = 0
monster = 0
netflix = 0
nfl = 0
jrockets = 0
sega = 0
spacex = 0
utorrent = 0
tosty = 0
vscode = 0

# 3
adobe = 0
autodesk = 0
balance = 0
blackberry = 0
chevro = 0
coke = 0
delMonte = 0
discord = 0
dreamworks = 0
facebook = 0
hulu = 0
microsoft = 0
motorola = 0
moyo = 0
nascar = 0
nike = 0
nintendo = 0
nissan = 0
office = 0
pyg = 0
pizzahut = 0
purina = 0
rayovac = 0
razer = 0
safari = 0
siman=0
sprite=0
tacobell=0
toyota=0
vlc=0

# Logos incompletos:
# 1
Pepsi_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/pepsi.png").convert_alpha()
McDonalds_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/mcdonalds.png").convert_alpha()
BurgerKing_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/burger-king.png").convert_alpha()
logitech_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/logitech.png").convert_alpha()
spotify_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/spotify.png").convert_alpha()
starbucks_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/starbucks.png").convert_alpha()
youtube_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/youtube.png").convert_alpha()
python_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/python.png").convert_alpha()
apple_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/apple.png").convert_alpha()
_3m_Incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel1/3m.png").convert_alpha()
# 2
_7up_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/7up.png").convert_alpha()
adidas_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/adidas.png").convert_alpha()
amazon_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/amazon.png").convert_alpha()
bmw_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/bmw.png").convert_alpha()
duckgo_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/duckduckgo.png").convert_alpha()
ea_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/ea.png").convert_alpha()
fanta_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/fanta.png").convert_alpha()
hasbro_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/hasbro.png").convert_alpha()
jacks_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/jacks.png").convert_alpha()
kfc_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/kfc.png").convert_alpha()
lego_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/lego.png").convert_alpha()
monster_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/monster.png").convert_alpha()
netflix_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/netflix.png").convert_alpha()
nfl_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/nfl.png").convert_alpha()
jrockets_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel2/rockets.png").convert_alpha()
sega_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel2/sega.png").convert_alpha()
spacex_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel2/space.png").convert_alpha()
utorrent_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel2/torrent.png").convert_alpha()
tosty_incompleto  =pygame.image.load("Media/Marcas_Incompletas/Nivel2/tosty.png").convert_alpha()
vscode_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel2/vscode.png").convert_alpha()
#3
adobe_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/adobe.png").convert_alpha()
autodesk_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel3/autodesk.png").convert_alpha()
balance_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel3/balance.png").convert_alpha()
blackberry_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel3/blackberry.png").convert_alpha()
chevro_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel3/chevro.png").convert_alpha()
coke_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel3/coke.png").convert_alpha()
delMonte_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel3/delMonte.png").convert_alpha()
discord_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel3/discord.png").convert_alpha()
dreamworks_incompleto =pygame.image.load("Media/Marcas_Incompletas/Nivel3/dreamworks.png").convert_alpha()
facebook_incompleto=pygame.image.load("Media/Marcas_Incompletas/Nivel3/facebook.png").convert_alpha()
hulu_incompleto=pygame.image.load("Media/Marcas_Incompletas/Nivel3/hulu.png").convert_alpha()
microsoft_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/microsoft.png").convert_alpha()
motorola_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/motorola.png").convert_alpha()
moyo_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/moyo.png").convert_alpha()
nascar_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/nascar.png").convert_alpha()
nike_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/nike.png").convert_alpha()
nintendo_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/nintendo.png").convert_alpha()
nissan_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/nissan.png").convert_alpha()
office_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/office.png").convert_alpha()
pyg_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/p&g.png").convert_alpha()
pizzahut_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/pizzahut.png").convert_alpha()
purina_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/purina.png").convert_alpha()
rayovac_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/rayovac.png").convert_alpha()
razer_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/razer.png").convert_alpha()
safari_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/safari.png").convert_alpha()
siman_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/siman.png").convert_alpha()
sprite_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/sprite.png").convert_alpha()
tacobell_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/tacobell.png").convert_alpha()
toyota_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/toyota.png").convert_alpha()
vlc_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel3/vlc.png").convert_alpha()


# Strings Nivel1
BurgerKing_str = "BurgerKing"
starbucks_str = "Starbucks" 
McDonalds_str ="McDonalds"
logitech_str = "Logitech"
spotify_str = "Spotify"
youtube_str ="YouTube"
python_str = "Python"
Pepsi_str = "Pepsi"
apple_str ="Apple"
_3m_str = "3M"


# Strings Nivel2
_7up_str="7up"
adidas_str="Adidas"
amazon_str="Amazon"
bmw_str="BMW"
duckgi_str="Duckgo"
ea_str="EA"
fanta_str="Fanta"
hasbro_str="Hasbro"
jacks_str="Jacks"
kfc_str="KFC"
lego_str="LEGO"
monster_str="Monster"
netflix_str="Netflix"
nfl_str="NFL"
jrockets_str="J. Rockets"
sega_str="SEGA"
spacex_str="SpaceX"
utorrent_str="UTorrent"
tosty_str="Tosty"
vscode_str="VSCode"

#Strings Nivel3
adobe_str="Adobe"
autodesk_str="Autodesk"
balance_str="Balance"
blackberry_str="BlackBerry"
chevro_str="Chevrolet"
coke_str="Coke"
delMonte_str="Del Monte"
discord_str="Discord"
dreamworks_str="Dreamworks"
facebook_str = "Facebook"
hulu_str = "Hulu"
microsoft_str = "Microsoft"
motorola_str = "Motorola"
moyo_str = "Moyo"
nascar_str = "Nascar"
nike_str = "Nike"
nintendo_str = "Nintendo"
nissan_str = "Nissan"
office_str = "Office"
pyg_str = "P&G"
pizzahut_str = "Pizzahut"
purina_str = "Purina"
rayovac_str = "Rayovac"
razer_str = "Razer"
safari_str = "Safari"
siman_str = "Siman"
sprite_str = "Sprite"
tacobell_str = "TacoBell"
toyota_str = "Toyota"
vlc_str = "VLC"
# Tiempos
P_TiempoTardado = 0
M_TiempoTardado = 0
B_TiempoTardado = 0
L_TiempoTardado = 0
S_TiempoTardado = 0
SB_TiempoTardado = 0
YT_TiempoTardado = 0
PY_TiempoTardado = 0
A_TiempoTardado = 0
M3_TiempoTardado = 0

# Setup
ListaNivel1=[
    [Pepsi,Pepsi_Incompleto,Pepsi_str,P_TiempoTardado],
    [McDonalds,McDonalds_Incompleto,McDonalds_str,M_TiempoTardado],
    [BurgerKing,BurgerKing_Incompleto,BurgerKing_str,B_TiempoTardado],
    [logitech,logitech_Incompleto,logitech_str,L_TiempoTardado],
    [spotify,spotify_Incompleto,spotify_str,S_TiempoTardado],
    [starbucks,starbucks_Incompleto,starbucks_str,SB_TiempoTardado],
    [youtube,youtube_Incompleto,youtube_str,YT_TiempoTardado],
    [python,python_Incompleto,python_str,PY_TiempoTardado],
    [apple,apple_Incompleto,apple_str,A_TiempoTardado],
    [_3m,_3m_Incompleto,_3m_str,M3_TiempoTardado]]
random.shuffle(ListaNivel1)

ListaNivel2=[
    [_7up,_7up_incompleto,_7up_str],
    [adidas,adidas_incompleto,adidas_str],
    [amazon,amazon_incompleto,amazon_str],
    [bmw,bmw_incompleto,bmw_str],
    [duckduckgo,duckgo_incompleto,duckgi_str],
    [ea,ea_incompleto,ea_str],
    [fanta,fanta_incompleto,fanta_str],
    [hasbro,hasbro_incompleto,hasbro_str],
    [jacks,jacks_incompleto,jacks_str],
    [kfc,kfc_incompleto,kfc_str],
    [lego,lego_incompleto,lego_str],
    [monster,monster_incompleto,monster_str],
    [nfl,nfl_incompleto,nfl_str],
    [netflix,netflix_incompleto,netflix_str],
    [jrockets,jrockets_incompleto,jrockets_str],
    [sega,sega_incompleto,sega_str],
    [spacex,spacex_incompleto,spacex_str],
    [utorrent,utorrent_incompleto,utorrent_str],
    [vscode,vscode_incompleto,vscode_str],
    [tosty,tosty_incompleto,tosty_str] ]
random.shuffle(ListaNivel2)

ListaNivel3=[
  [adobe, adobe_incompleto, adobe_str],
  [autodesk, autodesk_incompleto, autodesk_str],
  [balance, balance_incompleto, balance_str],
  [blackberry, blackberry_incompleto, blackberry_str],
  [chevro, chevro_incompleto, chevro_str],
  [coke, coke_incompleto, coke_str],
  [delMonte, delMonte_incompleto, delMonte_str],
  [discord, discord_incompleto, discord_str],
  [dreamworks, dreamworks_incompleto, dreamworks_str],
  [facebook, facebook_incompleto, facebook_str],
  [hulu, hulu_incompleto, hulu_str],
  [microsoft, microsoft_incompleto, microsoft_str],
  [motorola, motorola_incompleto, motorola_str],
  [moyo, moyo_incompleto, moyo_str],
  [nascar, nascar_incompleto, nascar_str],
  [nike, nike_incompleto, nike_str],
  [nintendo, nintendo_incompleto, nintendo_str],
  [nissan, nissan_incompleto, nissan_str],
  [office, office_incompleto, office_str],
  [pyg, pyg_incompleto, pyg_str],
  [pizzahut, pizzahut_incompleto, pizzahut_str],
  [purina, purina_incompleto, purina_str],
  [rayovac, rayovac_incompleto, rayovac_str],
  [razer, razer_incompleto, razer_str],
  [safari, safari_incompleto, safari_str],
  [siman, siman_incompleto, siman_str],
  [sprite, sprite_incompleto, sprite_str],
  [tacobell, tacobell_incompleto, tacobell_str],
  [toyota, toyota_incompleto, toyota_str],
  [vlc, vlc_incompleto, vlc_str]
]
random.shuffle(ListaNivel3)

ListaNivel4=[]
random.shuffle(ListaNivel4)

ListaNivel5=[]
random.shuffle(ListaNivel5)

Fondo = pygame.image.load("Media/Fondo.png").convert()
FondoNegro = pygame.image.load("Media/FondoNegro.png").convert_alpha()
Opciones = Font_Daydream_30.render("Elija su respuesta:",False,"aquamarine")
Logo = Font_Daydream_100.render("Logo",False,"aquamarine")
timer_animation = 0
point = 0
guess1_button = pygame.Rect(1125,190,300,60)
guess2_button = pygame.Rect(1125,290,300,60)
guess3_button = pygame.Rect(1125,390,300,60)
level=1
Cantidad_Logos_Admin = 10 #Poner que se cambie 
exitosas=0
tiempo = 60
tempo = 60
lugar,lugar2,lugar3 = randomizer(exitosas)

# Ingreso de usuarios
usuario_input=""
password_input=""
textbox_usuario=pygame.Rect(350,250,300,50)
textbox_password=pygame.Rect(textbox_usuario.x,textbox_usuario.y+125,textbox_usuario.width,textbox_usuario.height)
active_user=False
active_pw=False
ingreso_text=Font_Daydream_50.render("INGRESO DE USUARIOS",False,(5, 150, 131))
usuario_text=Font_Daydream_30.render("USER:",False,(5, 150, 131))
password_text=Font_Daydream_30.render("PASSWORD:",False,(5, 150, 131))
colour1=pygame.Color(20,30,70,255)
colour2=colour1
ingresar_text=Font_Daydream_20.render("Ingresar",False,(5, 150, 131))
ingresar_button=pygame.Rect(400,450,195,40)
noEncontrado_text=Font_Daydream_20.render("Usuario no encontrado!",False,("red"))
crear_text=Font_Daydream_50.render("CREAR  USUARIO",False,(5, 150, 131))
crearUsuario_text=Font_Daydream_20.render("Crear  usuario",False,(5, 150, 131))
regresar_text=Font_Daydream_20.render("Regresar",False,(5, 150, 131))
creacionUsuario_button=pygame.Rect(770,700,295,40)
regresar_button=pygame.Rect(50,686,195,40)
crearUsuario_real=pygame.Rect(360,450,275,40)
wrongPw_text=Font_Daydream_20.render("Contrasena incorrecta!",False,("red"))
errorUsuario=Font_Daydream_20.render("Ingrese un usuario!",False,("red"))
errorPassword=Font_Daydream_20.render("Ingrese una contrasena!",False,("red"))
UsuarioRegistrado=Font_Daydream_20.render("Usuario registrado!",False,(10,255,10))

colour3=pygame.Color(5, 150, 131)
cuatroCaracteres1=Font_Daydream_20.render("*el usuario y la",False,colour3)
cuatroCaracteres2=Font_Daydream_20.render("contrasena deben tener",False,colour3)
cuatroCaracteres3=Font_Daydream_20.render("al menos 4 caracteres",False,colour3)
cuatroCaracteres1_red=Font_Daydream_20.render("*el usuario y la",False,"red")
cuatroCaracteres2_red=Font_Daydream_20.render("contrasena deben tener",False,"red")
cuatroCaracteres3_red=Font_Daydream_20.render("al menos 4 caracteres",False,"red")
        


USUARIOS={
    "user":"user",
    "admin":"admin",
    "lun":"lun",
    "javier":"javier",
    "josue":'josue',
    "steven":"steven"
}

#si USER es "START", se muestra la pantalla de inicio de sesion
#si es "admin" se abre la configuracion
#si es "CrearUsuario" se abre el menu para crear usuarios
#si es "user" se inicia el juego
USER="user"

# Admin
Nivel_text = Font_Daydream_30.render("Nivel:",False,(5, 150, 131))
Nivel_text_shadow = Font_Daydream_30.render("Nivel:",False,(2, 77, 67))
CantLogos_text = Font_Daydream_30.render("Logos:",False,(5, 150, 131))
CantLogos_text_shadow = Font_Daydream_30.render("Logos:",False,(2, 77, 67))
tiempo_text = Font_Daydream_30.render("Tiempo:",False,(5, 150, 131))
tiempo_text_shadow = Font_Daydream_30.render("Tiempo:",False,(2, 77, 67))
Config_text = Font_Daydream_30.render("CONFIGURACION",False,(5, 150, 131))
Config_text_shadow = Font_Daydream_30.render("CONFIGURACION",False,(2, 77, 67))
tiempo_button=pygame.Rect(225,250,150,40)
CantLogos_button=pygame.Rect(660,250,150,40)

logos_int=10

flecha_size=(45,45)
arriba_flecha= pygame.image.load("Media/flecha_up.png").convert_alpha()
arriba_flecha=pygame.transform.scale(arriba_flecha,flecha_size)
abajo_flecha= pygame.image.load("Media/flecha_down.png").convert_alpha()
abajo_flecha=pygame.transform.scale(abajo_flecha,flecha_size)

tiempo_flecha_arriba=pygame.Rect(230,300,40,40)
tiempo_flecha_abajo=pygame.Rect(315,300,40,40)
logo_flecha_arriba=pygame.Rect(665,300,40,40)
logo_flecha_abajo=pygame.Rect(750,300,40,40)

Perdiste_txt = Font_Daydream_100.render("Perdiste",False,(179, 30, 30))
Perdiste_txt_shadow = Font_Daydream_100.render("Perdiste",False,(97, 10, 10))
# --------------------------------[Game]--------------------------------#

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if guess1_button.collidepoint(event.pos):
                exitosas = exitosas + tr1 # -1 es igual a + (-1)
                lugar,lugar2,lugar3 = randomizer(exitosas)
            elif guess2_button.collidepoint(event.pos):
                exitosas = exitosas + tr2 # -1 es igual a + (-1)
                lugar,lugar2,lugar3 = randomizer(exitosas)
            elif guess3_button.collidepoint(event.pos):
                exitosas = exitosas + tr3 # -1 es igual a + (-1)
                lugar,lugar2,lugar3 = randomizer(exitosas)

        if event.type==pygame.KEYDOWN:
            if active_user:
                if event.key == pygame.K_BACKSPACE:
                    usuario_input=usuario_input[:-1]
                else:
                    usuario_input+=event.unicode  
            elif active_pw:
                if event.key == pygame.K_BACKSPACE:
                    password_input=password_input[:-1]
                else:
                    password_input+=event.unicode              

    if USER=="START":
        screen.blit(Fondo,(0,0))
        if active_user==True:
            colour1=pygame.Color(0,42,210)
        else:
            colour1=pygame.Color(20,30,70,255)
        if active_pw==True:
            colour2=pygame.Color(0,42,210)
        else:
            colour2=pygame.Color(20,30,70,255)
        pygame.draw.rect(screen,colour1,textbox_usuario,0)
        pygame.draw.rect(screen,colour2,textbox_password,0)
        surface1=Font_Daydream_30.render(usuario_input,True,"white")
        surface2=Font_Daydream_30.render(password_input,True,"white")
        screen.blit(ingreso_text,(80,85))
        screen.blit(usuario_text,(textbox_usuario.x,textbox_usuario.y-51))
        screen.blit(surface1,(textbox_usuario.x+5,textbox_usuario.y+5))
        screen.blit(password_text,(textbox_password.x,textbox_password.y-51))
        screen.blit(surface2,(textbox_password.x+5,textbox_password.y+5))
        screen.blit(ingresar_text,(ingresar_button.x+1,ingresar_button.y+1))
        screen.blit(crearUsuario_text,(creacionUsuario_button.x,creacionUsuario_button.y))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ingresar_button.collidepoint(event.pos):
                if usuario_input in USUARIOS:
                    if usuario_input=="admin" and password_input=="admin":
                        USER=usuario_input
                    elif password_input==USUARIOS[usuario_input]:
                        USER="user"
                    elif password_input!=USUARIOS[usuario_input]:
                        screen.blit(wrongPw_text,(ingresar_button.x-120,ingresar_button.y+45))
                elif usuario_input not in USUARIOS:
                    screen.blit(noEncontrado_text,(ingresar_button.x-120,ingresar_button.y+45))
            if creacionUsuario_button.collidepoint(event.pos):
                USER="CrearUsuario"
                    
            elif textbox_usuario.collidepoint(event.pos) or textbox_password.collidepoint(event.pos):
                if textbox_usuario.collidepoint(event.pos):
                    active_user=True
                    active_pw=False
                else:
                    active_pw=True
                    active_user=False
            else:
                active_user=False
                active_pw=False
                
    elif USER=="CrearUsuario":
        screen.blit(Fondo,(0,0))
        screen.blit(crear_text,(180,85))
        screen.blit(regresar_text,(regresar_button.x,regresar_button.y+10))
        pygame.draw.rect(screen,colour1,textbox_usuario,0)
        pygame.draw.rect(screen,colour2,textbox_password,0)
        surface1=Font_Daydream_30.render(usuario_input,True,"white")
        surface2=Font_Daydream_30.render(password_input,True,"white")
        screen.blit(usuario_text,(textbox_usuario.x,textbox_usuario.y-51))
        screen.blit(surface1,(textbox_usuario.x+5,textbox_usuario.y+5))
        screen.blit(password_text,(textbox_password.x,textbox_password.y-51))
        screen.blit(surface2,(textbox_password.x+5,textbox_password.y+5))
        screen.blit(crearUsuario_text,(ingresar_button.x-40,ingresar_button.y+1))
        
        screen.blit(cuatroCaracteres1,(1060,200))
        screen.blit(cuatroCaracteres2,(1060,240))
        screen.blit(cuatroCaracteres3,(1060,280))
        
        if active_user:
            colour1=pygame.Color(0,42,210)
        else:
            colour1=pygame.Color(20,30,70,255)
        if active_pw:
            colour2=pygame.Color(0,42,210)
        else:
            colour2=pygame.Color(20,30,70,255)
               
        if event.type == pygame.MOUSEBUTTONDOWN:
            if regresar_button.collidepoint(event.pos):
                USER="START"
            elif crearUsuario_real.collidepoint(event.pos):
                if usuario_input in USUARIOS:
                    screen.blit(UsuarioRegistrado,(ingresar_button.x-20,ingresar_button.y+55))
                else:
                    if usuario_input!="" and password_input!="":
                        if len(usuario_input)>=4 and len(password_input)>=4:
                            USUARIOS[usuario_input]=password_input
                            screen.blit(UsuarioRegistrado,(ingresar_button.x-20,ingresar_button.y+55))
                        else:
                            screen.blit(cuatroCaracteres1_red,(1060,200))
                            screen.blit(cuatroCaracteres2_red,(1060,240))
                            screen.blit(cuatroCaracteres3_red,(1060,280))
                    else:
                        if usuario_input!="" and password_input=="":
                            screen.blit(errorUsuario,(ingresar_button.x-20,ingresar_button.y+55))
                        elif usuario_input=="" and password_input!="":
                            screen.blit(errorPassword,(ingresar_button.x-20,ingresar_button.y+55))
                
            elif textbox_usuario.collidepoint(event.pos) or textbox_password.collidepoint(event.pos):
                if textbox_usuario.collidepoint(event.pos):
                    active_user=True
                    active_pw=False
                else:
                    active_pw=True
                    active_user=False
            else:
                active_user=False
                active_pw=False

    elif USER=="admin":
        screen.blit(Fondo,(0,0))
        screen.blit(regresar_text,(regresar_button.x,regresar_button.y+10))
        screen.blit(Config_text_shadow, (300,105))
        screen.blit(Config_text, (300,100))
        screen.blit(tiempo_text_shadow,(200,205))
        screen.blit(tiempo_text,(200,200))
        screen.blit(CantLogos_text_shadow, (650,205))
        screen.blit(CantLogos_text, (650,200))
        pygame.draw.rect(screen,(80,104,242),tiempo_button, 3)
        pygame.draw.rect(screen,(80,104,242),CantLogos_button, 3)
        screen.blit(arriba_flecha,(230,300))
        screen.blit(abajo_flecha,(315,300))
        screen.blit(arriba_flecha,(665,300))
        screen.blit(abajo_flecha,(750,300))
        
        time_changingtext=Font_Daydream_30.render(str(tiempo),False,"black")
        logos_changingtext=Font_Daydream_30.render(str(logos_int),False,"black")
        
        screen.blit(time_changingtext,(tiempo_button.x,tiempo_button.y))
        screen.blit(logos_changingtext,(CantLogos_button.x,CantLogos_button.y))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if regresar_button.collidepoint(event.pos):
                USER="START"
            elif tiempo_flecha_arriba.collidepoint(event.pos):
                tiempo=tiempo+1
            elif tiempo_flecha_abajo.collidepoint(event.pos):
                tiempo=tiempo-1
            elif logo_flecha_arriba.collidepoint(event.pos):
                logos_int=logos_int+1
            elif logo_flecha_abajo.collidepoint(event.pos):
                logos_int=logos_int-1
   
    else:
        if level == 1:
            if exitosas < Cantidad_Logos_Admin*1:
                imagen,opcion = imageChoice(ListaNivel1, exitosas)
                guess1,guess2,guess3,tr1,tr2,tr3 = textoRandomizador(opcion,ListaNivel1,lugar,lugar2,lugar3)
                guess1 = Font_Minecraft.render(f"{guess1}",(80, 104, 242),"White")
                guess2 = Font_Minecraft.render(f"{guess2}",(80, 104, 242),"White")
                guess3 = Font_Minecraft.render(f"{guess3}",(80, 104, 242),"White")
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
                tiempo_txt = Font_Minecraft.render(f"Tiempo restante: {tiempo}",False,"White")
                screen.blit(tiempo_txt, (1100,850))
                timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)
                tempo -= 1
                if tempo <= 0:
                    tempo = 60
                    tiempo -=1
                if tiempo < 0:
                    screen.blit(FondoNegro, (0,0))
                    screen.blit(Perdiste_txt,(425,195))
                    screen.blit(Perdiste_txt_shadow,(425,200))
            else:
                exitosas = 0
                level += 1

        elif level == 2:
            if exitosas < Cantidad_Logos_Admin*2:
                imagen,opcion = imageChoice(ListaNivel2, exitosas)
                guess1,guess2,guess3,tr1,tr2,tr3 = textoRandomizador(opcion,ListaNivel1,lugar,lugar2,lugar3)
                guess1 = Font_Minecraft.render(f"{guess1}",(80, 104, 242),"White")
                guess2 = Font_Minecraft.render(f"{guess2}",(80, 104, 242),"White")
                guess3 = Font_Minecraft.render(f"{guess3}",(80, 104, 242),"White")
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
                tiempo_txt = Font_Minecraft.render(f"Tiempo restante: {tiempo}",False,"White")
                screen.blit(tiempo_txt, (1100,850))
                timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)
                tempo -= 1
                if tempo <= 0:
                    tempo = 60
                    tiempo -=1
                if tiempo < 0:
                    screen.blit(FondoNegro, (0,0))
                    screen.blit(Perdiste_txt,(425,195))
                    screen.blit(Perdiste_txt_shadow,(425,200))
            else:
                exitosas = 0
                level += 1
        elif level == 3:
            if exitosas < Cantidad_Logos_Admin*3:
                imagen,opcion = imageChoice(ListaNivel3, exitosas)
                guess1,guess2,guess3,tr1,tr2,tr3 = textoRandomizador(opcion,ListaNivel3,lugar,lugar2,lugar3)
                guess1 = Font_Minecraft.render(f"{guess1}",(80, 104, 242),"White")
                guess2 = Font_Minecraft.render(f"{guess2}",(80, 104, 242),"White")
                guess3 = Font_Minecraft.render(f"{guess3}",(80, 104, 242),"White")
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
                tiempo_txt = Font_Minecraft.render(f"Tiempo restante: {tiempo}",False,"White")
                screen.blit(tiempo_txt, (1100,850))
                timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)
                tempo -= 1
                if tempo <= 0:
                    tempo = 60
                    tiempo -=1
                if tiempo < 0:
                    screen.blit(FondoNegro, (0,0))
                    screen.blit(Perdiste_txt,(425,195))
                    screen.blit(Perdiste_txt_shadow,(425,200))
            else:
                exitosas = 0
                level += 1
        
        elif level == 4:
            if exitosas < Cantidad_Logos_Admin*4:
                imagen,opcion = imageChoice(ListaNivel4, exitosas)
                guess1,guess2,guess3,tr1,tr2,tr3 = textoRandomizador(opcion,ListaNivel4,lugar,lugar2,lugar3)
                guess1 = Font_Minecraft.render(f"{guess1}",(80, 104, 242),"White")
                guess2 = Font_Minecraft.render(f"{guess2}",(80, 104, 242),"White")
                guess3 = Font_Minecraft.render(f"{guess3}",(80, 104, 242),"White")
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
                tiempo_txt = Font_Minecraft.render(f"Tiempo restante: {tiempo}",False,"White")
                screen.blit(tiempo_txt, (1100,850))
                timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)
                tempo -= 1
                if tempo <= 0:
                    tempo = 60
                    tiempo -=1
                if tiempo < 0:
                    screen.blit(FondoNegro, (0,0))
                    screen.blit(Perdiste_txt,(425,195))
                    screen.blit(Perdiste_txt_shadow,(425,200))
            else:
                exitosas = 0
                level += 1
        
        elif level == 5:
            if exitosas < Cantidad_Logos_Admin*5:
                imagen,opcion = imageChoice(ListaNivel5, exitosas)
                guess1,guess2,guess3,tr1,tr2,tr3 = textoRandomizador(opcion,ListaNivel5,lugar,lugar2,lugar3)
                guess1 = Font_Minecraft.render(f"{guess1}",(80, 104, 242),"White")
                guess2 = Font_Minecraft.render(f"{guess2}",(80, 104, 242),"White")
                guess3 = Font_Minecraft.render(f"{guess3}",(80, 104, 242),"White")
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
                tiempo_txt = Font_Minecraft.render(f"Tiempo restante: {tiempo}",False,"White")
                screen.blit(tiempo_txt, (1100,850))
                timer_animation, text_y_pos = animacionLogo(timer_animation, text_y_pos)
                tempo -= 1
                if tempo <= 0:
                    tempo = 60
                    tiempo -=1
                if tiempo < 0:
                    screen.blit(FondoNegro, (0,0))
                    screen.blit(Perdiste_txt,(425,195))
                    screen.blit(Perdiste_txt_shadow,(425,200))
            else:
                exitosas = 0
                level += 1

    pygame.display.update()
    clock.tick(60)