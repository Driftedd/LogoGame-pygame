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

def animaciones(timer_animation,text_y_pos,posorigin):
    timer_animation += 1
    if text_y_pos == posorigin and timer_animation < 15:
        text_y_pos = text_y_pos-5
    elif text_y_pos == posorigin-10 and timer_animation > 15 and timer_animation < 30:
        text_y_pos = text_y_pos-5
    elif text_y_pos == posorigin-10 and timer_animation > 30 and timer_animation < 45:
        text_y_pos = text_y_pos+5
    elif text_y_pos == posorigin-5 and timer_animation > 45:
        text_y_pos = text_y_pos+5
    elif timer_animation > 60:
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

def GuardarTiempos(tiempoanterior,tiempo):
    tiempo_admin
    if tiempoanterior==0:
        return tiempo_admin-tiempo
    elif tiempoanterior != 0:
        return tiempoanterior + (tiempo_admin-tiempo)
    
def cargarusuarios(USUARIOS):
    with open("archivos/allusers","r") as allusers:
        usersList=allusers.read().split("\n")
    for i in range(0,len(usersList),2):
        USUARIOS[usersList[i]]=usersList[i+1]
    return USUARIOS


def agregarNuevoUsuario(usuario_input, password_input, USUARIOS):
    print("llamando agregarNuevoUsuario")
    print(USUARIOS)
    if usuario_input.lower() not in USUARIOS:
        with open("archivos/allusers","a+") as allusers:
                allusers.write("\n"+usuario_input)
                allusers.write("\n"+password_input)
        USUARIOS=cargarusuarios(USUARIOS)
        print(USUARIOS)
        tiempototal=0
        promedio=0
        with open("archivos/all_users/"+str(usuario_input),'w+') as user_info:
                user_info.write(usuario_input)
                user_info.write("\n")
                user_info.write(password_input)
                user_info.write("\n")
                user_info.write(str(exitosas))
                user_info.write("\n")
                user_info.write(str(tiempototal))
                user_info.write("\n")
                user_info.write(str(promedio))
                user_info.write("\n0"*150)
        print("usuario agregado")
        return USUARIOS
    else:
        print("usuario ya registrado")

            
def guardarInfoUsuario(usuario_input,password_input,exitosas,tiempototal,promedio,tiemposLogos):
    print("llamando guardarInfoUsuario")
    with open("archivos/all_users/"+str(usuario_input.lower()),'w+') as user_info:
        user_info.write(usuario_input.lower()+"\n")
        user_info.write(password_input.lower()+"\n")
        user_info.write(str(exitosas)+"\n")
        user_info.write(str(tiempototal)+"\n")
        user_info.write((str(promedio)))
        for i in range(len(tiemposLogos)):
            user_info.write("\n"+str(tiemposLogos[i]))
        
def cargarInfoUsuario(exitosas,tiempototal,promedio,Lista_Niveles):
    print("llamando cargarInfoUsuario")
    with open("archivos/all_users/"+str(usuario_input.lower()),'r+') as user_info:
        user_info_list=user_info.read().split("\n")
    print(user_info_list)
    
    exitosas=int(user_info_list[2])
    tiempototal=0
    promedio=0
    
    infoUsuario=[exitosas,tiempototal,promedio]
    tiempoPorLogoFalse=user_info_list[5:]
    

    infoUsuarioList=[infoUsuario,tiempoPorLogoFalse]
    return infoUsuarioList
        
        

def mostrarInfoUsuario():
    print("llamando mostrarInfoUsuario")
    print("usuario:  ", usuario_input.lower())
    print("password:  ", password_input.lower())
    print("logos acertados:  ",exitosas)
    print("Tiempo acumulado:  ")
    print("Tiempo promedio:  ")
    print("tiempo admin:  ", tiempo_admin)
    print("cantidad de logos admin:  ", Cantidad_Logos_Admin)
    print("\n\n")
mostrar=True   

usuarioAgregado=False
 
#--------------------------------[Pre-Game]--------------------------------#
pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Quiz Logo")
clock = pygame.time.Clock()
Font_Daydream_20 = pygame.font.Font("Media/Font_Daydream.ttf", 20)
Font_Daydream_30 = pygame.font.Font("Media/Font_Daydream.ttf", 30)
Font_Daydream_50 = pygame.font.Font("Media/Font_Daydream.ttf", 50)
Font_Daydream_100 = pygame.font.Font("Media/Font_Daydream.ttf", 100)
Font_Empire_80 = pygame.font.Font("Media/Font_Empire.ttf", 80)
Font_Empire_40 = pygame.font.Font("Media/Font_Empire.ttf", 40)
Font_Minecraft = pygame.font.Font("Media/Font_Minecraft.ttf",50)
text_x_pos = 230
text_y_pos = 70

# Logos completos:
# 1
Pepsi = pygame.image.load("Media/Marcas/Nivel1/pepsi.png").convert_alpha()
McDonalds = pygame.image.load("Media/Marcas/Nivel1/mcdonalds.png").convert_alpha()
BurgerKing = pygame.image.load("Media/Marcas/Nivel1/burger-king.png").convert_alpha()
logitech = pygame.image.load("Media/Marcas/Nivel1/logitech.png").convert_alpha()
spotify = pygame.image.load("Media/Marcas/Nivel1/spotify.png").convert_alpha()
starbucks = pygame.image.load("Media/Marcas/Nivel1/starbucks.png").convert_alpha()
youtube = pygame.image.load("Media/Marcas/Nivel1/youtube.png").convert_alpha()
python = pygame.image.load("Media/Marcas/Nivel1/python.png").convert_alpha()
apple = pygame.image.load("Media/Marcas/Nivel1/apple.png").convert_alpha()
_3m = pygame.image.load("Media/Marcas/Nivel1/3m.png").convert_alpha()
# 2
_7up = pygame.image.load("Media/Marcas/Nivel2/7up.png").convert_alpha()
adidas = pygame.image.load("Media/Marcas/Nivel2/adidas.png").convert_alpha()
amazon = pygame.image.load("Media/Marcas/Nivel2/amazon.png").convert_alpha()
bmw = pygame.image.load("Media/Marcas/Nivel2/bmw.png").convert_alpha()
duckduckgo = pygame.image.load("Media/Marcas/Nivel2/duckduckgo.png").convert_alpha()
ea = pygame.image.load("Media/Marcas/Nivel2/ea.png").convert_alpha()
fanta = pygame.image.load("Media/Marcas/Nivel2/fanta.png").convert_alpha()
hasbro = pygame.image.load("Media/Marcas/Nivel2/hasbro.png").convert_alpha()
jacks = pygame.image.load("Media/Marcas/Nivel2/jacks.png").convert_alpha()
kfc = pygame.image.load("Media/Marcas/Nivel2/kfc.png").convert_alpha()
lego = pygame.image.load("Media/Marcas/Nivel2/lego.png").convert_alpha()
monster = pygame.image.load("Media/Marcas/Nivel2/monster.png").convert_alpha()
netflix = pygame.image.load("Media/Marcas/Nivel2/netflix.png").convert_alpha()
nfl = pygame.image.load("Media/Marcas/Nivel2/nfl.png").convert_alpha()
jrockets = pygame.image.load("Media/Marcas/Nivel2/rockets.png").convert_alpha()
sega = pygame.image.load("Media/Marcas/Nivel2/sega.png").convert_alpha()
spacex = pygame.image.load("Media/Marcas/Nivel2/space.png").convert_alpha()
utorrent = pygame.image.load("Media/Marcas/Nivel2/torrent.png").convert_alpha()
tosty = pygame.image.load("Media/Marcas/Nivel2/tosty.png").convert_alpha()
vscode = pygame.image.load("Media/Marcas/Nivel2/vscode.png").convert_alpha()

# 3
adobe = pygame.image.load("Media/Marcas/Nivel3/adobe.png").convert_alpha()
autodesk = pygame.image.load("Media/Marcas/Nivel3/autodesk.png").convert_alpha()
balance = pygame.image.load("Media/Marcas/Nivel3/balance.png").convert_alpha()
blackberry = pygame.image.load("Media/Marcas/Nivel3/blackberry.png").convert_alpha()
chevro = pygame.image.load("Media/Marcas/Nivel3/chevro.png").convert_alpha()
coke = pygame.image.load("Media/Marcas/Nivel3/coke.png").convert_alpha()
delMonte = pygame.image.load("Media/Marcas/Nivel3/delMonte.png").convert_alpha()
discord = pygame.image.load("Media/Marcas/Nivel3/discord.png").convert_alpha()
dreamworks = pygame.image.load("Media/Marcas/Nivel3/dreamworks.png").convert_alpha()
facebook = pygame.image.load("Media/Marcas/Nivel3/facebook.png").convert_alpha()
hulu = pygame.image.load("Media/Marcas/Nivel3/hulu.png").convert_alpha()
microsoft = pygame.image.load("Media/Marcas/Nivel3/microsoft.png").convert_alpha()
motorola = pygame.image.load("Media/Marcas/Nivel3/motorola.png").convert_alpha()
moyo = pygame.image.load("Media/Marcas/Nivel3/moyo.png").convert_alpha()
nascar = pygame.image.load("Media/Marcas/Nivel3/nascar.png").convert_alpha()
nike = pygame.image.load("Media/Marcas/Nivel3/nike.png").convert_alpha()
nintendo = pygame.image.load("Media/Marcas/Nivel3/nintendo.png").convert_alpha()
nissan = pygame.image.load("Media/Marcas/Nivel3/nissan.png").convert_alpha()
office = pygame.image.load("Media/Marcas/Nivel3/office.png").convert_alpha()
pyg = pygame.image.load("Media/Marcas/Nivel3/p&g.png").convert_alpha()
pizzahut = pygame.image.load("Media/Marcas/Nivel3/pizzahut.png").convert_alpha()
purina = pygame.image.load("Media/Marcas/Nivel3/purina.png").convert_alpha()
rayovac = pygame.image.load("Media/Marcas/Nivel3/rayovac.png").convert_alpha()
razer = pygame.image.load("Media/Marcas/Nivel3/razer.png").convert_alpha()
safari = pygame.image.load("Media/Marcas/Nivel3/safari.png").convert_alpha()
siman = pygame.image.load("Media/Marcas/Nivel3/siman.png").convert_alpha()
sprite = pygame.image.load("Media/Marcas/Nivel3/sprite.png").convert_alpha()
tacobell = pygame.image.load("Media/Marcas/Nivel3/tacobell.png").convert_alpha()
toyota = pygame.image.load("Media/Marcas/Nivel3/toyota.png").convert_alpha()
vlc = pygame.image.load("Media/Marcas/Nivel3/vlc.png").convert_alpha()
#4
bimbo = pygame.image.load("Media/Marcas/Nivel4/bimbo.png").convert_alpha()
colgate = pygame.image.load("Media/Marcas/Nivel4/colgate.png").convert_alpha()
dell = pygame.image.load("Media/Marcas/Nivel4/dell.png").convert_alpha()
dhl = pygame.image.load("Media/Marcas/Nivel4/dhl.png").convert_alpha()
didi = pygame.image.load("Media/Marcas/Nivel4/didi.png").convert_alpha()
disney = pygame.image.load("Media/Marcas/Nivel4/disney.png").convert_alpha()
dominos = pygame.image.load("Media/Marcas/Nivel4/dominos.png").convert_alpha()
doritos = pygame.image.load("Media/Marcas/Nivel4/doritos.png").convert_alpha()
dospinos = pygame.image.load("Media/Marcas/Nivel4/dospinos.png").convert_alpha()
gatorade = pygame.image.load("Media/Marcas/Nivel4/gatorade.png").convert_alpha()
gog = pygame.image.load("Media/Marcas/Nivel4/gog.png").convert_alpha()
google = pygame.image.load("Media/Marcas/Nivel4/google.png").convert_alpha()
gucci = pygame.image.load("Media/Marcas/Nivel4/gucci.png").convert_alpha()
gillette = pygame.image.load("Media/Marcas/Nivel4/gillette.png").convert_alpha()
heineken = pygame.image.load("Media/Marcas/Nivel4/heineken.png").convert_alpha()
imperial = pygame.image.load("Media/Marcas/Nivel4/imperial.png").convert_alpha()
kellogs = pygame.image.load("Media/Marcas/Nivel4/kellogs.png").convert_alpha()
kolbi = pygame.image.load("Media/Marcas/Nivel4/kolbi.png").convert_alpha()
maggi = pygame.image.load("Media/Marcas/Nivel4/maggi.png").convert_alpha()
mastercard = pygame.image.load("Media/Marcas/Nivel4/mastercard.png").convert_alpha()
mattel = pygame.image.load("Media/Marcas/Nivel4/mattel.png").convert_alpha()
maxi = pygame.image.load("Media/Marcas/Nivel4/maxi.png").convert_alpha()
monopoly = pygame.image.load("Media/Marcas/Nivel4/monopoly.png").convert_alpha()
motorola = pygame.image.load("Media/Marcas/Nivel4/motorola.png").convert_alpha()
movistar = pygame.image.load("Media/Marcas/Nivel4/movistar.png").convert_alpha()
nestle = pygame.image.load("Media/Marcas/Nivel4/nestle.png").convert_alpha()
pali = pygame.image.load("Media/Marcas/Nivel4/pali.png").convert_alpha()
pixar = pygame.image.load("Media/Marcas/Nivel4/pixar.png").convert_alpha()
powerade = pygame.image.load("Media/Marcas/Nivel4/powerade.png").convert_alpha()
pozuelo = pygame.image.load("Media/Marcas/Nivel4/pozuelo.png").convert_alpha()
pringles = pygame.image.load("Media/Marcas/Nivel4/pringles.png").convert_alpha()
rareware = pygame.image.load("Media/Marcas/Nivel4/rareware.png").convert_alpha()
rexona = pygame.image.load("Media/Marcas/Nivel4/rexona.png").convert_alpha()
riot = pygame.image.load("Media/Marcas/Nivel4/riot.png").convert_alpha()
samsung = pygame.image.load("Media/Marcas/Nivel4/samsung.png").convert_alpha()
scott = pygame.image.load("Media/Marcas/Nivel4/scott.png").convert_alpha()
sony = pygame.image.load("Media/Marcas/Nivel4/sony.png").convert_alpha()
tesla = pygame.image.load("Media/Marcas/Nivel4/tesla.png").convert_alpha()
tigo = pygame.image.load("Media/Marcas/Nivel4/tigo.png").convert_alpha()
uber = pygame.image.load("Media/Marcas/Nivel4/uber.png").convert_alpha()
#5
alka = pygame.image.load("Media/Marcas/Nivel5/alka.png").convert_alpha()
amd = pygame.image.load("Media/Marcas/Nivel5/amd.png").convert_alpha()
atyt = pygame.image.load("Media/Marcas/Nivel5/at&t.png").convert_alpha()
bacardi = pygame.image.load("Media/Marcas/Nivel5/bacardi.png").convert_alpha()
bandai = pygame.image.load("Media/Marcas/Nivel5/bandai.png").convert_alpha()
bayer = pygame.image.load("Media/Marcas/Nivel5/bayer.png").convert_alpha()
cacique = pygame.image.load("Media/Marcas/Nivel5/cacique.png").convert_alpha()
carlsjr = pygame.image.load("Media/Marcas/Nivel5/carlsjr.png").convert_alpha()
cdprojekt = pygame.image.load("Media/Marcas/Nivel5/cdprojekt.png").convert_alpha()
chanel = pygame.image.load("Media/Marcas/Nivel5/chanel.png").convert_alpha()
cisco = pygame.image.load("Media/Marcas/Nivel5/cisco.png").convert_alpha()
claro = pygame.image.load("Media/Marcas/Nivel5/claro.png").convert_alpha()
corvette = pygame.image.load("Media/Marcas/Nivel5/corvette.png").convert_alpha()
daniels = pygame.image.load("Media/Marcas/Nivel5/daniels.png").convert_alpha()
dos = pygame.image.load("Media/Marcas/Nivel5/dos.png").convert_alpha()
ebay = pygame.image.load("Media/Marcas/Nivel5/ebay.png").convert_alpha()
edge = pygame.image.load("Media/Marcas/Nivel5/edge.png").convert_alpha()
fedex = pygame.image.load("Media/Marcas/Nivel5/fedex.png").convert_alpha()
ferrari = pygame.image.load("Media/Marcas/Nivel5/ferrari.png").convert_alpha()
ford = pygame.image.load("Media/Marcas/Nivel5/ford.png").convert_alpha()
gmail = pygame.image.load("Media/Marcas/Nivel5/gmail.png").convert_alpha()
huawei = pygame.image.load("Media/Marcas/Nivel5/huawei.png").convert_alpha()
hyundai = pygame.image.load("Media/Marcas/Nivel5/hyundai.png").convert_alpha()
intel = pygame.image.load("Media/Marcas/Nivel5/intel.png").convert_alpha()
java = pygame.image.load("Media/Marcas/Nivel5/java.png").convert_alpha()
_max = pygame.image.load("Media/Marcas/Nivel5/max.png").convert_alpha()
mcdonalds_1953 = pygame.image.load("Media/Marcas/Nivel5/mcdonalds_1953.png").convert_alpha()
mercedes = pygame.image.load("Media/Marcas/Nivel5/mercedes.png").convert_alpha()
michelin = pygame.image.load("Media/Marcas/Nivel5/michelin.png").convert_alpha()
numar = pygame.image.load("Media/Marcas/Nivel5/numar.png").convert_alpha()
oralB = pygame.image.load("Media/Marcas/Nivel5/oralB.png").convert_alpha()
oreo = pygame.image.load("Media/Marcas/Nivel5/oreo.png").convert_alpha()
palmolive = pygame.image.load("Media/Marcas/Nivel5/palmolive.png").convert_alpha()
pampers = pygame.image.load("Media/Marcas/Nivel5/pampers.png").convert_alpha()
panasonic = pygame.image.load("Media/Marcas/Nivel5/panasonic.png").convert_alpha()
papajohns = pygame.image.load("Media/Marcas/Nivel5/papajohns.png").convert_alpha()
paypal = pygame.image.load("Media/Marcas/Nivel5/paypal.png").convert_alpha()
pepto = pygame.image.load("Media/Marcas/Nivel5/pepto.png").convert_alpha()
pinterest = pygame.image.load("Media/Marcas/Nivel5/pinterest.png").convert_alpha()
redbull = pygame.image.load("Media/Marcas/Nivel5/redbull.png").convert_alpha()
salsol = pygame.image.load("Media/Marcas/Nivel5/salsol.png").convert_alpha()
steam = pygame.image.load("Media/Marcas/Nivel5/steam.png").convert_alpha()
subway = pygame.image.load("Media/Marcas/Nivel5/subway.png").convert_alpha()
swim = pygame.image.load("Media/Marcas/Nivel5/swim.png").convert_alpha()
ups = pygame.image.load("Media/Marcas/Nivel5/ups.png").convert_alpha()
valve = pygame.image.load("Media/Marcas/Nivel5/valve.png").convert_alpha()
visa = pygame.image.load("Media/Marcas/Nivel5/visa.png").convert_alpha()
walmart = pygame.image.load("Media/Marcas/Nivel5/walmart.png").convert_alpha()
whatsapp = pygame.image.load("Media/Marcas/Nivel5/whatsapp.png").convert_alpha()
yamaha = pygame.image.load("Media/Marcas/Nivel5/yamaha.png").convert_alpha()

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
#4
bimbo_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/bimbo.png").convert_alpha()
colgate_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/colgate.png").convert_alpha()
dell_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/dell.png").convert_alpha()
dhl_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/dhl.png").convert_alpha()
didi_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/didi.png").convert_alpha()
disney_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/disney.png").convert_alpha()
dominos_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/dominos.png").convert_alpha()
doritos_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/doritos.png").convert_alpha()
dospinos_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/dospinos.png").convert_alpha()
gatorade_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/gatorade.png").convert_alpha()
gog_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/gog.png").convert_alpha()
google_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/google.png").convert_alpha()
gucci_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/gucci.png").convert_alpha()
gillette_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/gillette.png").convert_alpha()
heineken_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/heineken.png").convert_alpha()
imperial_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/imperial.png").convert_alpha()
kellogs_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/kellogs.png").convert_alpha()
kolbi_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/kolbi.png").convert_alpha()
maggi_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/maggi.png").convert_alpha()
mastercard_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/mastercard.png").convert_alpha()
mattel_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/mattel.png").convert_alpha()
maxi_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/maxi.png").convert_alpha()
monopoly_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/monopoly.png").convert_alpha()
motorola_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/motorola.png").convert_alpha()
movistar_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/movistar.png").convert_alpha()
nestle_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/nestle.png").convert_alpha()
pali_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/pali.png").convert_alpha()
pixar_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/pixar.png").convert_alpha()
powerade_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/powerade.png").convert_alpha()
pozuelo_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/pozuelo.png").convert_alpha()
pringles_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/pringles.png").convert_alpha()
rareware_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/rareware.png").convert_alpha()
rexona_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/rexona.png").convert_alpha()
riot_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/riot.png").convert_alpha()
samsung_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/samsung.png").convert_alpha()
scott_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/scott.png").convert_alpha()
sony_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/sony.png").convert_alpha()
tesla_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/tesla.png").convert_alpha()
tigo_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/tigo.png").convert_alpha()
uber_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel4/uber.png").convert_alpha()
#5
alka_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/alka.png").convert_alpha()
amd_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/amd.png").convert_alpha()
atyt_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/at&t.png").convert_alpha()
bacardi_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/bacardi.png").convert_alpha()
bandai_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/bandai.png").convert_alpha()
bayer_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/bayer.png").convert_alpha()
cacique_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/cacique.png").convert_alpha()
carlsjr_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/carlsjr.png").convert_alpha()
cdprojekt_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/cdprojekt.png").convert_alpha()
chanel_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/chanel.png").convert_alpha()
cisco_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/cisco.png").convert_alpha()
claro_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/claro.png").convert_alpha()
corvette_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/corvette.png").convert_alpha()
daniels_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/daniels.png").convert_alpha()
dos_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/dos.png").convert_alpha()
ebay_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/ebay.png").convert_alpha()
edge_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/edge.png").convert_alpha()
fedex_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/fedex.png").convert_alpha()
ferrari_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/ferrari.png").convert_alpha()
ford_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/ford.png").convert_alpha()
gmail_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/gmail.png").convert_alpha()
huawei_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/huawei.png").convert_alpha()
hyundai_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/hyundai.png").convert_alpha()
intel_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/intel.png").convert_alpha()
java_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/java.png").convert_alpha()
_max_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/max.png").convert_alpha()
mcdonalds_1953_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/mcdonalds_1953.png").convert_alpha()
mercedes_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/mercedes.png").convert_alpha()
michelin_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/michelin.png").convert_alpha()
numar_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/numar.png").convert_alpha()
oralB_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/oralB.png").convert_alpha()
oreo_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/oreo.png").convert_alpha()
palmolive_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/palmolive.png").convert_alpha()
pampers_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/pampers.png").convert_alpha()
panasonic_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/panasonic.png").convert_alpha()
papajohns_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/papajohns.png").convert_alpha()
paypal_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/paypal.png").convert_alpha()
pepto_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/pepto.png").convert_alpha()
pinterest_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/pinterest.png").convert_alpha()
redbull_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/redbull.png").convert_alpha()
salsol_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/salsol.png").convert_alpha()
steam_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/steam.png").convert_alpha()
subway_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/subway.png").convert_alpha()
swim_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/swim.png").convert_alpha()
ups_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/ups.png").convert_alpha()
valve_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/valve.png").convert_alpha()
visa_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/visa.png").convert_alpha()
walmart_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/walmart.png").convert_alpha()
whatsapp_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/whatsapp.png").convert_alpha()
yamaha_incompleto = pygame.image.load("Media/Marcas_Incompletas/Nivel5/yamaha.png").convert_alpha()
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
balance_str="NewBalance"
blackberry_str="BlackBerry"
chevro_str="Chevrolet"
coke_str="CocaCola"
delMonte_str="delMonte"
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
#Strings Nivel 4
bimbo_str="Bimbo"
colgate_str="Colgate"
dell_str="Dell"
dhl_str="DHL"
didi_str="DiDi"
disney_str="Disney"
dominos_str="Dominos"
doritos_str="Doritos"
dospinos_str="Dos Pinos"
gatorade_str="Gatorade"
gog_str="GoG"
google_str="Google"
gucci_str="Gucci"
gillette_str="Gillette"
heineken_str="Heineken"
imperial_str="Imperial"
kellogs_str="Kellogs"
kolbi_str="Kolbi"
maggi_str="Maggi"
mastercard_str="MasterCard"
mattel_str="Mattel"
maxi_str="Maxi"
monopoly_str="Monopoly"
motorola_str="Motorola"
movistar_str="Movistar"
nestle_str="Nestle"
pali_str="Pali"
pixar_str="Pixar"
powerade_str="Powerade"
pozuelo_str="Pozuelo"
pringles_str="Pringles"
rareware_str="Rareware"
rexona_str="Rexona"
riot_str="Riot"
samsung_str="Samsung"
scott_str="Scott"
sony_str="Sony"
tesla_str="Tesla"
tigo_str="Tigo"
uber_str="Uber"
#Strings Nivel 5
alka_str="Alka-Seltzer"
amd_str="AMD"
atyt_str="AT&T"
bacardi_str="Bacardi"
bandai_str="Bandai"
bayer_str="Bayer"
cacique_str="Cacique"
carlsjr_str="Carl's Jr."
cdprojekt_str="CdProjekt"
chanel_str="Chanel"
cisco_str="Cisco"
claro_str="Claro"
corvette_str="Corvette"
daniels_str="Jack Daniels"
dos_str="Dos"
ebay_str="Ebay"
edge_str="Edge"
fedex_str="FedEx"
ferrari_str="Ferrari"
ford_str="Ford"
gmail_str="GMail"
huawei_str="Huawei"
hyundai_str="Hyundai"
intel_str="Intel"
java_str="Java"
_max_str="Max"
mcdonalds_1953_str="McDonald's Antiguo"
mercedes_str="Mercedes"
michelin_str="Michelin"
numar_str="Numar"
oralB_str="Oral B"
oreo_str="Oreo"
palmolive_str = "Palmolive"
pampers_str = "Pampers"
panasonic_str = "Panasonic"
papajohns_str = "Papa Johns"
paypal_str = "Paypal"
pepto_str = "PeptoBismol"
pinterest_str = "Pinterest"
redbull_str = "RedBull"
salsol_str = "SalSol"
steam_str = "Steam"
subway_str="Subway"
swim_str="Swim"
ups_str="Ups"
valve_str="Valve"
visa_str="Visa"
walmart_str="Walmart"
whatsapp_str="WhatsApp"
yamaha_str="Yamaha"
# Tiempos
#1
Pepsi_TiempoTardado = 0
Macdonalds_TiempoTardado = 0
BurgerKing_TiempoTardado = 0
Logitech_TiempoTardado = 0
Spotify_TiempoTardado = 0
StarBucks_TiempoTardado = 0
YouTube_TiempoTardado = 0
Python_TiempoTardado = 0
Apple_TiempoTardado = 0
M3_TiempoTardado = 0
#2
_7up_TiempoTardado = 0
adidas_TiempoTardado = 0
amazon_TiempoTardado = 0
bmw_TiempoTardado = 0
duckduckgo_TiempoTardado = 0
ea_TiempoTardado = 0
fanta_TiempoTardado = 0
hasbro_TiempoTardado = 0
jacks_TiempoTardado = 0
kfc_TiempoTardado = 0
lego_TiempoTardado = 0
monster_TiempoTardado = 0
netflix_TiempoTardado = 0
nfl_TiempoTardado = 0
jrockets_TiempoTardado = 0
sega_TiempoTardado = 0
spacex_TiempoTardado = 0
utorrent_TiempoTardado = 0
tosty_TiempoTardado = 0
vscode_TiempoTardado = 0
#3
adobe_TiempoTardado = 0
autodesk_TiempoTardado = 0
balance_TiempoTardado = 0
blackberry_TiempoTardado = 0
chevro_TiempoTardado = 0
coke_TiempoTardado = 0
delMonte_TiempoTardado = 0
discord_TiempoTardado = 0
dreamworks_TiempoTardado = 0
facebook_TiempoTardado = 0
hulu_TiempoTardado = 0
microsoft_TiempoTardado = 0
motorola_TiempoTardado = 0
moyo_TiempoTardado = 0
nascar_TiempoTardado = 0
nike_TiempoTardado = 0
nintendo_TiempoTardado = 0
nissan_TiempoTardado = 0
office_TiempoTardado = 0
pyg_TiempoTardado = 0
pizzahut_TiempoTardado = 0
purina_TiempoTardado = 0
rayovac_TiempoTardado = 0
razer_TiempoTardado = 0
safari_TiempoTardado = 0
siman_TiempoTardado = 0
sprite_TiempoTardado = 0
tacobell_TiempoTardado = 0
toyota_TiempoTardado = 0
vlc_TiempoTardado = 0
#4
bimbo_TiempoTardado = 0
colgate_TiempoTardado = 0
dell_TiempoTardado = 0
dhl_TiempoTardado = 0
didi_TiempoTardado = 0
disney_TiempoTardado = 0
dominos_TiempoTardado = 0
doritos_TiempoTardado = 0
dospinos_TiempoTardado = 0
gatorade_TiempoTardado = 0
gog_TiempoTardado = 0
google_TiempoTardado = 0
gucci_TiempoTardado = 0
gillette_TiempoTardado = 0
heineken_TiempoTardado = 0
imperial_TiempoTardado = 0
kellogs_TiempoTardado = 0
kolbi_TiempoTardado = 0
maggi_TiempoTardado = 0
mastercard_TiempoTardado = 0
mattel_TiempoTardado = 0
maxi_TiempoTardado = 0
monopoly_TiempoTardado = 0
motorola_TiempoTardado = 0
movistar_TiempoTardado = 0
nestle_TiempoTardado = 0
pali_TiempoTardado = 0
pixar_TiempoTardado = 0
powerade_TiempoTardado = 0
pozuelo_TiempoTardado = 0
pringles_TiempoTardado = 0
rareware_TiempoTardado = 0
rexona_TiempoTardado = 0
riot_TiempoTardado = 0
samsung_TiempoTardado = 0
scott_TiempoTardado = 0
sony_TiempoTardado = 0
tesla_TiempoTardado = 0
tigo_TiempoTardado = 0
uber_TiempoTardado = 0

#5
alka_TiempoTardado = 0
amd_TiempoTardado = 0
atyt_TiempoTardado = 0
bacardi_TiempoTardado = 0
bandai_TiempoTardado = 0
bayer_TiempoTardado = 0
cacique_TiempoTardado = 0
carlsjr_TiempoTardado = 0
cdprojekt_TiempoTardado = 0
chanel_TiempoTardado = 0
cisco_TiempoTardado = 0
claro_TiempoTardado = 0
corvette_TiempoTardado = 0
daniels_TiempoTardado = 0
dos_TiempoTardado = 0
ebay_TiempoTardado = 0
edge_TiempoTardado = 0
fedex_TiempoTardado = 0
ferrari_TiempoTardado = 0
ford_TiempoTardado = 0
gmail_TiempoTardado = 0
huawei_TiempoTardado = 0
hyundai_TiempoTardado = 0
intel_TiempoTardado = 0
java_TiempoTardado = 0
_max_TiempoTardado = 0
mcdonalds_1953_TiempoTardado = 0
mercedes_TiempoTardado = 0
michelin_TiempoTardado = 0
numar_TiempoTardado = 0
oralB_TiempoTardado = 0
oreo_TiempoTardado = 0
subway_TiempoTardado = 0
swim_TiempoTardado = 0
ups_TiempoTardado = 0
valve_TiempoTardado = 0
visa_TiempoTardado = 0
walmart_TiempoTardado = 0
whatsapp_TiempoTardado = 0
yamaha_TiempoTardado = 0
palmolive_TiempoTardado = 0
pampers_TiempoTardado = 0
panasonic_TiempoTardado = 0
papajohns_TiempoTardado = 0
paypal_TiempoTardado = 0
pepto_TiempoTardado = 0
pinterest_TiempoTardado = 0
redbull_TiempoTardado = 0
salsol_TiempoTardado = 0
steam_TiempoTardado = 0

# Setup
ListaNivel1=[
    [Pepsi,Pepsi_Incompleto,Pepsi_str,Pepsi_TiempoTardado],
    [McDonalds,McDonalds_Incompleto,McDonalds_str,Macdonalds_TiempoTardado],
    [BurgerKing,BurgerKing_Incompleto,BurgerKing_str,BurgerKing_TiempoTardado],
    [logitech,logitech_Incompleto,logitech_str,Logitech_TiempoTardado],
    [spotify,spotify_Incompleto,spotify_str,Spotify_TiempoTardado],
    [starbucks,starbucks_Incompleto,starbucks_str,StarBucks_TiempoTardado],
    [youtube,youtube_Incompleto,youtube_str,YouTube_TiempoTardado],
    [python,python_Incompleto,python_str,Python_TiempoTardado],
    [apple,apple_Incompleto,apple_str,Apple_TiempoTardado],
    [_3m,_3m_Incompleto,_3m_str,M3_TiempoTardado]]
random.shuffle(ListaNivel1)

ListaNivel2=[
    [_7up,_7up_incompleto,_7up_str,_7up_TiempoTardado],
    [adidas,adidas_incompleto,adidas_str,adidas_TiempoTardado],
    [amazon,amazon_incompleto,amazon_str,amazon_TiempoTardado],
    [bmw,bmw_incompleto,bmw_str,bmw_TiempoTardado],
    [duckduckgo,duckgo_incompleto,duckgi_str,duckduckgo_TiempoTardado],
    [ea,ea_incompleto,ea_str,ea_TiempoTardado],
    [fanta,fanta_incompleto,fanta_str,fanta_TiempoTardado],
    [hasbro,hasbro_incompleto,hasbro_str,hasbro_TiempoTardado],
    [jacks,jacks_incompleto,jacks_str,jacks_TiempoTardado],
    [kfc,kfc_incompleto,kfc_str,kfc_TiempoTardado],
    [lego,lego_incompleto,lego_str,lego_TiempoTardado],
    [monster,monster_incompleto,monster_str,monster_TiempoTardado],
    [nfl,nfl_incompleto,nfl_str,nfl_TiempoTardado],
    [netflix,netflix_incompleto,netflix_str,netflix_TiempoTardado],
    [jrockets,jrockets_incompleto,jrockets_str,jrockets_TiempoTardado],
    [sega,sega_incompleto,sega_str,sega_TiempoTardado],
    [spacex,spacex_incompleto,spacex_str,spacex_TiempoTardado],
    [utorrent,utorrent_incompleto,utorrent_str,utorrent_TiempoTardado],
    [vscode,vscode_incompleto,vscode_str,vscode_TiempoTardado],
    [tosty,tosty_incompleto,tosty_str,tosty_TiempoTardado] ]
random.shuffle(ListaNivel2)

ListaNivel3=[
  [adobe, adobe_incompleto, adobe_str,adobe_TiempoTardado],
  [autodesk, autodesk_incompleto, autodesk_str,autodesk_TiempoTardado],
  [balance, balance_incompleto, balance_str,balance_TiempoTardado],
  [blackberry, blackberry_incompleto, blackberry_str,blackberry_TiempoTardado],
  [chevro, chevro_incompleto, chevro_str,chevro_TiempoTardado],
  [coke, coke_incompleto, coke_str,coke_TiempoTardado],
  [delMonte, delMonte_incompleto, delMonte_str,delMonte_TiempoTardado],
  [discord, discord_incompleto, discord_str,discord_TiempoTardado],
  [dreamworks, dreamworks_incompleto, dreamworks_str,dreamworks_TiempoTardado],
  [facebook, facebook_incompleto, facebook_str,facebook_TiempoTardado],
  [hulu, hulu_incompleto, hulu_str,hulu_TiempoTardado],
  [microsoft, microsoft_incompleto, microsoft_str,microsoft_TiempoTardado],
  [motorola, motorola_incompleto, motorola_str,motorola_TiempoTardado],
  [moyo, moyo_incompleto, moyo_str,moyo_TiempoTardado],
  [nascar, nascar_incompleto, nascar_str,nascar_TiempoTardado],
  [nike, nike_incompleto, nike_str,nike_TiempoTardado],
  [nintendo, nintendo_incompleto, nintendo_str,nintendo_TiempoTardado],
  [nissan, nissan_incompleto, nissan_str,nissan_TiempoTardado],
  [office, office_incompleto, office_str,office_TiempoTardado],
  [pyg, pyg_incompleto, pyg_str,pyg_TiempoTardado],
  [pizzahut, pizzahut_incompleto, pizzahut_str,pizzahut_TiempoTardado],
  [purina, purina_incompleto, purina_str,purina_TiempoTardado],
  [rayovac, rayovac_incompleto, rayovac_str,rayovac_TiempoTardado],
  [razer, razer_incompleto, razer_str,razer_TiempoTardado],
  [safari, safari_incompleto, safari_str,safari_TiempoTardado],
  [siman, siman_incompleto, siman_str,siman_TiempoTardado],
  [sprite, sprite_incompleto, sprite_str,sprite_TiempoTardado],
  [tacobell, tacobell_incompleto, tacobell_str,tacobell_TiempoTardado],
  [toyota, toyota_incompleto, toyota_str,toyota_TiempoTardado],
  [vlc, vlc_incompleto, vlc_str,vlc_TiempoTardado]
]
random.shuffle(ListaNivel3)

ListaNivel4=[
    [bimbo,bimbo_incompleto,bimbo_str,bimbo_TiempoTardado],
    [colgate,colgate_incompleto,colgate_str,colgate_TiempoTardado],
    [dell,dell_incompleto,dell_str,dell_TiempoTardado],
    [dhl,dhl_incompleto,dhl_str,dhl_TiempoTardado],
    [didi,didi_incompleto,didi_str,didi_TiempoTardado],
    [disney,disney_incompleto,disney_str,disney_TiempoTardado],
    [dominos,dominos_incompleto,dominos_str,dominos_TiempoTardado],
    [doritos,doritos_incompleto,doritos_str,doritos_TiempoTardado],
    [dospinos,dospinos_incompleto,dospinos_str,dospinos_TiempoTardado],
    [gatorade,gatorade_incompleto,gatorade_str,gatorade_TiempoTardado],
    [gog,gog_incompleto,gog_str,gog_TiempoTardado],
    [google,google_incompleto,google_str,google_TiempoTardado],
    [gucci,gucci_incompleto,gucci_str,gucci_TiempoTardado],
    [gillette,gillette_incompleto,gillette_str,gillette_TiempoTardado],
    [heineken,heineken_incompleto,heineken_str,heineken_TiempoTardado],
    [imperial,imperial_incompleto,imperial_str,imperial_TiempoTardado],
    [kellogs,kellogs_incompleto,kellogs_str,kellogs_TiempoTardado],
    [kolbi,kolbi_incompleto,kolbi_str,kolbi_TiempoTardado],
    [maggi,maggi_incompleto,maggi_str,maggi_TiempoTardado],
    [mastercard,mastercard_incompleto,mastercard_str,mastercard_TiempoTardado],
    [mattel,mattel_incompleto,mattel_str,mattel_TiempoTardado],
    [maxi,maxi_incompleto,maxi_str,maxi_TiempoTardado],
    [monopoly,monopoly_incompleto,monopoly_str,monopoly_TiempoTardado],
    [motorola,motorola_incompleto,motorola_str,motorola_TiempoTardado],
    [movistar,movistar_incompleto,movistar_str,movistar_TiempoTardado],
    [nestle,nestle_incompleto,nestle_str,nestle_TiempoTardado],
    [pali,pali_incompleto,pali_str,pali_TiempoTardado],
    [pixar,pixar_incompleto,pixar_str,pixar_TiempoTardado],
    [powerade,powerade_incompleto,powerade_str,powerade_TiempoTardado],
    [pozuelo,pozuelo_incompleto,pozuelo_str,pozuelo_TiempoTardado],
    [pringles,pringles_incompleto,pringles_str,pringles_TiempoTardado],
    [rareware,rareware_incompleto,rareware_str,rareware_TiempoTardado],
    [rexona,rexona_incompleto,rexona_str,rexona_TiempoTardado],
    [riot,riot_incompleto,riot_str,riot_TiempoTardado],
    [samsung,samsung_incompleto,samsung_str,samsung_TiempoTardado],
    [scott,scott_incompleto,scott_str,scott_TiempoTardado],
    [sony,sony_incompleto,sony_str,sony_TiempoTardado],
    [tesla,tesla_incompleto,tesla_str,tesla_TiempoTardado],
    [tigo,tigo_incompleto,tigo_str,tigo_TiempoTardado],
    [uber,uber_incompleto,uber_str,uber_TiempoTardado]
]
random.shuffle(ListaNivel4)

ListaNivel5=[
    [alka,alka_incompleto,alka_str,alka_TiempoTardado],
    [amd,amd_incompleto,amd_str,amd_TiempoTardado],
    [atyt,atyt_incompleto,atyt_str,atyt_TiempoTardado],
    [bacardi,bacardi_incompleto,bacardi_str,bacardi_TiempoTardado],
    [bandai,bandai_incompleto,bandai_str,bandai_TiempoTardado],
    [bayer,bayer_incompleto,bayer_str,bayer_TiempoTardado],
    [cacique,cacique_incompleto,cacique_str,cacique_TiempoTardado],
    [carlsjr,carlsjr_incompleto,carlsjr_str,carlsjr_TiempoTardado],
    [cdprojekt,cdprojekt_incompleto,cdprojekt_str,cdprojekt_TiempoTardado],
    [chanel,chanel_incompleto,chanel_str,chanel_TiempoTardado],
    [cisco,cisco_incompleto,cisco_str,cisco_TiempoTardado],
    [claro,claro_incompleto,claro_str,claro_TiempoTardado],
    [corvette,corvette_incompleto,corvette_str,corvette_TiempoTardado],
    [daniels,daniels_incompleto,daniels_str,daniels_TiempoTardado],
    [dos,dos_incompleto,dos_str,dos_TiempoTardado],
    [ebay,ebay_incompleto,ebay_str,ebay_TiempoTardado],
    [edge,edge_incompleto,edge_str,edge_TiempoTardado],
    [fedex,fedex_incompleto,fedex_str,fedex_TiempoTardado],
    [ferrari,ferrari_incompleto,ferrari_str,ferrari_TiempoTardado],
    [ford,ford_incompleto,ford_str,ford_TiempoTardado],
    [gmail,gmail_incompleto,gmail_str,gmail_TiempoTardado],
    [huawei,huawei_incompleto,huawei_str,huawei_TiempoTardado],
    [hyundai,hyundai_incompleto,hyundai_str,hyundai_TiempoTardado],
    [intel,intel_incompleto,intel_str,intel_TiempoTardado],
    [java,java_incompleto,java_str,java_TiempoTardado],
    [_max,_max_incompleto,_max_str,_max_TiempoTardado],
    [mcdonalds_1953,mcdonalds_1953_incompleto,mcdonalds_1953_str,mcdonalds_1953_TiempoTardado],
    [mercedes,mercedes_incompleto,mercedes_str,mercedes_TiempoTardado],
    [michelin,michelin_incompleto,michelin_str,michelin_TiempoTardado],
    [numar,numar_incompleto,numar_str,numar_TiempoTardado],
    [oralB,oralB_incompleto,oralB_str,oralB_TiempoTardado],
    [oreo,oreo_incompleto,oreo_str,oreo_TiempoTardado],
    [palmolive,palmolive_incompleto,palmolive_str,palmolive_TiempoTardado],
    [pampers,pampers_incompleto,pampers_str,pampers_TiempoTardado],
    [panasonic,panasonic_incompleto,panasonic_str,panasonic_TiempoTardado],
    [papajohns,papajohns_incompleto,papajohns_str,papajohns_TiempoTardado],
    [paypal,paypal_incompleto,paypal_str,paypal_TiempoTardado],
    [pepto,pepto_incompleto,pepto_str,pepto_TiempoTardado],
    [pinterest,pinterest_incompleto,pinterest_str,pinterest_TiempoTardado],
    [redbull,redbull_incompleto,redbull_str,redbull_TiempoTardado],
    [salsol,salsol_incompleto,salsol_str,salsol_TiempoTardado],
    [steam,steam_incompleto,steam_str,steam_TiempoTardado],
    [subway,subway_incompleto,subway_str,subway_TiempoTardado],
    [swim,swim_incompleto,swim_str,swim_TiempoTardado],
    [ups,ups_incompleto,ups_str,ups_TiempoTardado],
    [valve,valve_incompleto,valve_str,valve_TiempoTardado],
    [visa,visa_incompleto,visa_str,visa_TiempoTardado],
    [walmart,walmart_incompleto,walmart_str,walmart_TiempoTardado],
    [whatsapp,whatsapp_incompleto,whatsapp_str,whatsapp_TiempoTardado],
    [yamaha,yamaha_incompleto,yamaha_str,yamaha_TiempoTardado]
]
random.shuffle(ListaNivel5)
Lista_Niveles=[ListaNivel1,ListaNivel2,ListaNivel3,ListaNivel4,ListaNivel5]
              
Fondo = pygame.image.load("Media/Fondo.png").convert()
FondoNegro = pygame.image.load("Media/FondoNegro.png").convert_alpha()
FondoVictoria = pygame.image.load("Media/Victoria.png").convert_alpha()
Opciones = Font_Daydream_30.render("Elija su respuesta:",False,"aquamarine")
Nivel1 = Font_Daydream_100.render("Nivel 1",False,"aquamarine")
Nivel2 = Font_Daydream_100.render("Nivel 2",False,"aquamarine")
Nivel3 = Font_Daydream_100.render("Nivel 3",False,"aquamarine")
Nivel4 = Font_Daydream_100.render("Nivel 4",False,"aquamarine")
Nivel5 = Font_Daydream_100.render("Nivel 5",False,"aquamarine")
timer_animation = 0
point = 0
guess1_button = pygame.Rect(1125,190,300,60)
guess2_button = pygame.Rect(1125,290,300,60)
guess3_button = pygame.Rect(1125,390,300,60)
level=1
Cantidad_Logos_Admin = 10 
exitosas=0
NLogo=0
tiempo_admin = 30
tiempo = tiempo_admin
tempo = 60
lugar,lugar2,lugar3 = randomizer(exitosas)
gaming = False
leaderboard_icon=pygame.image.load("Media/Trofeo.png").convert_alpha()
leaderboard_title=Font_Empire_80.render("Leaderboard",False,"White")
leaderboard_background=pygame.image.load("Media/FondoLeaderboard.png").convert_alpha()
selfleaderboard_background=pygame.image.load("Media/FondoLeaderboard_Self.png").convert_alpha()
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
leaderboard_regresar=Font_Empire_40.render("Regresar",False,"White")
Play=Font_Daydream_50.render("Jugar",False,"Green")
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
cuatroCaracteres3=Font_Daydream_20.render("al menos 3 caracteres",False,colour3)
cuatroCaracteres1_red=Font_Daydream_20.render("*el usuario y la",False,"red")
cuatroCaracteres2_red=Font_Daydream_20.render("contrasena deben tener",False,"red")
cuatroCaracteres3_red=Font_Daydream_20.render("al menos 3 caracteres",False,"red")

USUARIOS={}
USUARIOS=cargarusuarios(USUARIOS)
print("USUARIOS:  ",USUARIOS)

#si USER es "START", se muestra la pantalla de inicio de sesion
#si es "admin" se abre la configuracion
#si es "CrearUsuario" se abre el menu para crear usuarios
#si es "user" se inicia el juego
USER="START"

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
            print("OPERACION TERMINADA")
            if USER=="user":
                guardarInfoUsuario(usuario_input,password_input,exitosas,tiempototal,promedio,tiemposLogos)
                mostrarInfoUsuario()
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if guess1_button.collidepoint(event.pos) and gaming == True:
                exitosas = exitosas + tr1 # -1 es igual a + (-1)
                NLogo+=1
                lugar,lugar2,lugar3 = randomizer(NLogo)
                tiempoanterior = Lista_Niveles[level-1][NLogo-1][3]
                Lista_Niveles[level-1][NLogo-1][3] = GuardarTiempos(tiempoanterior,tiempo)
                tiempo = tiempo_admin
            elif guess2_button.collidepoint(event.pos) and gaming == True:
                exitosas = exitosas + tr2 # -1 es igual a + (-1)
                NLogo+=1
                lugar,lugar2,lugar3 = randomizer(NLogo)
                tiempoanterior = Lista_Niveles[level-1][NLogo-1][3]
                Lista_Niveles[level-1][NLogo-1][3] = GuardarTiempos(tiempoanterior,tiempo)
                tiempo = tiempo_admin
            elif guess3_button.collidepoint(event.pos) and gaming == True:
                exitosas = exitosas + tr3 # -1 es igual a + (-1)
                NLogo+=1
                lugar,lugar2,lugar3 = randomizer(NLogo)
                tiempoanterior = Lista_Niveles[level-1][NLogo-1][3]
                Lista_Niveles[level-1][NLogo-1][3] = GuardarTiempos(tiempoanterior,tiempo)
                tiempo = tiempo_admin

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
        pygame.Rect(1500,100,60,60)
        leaderboard_button=pygame.draw.rect(screen,(245, 237, 169), pygame.Rect(1500, 30, 52, 52),  2, 3)
        screen.blit(leaderboard_icon, (1502,32))
        pygame.draw.rect(screen,colour1,textbox_usuario,0)
        pygame.draw.rect(screen,colour2,textbox_password,0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if leaderboard_button.collidepoint(event.pos) and gaming == False:
                USER = "Leaderboard_General"
        surface1=Font_Daydream_30.render(usuario_input,True,"white")
        surface2=Font_Daydream_30.render(password_input,True,"white")
        screen.blit(ingreso_text,(80,85))
        screen.blit(usuario_text,(textbox_usuario.x,textbox_usuario.y-51))
        screen.blit(surface1,(textbox_usuario.x+5,textbox_usuario.y+5))
        screen.blit(password_text,(textbox_password.x,textbox_password.y-51))
        screen.blit(surface2,(textbox_password.x+5,textbox_password.y+5))
        screen.blit(ingresar_text,(ingresar_button.x+1,ingresar_button.y+1))
        screen.blit(crearUsuario_text,(creacionUsuario_button.x,creacionUsuario_button.y))
        usuario_input=usuario_input.lower()
        password_input=password_input.lower()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ingresar_button.collidepoint(event.pos):
                usuario_input=usuario_input.lower()
                password_input=password_input.lower()
                if usuario_input=="admin" and password_input=="admin":
                        USER=usuario_input
                elif usuario_input in USUARIOS:
                    if password_input==USUARIOS[usuario_input]:
                        USER="Leaderboard_Self"
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

    elif USER=="Leaderboard_General":
        screen.blit(leaderboard_background,(0,0))
        screen.blit(leaderboard_title,(540,50))
        screen.blit(leaderboard_regresar,(20,800))
        leaderboard_regresar_button= pygame.Rect(20,790,200,60)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if leaderboard_regresar_button.collidepoint(event.pos) and gaming == False:
                USER = "START"

    elif USER == "Leaderboard_Self":
        screen.blit(selfleaderboard_background,(0,0))
        screen.blit(leaderboard_title,(540,50))
        screen.blit(Play,(650,800))
        selflead_play= pygame.Rect(640,790,280,70)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if selflead_play.collidepoint(event.pos) and gaming == False:
                USER = "s"


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
                if usuario_input.lower() in USUARIOS:
                    screen.blit(UsuarioRegistrado,(ingresar_button.x-20,ingresar_button.y+55))
                else:
                    if usuario_input!="" and password_input!="":
                        if len(usuario_input)>=3 and len(password_input)>=3:
                            if usuarioAgregado==False:
                                USUARIOS=agregarNuevoUsuario(usuario_input, password_input, USUARIOS)
                                print(USUARIOS)
                                usuarioAgregado=True
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
        password_input=""
        usuario_input=""
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
        
        time_changingtext=Font_Daydream_30.render(str(tiempo_admin),False,"black")
        logos_changingtext=Font_Daydream_30.render(str(Cantidad_Logos_Admin),False,"black")
        
        screen.blit(time_changingtext,(tiempo_button.x,tiempo_button.y))
        screen.blit(logos_changingtext,(CantLogos_button.x,CantLogos_button.y))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if regresar_button.collidepoint(event.pos):
                USER="START"
            elif tiempo_flecha_arriba.collidepoint(event.pos) and tiempo_admin<300:
                tiempo_admin=tiempo_admin+1
                tiempo=tiempo_admin
            elif tiempo_flecha_abajo.collidepoint(event.pos) and tiempo_admin>1:
                tiempo_admin=tiempo_admin-1
                tiempo=tiempo_admin
            elif logo_flecha_arriba.collidepoint(event.pos) and Cantidad_Logos_Admin<150:
                Cantidad_Logos_Admin=Cantidad_Logos_Admin+1
            elif logo_flecha_abajo.collidepoint(event.pos) and Cantidad_Logos_Admin>1:
                Cantidad_Logos_Admin=Cantidad_Logos_Admin-1
   
    else:
        if mostrar==True:
            #cambiar estas dos luego
            tiempototal=0
            promedio=0
            print('info sin cargar')
            mostrarInfoUsuario()
            infoUsuarioList=cargarInfoUsuario(exitosas,tiempototal,promedio, Lista_Niveles)
            exitosas=infoUsuarioList[0][0]
            tiempototal=infoUsuarioList[0][1]
            promedio=infoUsuarioList[0][2]
            tiemposLogos=infoUsuarioList[1]
            #Lista_Niveles=
            print('info cargada')
            mostrarInfoUsuario()
            mostrar=False

        if level == 1:
            gaming = True
            if exitosas < Cantidad_Logos_Admin*1 and NLogo<Cantidad_Logos_Admin*1:
                imagen,opcion = imageChoice(ListaNivel1, NLogo)
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
                screen.blit(Nivel1, (220, 750))
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
                    restart_button = pygame.Rect(700,710,300,60)
                    restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                    varposicional=700
                    timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                    screen.blit(restart_txt,(700,varposicional))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            elif NLogo!=exitosas and NLogo>=Cantidad_Logos_Admin*1:
                screen.blit(FondoNegro, (0,0))
                screen.blit(Perdiste_txt,(425,195))
                screen.blit(Perdiste_txt_shadow,(425,200))
                restart_button = pygame.Rect(700,710,300,60)
                restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                varposicional=700
                timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                screen.blit(restart_txt,(700,varposicional))
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            else:
                exitosas = 0
                NLogo=0
                level += 1

        elif level == 2:
            gaming = True
            if exitosas < Cantidad_Logos_Admin*2 and NLogo<Cantidad_Logos_Admin*2:
                imagen,opcion = imageChoice(ListaNivel2, NLogo)
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
                screen.blit(Nivel2, (220, 750))
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
                    restart_button = pygame.Rect(700,700,300,60)
                    restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                    varposicional=700
                    timer_animation, varposicional = animaciones(timer_animation, varposicional,posorigin=700)
                    screen.blit(restart_txt,(700,varposicional))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            elif NLogo!=exitosas and NLogo>=Cantidad_Logos_Admin*2:
                screen.blit(FondoNegro, (0,0))
                screen.blit(Perdiste_txt,(425,195))
                screen.blit(Perdiste_txt_shadow,(425,200))
                restart_button = pygame.Rect(700,710,300,60)
                restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                varposicional=700
                timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                screen.blit(restart_txt,(700,varposicional))
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            else:
                exitosas = 0
                NLogo=0
                level += 1

        elif level == 3:
            gaming = True
            if exitosas < Cantidad_Logos_Admin*3 and NLogo<Cantidad_Logos_Admin*3:
                imagen,opcion = imageChoice(ListaNivel3, NLogo)
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
                screen.blit(Nivel3, (220, 750))
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
                    restart_button = pygame.Rect(700,710,300,60)
                    restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                    varposicional=700
                    timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                    screen.blit(restart_txt,(700,varposicional))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            elif NLogo!=exitosas and NLogo>=Cantidad_Logos_Admin*3:
                screen.blit(FondoNegro, (0,0))
                screen.blit(Perdiste_txt,(425,195))
                screen.blit(Perdiste_txt_shadow,(425,200))
                restart_button = pygame.Rect(700,710,300,60)
                restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                varposicional=700
                timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                screen.blit(restart_txt,(700,varposicional))
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            else:
                exitosas = 0
                NLogo=0
                level += 1

        elif level == 4:
            gaming = True
            if exitosas < Cantidad_Logos_Admin*4 and NLogo<Cantidad_Logos_Admin*4:
                imagen,opcion = imageChoice(ListaNivel4, NLogo)
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
                screen.blit(Nivel4, (220, 750))
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
                    restart_button = pygame.Rect(700,710,300,60)
                    restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                    varposicional=700
                    timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                    screen.blit(restart_txt,(700,varposicional))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            elif NLogo!=exitosas and NLogo>=Cantidad_Logos_Admin*4:
                screen.blit(FondoNegro, (0,0))
                screen.blit(Perdiste_txt,(425,195))
                screen.blit(Perdiste_txt_shadow,(425,200))
                restart_button = pygame.Rect(700,710,300,60)
                restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                varposicional=700
                timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                screen.blit(restart_txt,(700,varposicional))
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            else:
                exitosas = 0
                NLogo=0
                level += 1

        elif level == 5:
            gaming = True
            if exitosas < Cantidad_Logos_Admin*5 and NLogo<Cantidad_Logos_Admin*5:
                imagen,opcion = imageChoice(ListaNivel5, NLogo)
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
                screen.blit(Nivel5, (220, 750))
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
                    restart_button = pygame.Rect(700,710,300,60)
                    restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                    varposicional=700
                    timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                    screen.blit(restart_txt,(700,varposicional))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            elif NLogo!=exitosas and NLogo>=Cantidad_Logos_Admin*5:
                screen.blit(FondoNegro, (0,0))
                screen.blit(Perdiste_txt,(425,195))
                screen.blit(Perdiste_txt_shadow,(425,200))
                restart_button = pygame.Rect(700,710,300,60)
                restart_txt = Font_Minecraft.render("Restart",False,(250, 242, 25))
                varposicional=700
                timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=700)
                screen.blit(restart_txt,(700,varposicional))
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            level=1
                            exitosas=0
                            NLogo=0
                            tiempo = tiempo_admin
            else:
                exitosas = 0
                NLogo=0
                level += 1
        else:
            gaming = False
            screen.blit(FondoVictoria, (0,0))
            victory_text = Font_Daydream_100.render("Ganaste",False,(252, 186, 3))
            victory_text_shadow = Font_Daydream_100.render("Ganaste",False,(186, 137, 0))
            varposicional=400
            timer_animation, varposicional = animaciones(timer_animation, varposicional, posorigin=400)
            screen.blit(victory_text_shadow,(400,varposicional+5))
            screen.blit(victory_text,(400,varposicional))

    pygame.display.update()
    clock.tick(60)