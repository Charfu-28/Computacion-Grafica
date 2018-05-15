import pygame
import random
from random import randint
#=============================================================================================================
NEGRO    = (   0,   0,   0)
BLANCO   = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO     = ( 255,   0,   0)
VERDE    = (   0, 255,   0)
#=============================================================================================================
ANCHO = 1000
ALTO  = 680
#=============================================================================================================
class Sonic(pygame.sprite.Sprite):
    def __init__(self,so):
        pygame.sprite.Sprite.__init__(self)
        self.so=so
        self.dir=0
        self.x=0
        self.var_x = 0
        self.var_y = 0
        self.image = so[self.x+3][self.dir+0]
        self.rect = self.image.get_rect()
    def gravedad(self):
        if self.var_y == 0:
            self.var_y = 1
        else:
            self.var_y += 1
        if self.rect.y >= (ALTO-40) - self.rect.height and self.var_y >= 0: #Limite Inferior
            self.var_y = 0
            self.rect.y = (ALTO-40) - self.rect.height
        if self.rect.x >= ANCHO - self.rect.width and self.var_x >= 0: # Limite  Derecha
            self.var_x = 0
            self.rect.x = ANCHO - self.rect.width
        if self.rect.x < 0:  #Limite Izquierda
            self.rect.x = 0
        if self.rect.y < 0:  #Limite Superior
            self.rect.y = 0
    def update(self):
        self.gravedad()
        if self.x < 1:
            self.x+=1
        else:
            self.x=0
        self.image = so[self.x+3][self.dir+0]
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.rect.x>=ANCHO-self.rect.width:
            self.rect.x=ANCHO - self.rect.width
        elif self.rect.x <= 0:
            self.var_x = 0
#=============================================================================================================
class Goomba (pygame.sprite.Sprite):
    def __init__(self,go):
        pygame.sprite.Sprite.__init__(self)
        self.go=go
        self.dir=0
        self.x=0
        self.image = go[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_x = -5
        self.var_y = 0
    def update(self):
        if self.x < 5:
            self.x+=1
        else:
            self.x=0
        self.image = go[self.x][self.dir]
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.rect.y>=640-self.rect.height:
            self.rect.y=640 - self.rect.height
#======================================== RIVALES NIVEL 2 ====================================================
class Lakitu(pygame.sprite.Sprite):
    def __init__(self,la):
        pygame.sprite.Sprite.__init__(self)
        self.la = la
        self.dir = 0
        self.x = 0
        self.image = la[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.rect.y= random.randint(0,50)
        self.var_y = 3
        self.var_x = 3
        self.rangodisparo = 2
        self.temporizador = random.randrange (300)
    def update(self):
        if self.x < 2:
            self.x+=1
        else:
            self.x=0
        self.image = la[self.x+0][self.dir+0]
        if(randint(0,30) < self.rangodisparo):
            be = BalaEnemigo(ba)
            be.rect.x = self.rect.x
            be.rect.y = self.rect.y
            balasRival1.add(be)
            general.add(be)
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.rect.x>=ANCHO-self.rect.width:
            self.var_x = -1.5
        elif (self.rect.x <= 0):
            self.var_x = 1.5
        if self.rect.y>=180-self.rect.height:
            self.var_y = -1
        elif (self.rect.y <= 0):
            self.var_y = 1
        if self.temporizador >= 0:
            self.temporizador -= 2
        else:
            self.rect.y += self.var_y
#=============================================================================================================
class DivisionPantalla (pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.var_x=0
        self.var_y=0
#=============================================================================================================
class Vida (pygame.sprite.Sprite):
    def __init__(self, vi):
        pygame.sprite.Sprite.__init__(self)
        self.vi=vi
        self.dir=0
        self.x=0
        self.image = vi[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_x=0
        self.var_y=0
#==============================================================================================================
class BalaEnemigo(pygame.sprite.Sprite):
    def __init__(self,ba):
        pygame.sprite.Sprite.__init__(self)
        self.ba=ba
        self.dir=1
        self.x=0
        self.image = ba[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_y = 7
    def update(self):
        self.rect.y+=self.var_y
#==============================================================================================================
class BalaSonic(pygame.sprite.Sprite):
    def __init__(self,bas):
        pygame.sprite.Sprite.__init__(self)
        self.bas=bas
        self.dir=0
        self.x=0
        self.image = bas[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_y = 0
        self.var_x = 5
    def update(self):
        self.rect.y+=self.var_y
        self.rect.x+=self.var_x
#======================================FUNCION PARA RECORTAR =================================================
def Recortar(archivo,an,al):
    imagen = pygame.image.load(archivo).convert_alpha()
    info = imagen.get_size()
    img_ancho = info[0]
    img_alto = info[1]
    corte_x = img_ancho/an
    corte_y = img_alto/al
    m = []
    for i in range (an):
        fila = []
        for j in range (al):
            cuadro = [i*corte_x,j*corte_y,corte_x,corte_y]
            recorte = imagen.subsurface(cuadro)
            fila.append(recorte)
        m.append(fila)
    return m
#===========================================Main==============================================================
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Sonic")
    so = Recortar('sonic_sprite.png',14,4)
    go = Recortar('goomba.png',15,2)
    vi = Recortar('vida1.png',1,1)
    la = Recortar('Lakitu.png',8,2)
    ba = Recortar('Lakitu.png',8,2)
    bas = Recortar('Fire3.png',1,1)
    pantalla.fill(NEGRO)
#============================================Sonic============================================================
    general = pygame.sprite.Group()
    general2 = pygame.sprite.Group()
    sonic = Sonic(so)
    general.add(sonic)
    general2.add(sonic)
    sonic.rect.x=370
    sonic.rect.y=560
#============================================Goomba============================================================
    EneGoomba = pygame.sprite.Group()
    n = 5
    for i in range(n):
        g = Goomba(go)
        g.rect.y = 640
        g.rect.x = random.randint(1000,1300)
        EneGoomba.add(g)
        general.add(g)
#===========================================Lakitu=============================================================
    EneLakitu = pygame.sprite.Group()
    n=5
    for i in range(n):
        l = Lakitu(la)
        l.rect.x=random.randrange(40, ANCHO - 40)
        l.rect.y=random.randrange(0, ALTO-460)
        EneLakitu.add(l)
        general.add(l)
#==========================================Linea De Division en X=============================================
    ln = DivisionPantalla(1000,2)
    general.add(ln)
    general2.add(ln)
    ln.rect.x = 0
    ln.rect.y = 640
#==========================================Vida_Nivel 1========================================================
    vida = pygame.sprite.Group()
    tempx = 120
    tempy = 640
    for p in range(5):
        vid = Vida(vi)
        vid.rect.x = tempx
        vid.rect.y = tempy
        tempx += 28
        vida.add(vid)
        general.add(vid)
        general2.add(vid)
#==========================================Balas==============================================================
    balasSonic = pygame.sprite.Group()
    balasRival1 = pygame.sprite.Group()
#=========================================Gestion de Eventos==================================================
    puntaje = 0
    ptos = 5
    Inicio = False
    Siguiente = False
    Pausa = False
    Fin_Juego = False
    Nivel2 = False
    Continuar = False
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sonic.var_x = -10
                    sonic.dir = 3
                if event.key == pygame.K_RIGHT:
                    sonic.var_x = 10
                    sonic.dir = 1
                if event.key == pygame.K_UP:
                    sonic.var_y = -20
                    sonic.dir = 2
                if event.key == pygame.K_LCTRL:
                    bs = BalaSonic(bas)
                    bs.rect.x = sonic.rect.x
                    bs.rect.y = sonic.rect.y+30
                    balasSonic.add(bs)
                    general.add(bs)
                    general2.add(bs)
                if event.key == pygame.K_p:
                    Pausa = not Pausa
                if event.key == pygame.K_RETURN:
                    Siguiente = not Siguiente
                if event.key == pygame.K_SPACE:
                    Continuar = not Continuar
            if event.type == pygame.KEYUP:
                sonic.var_x = 0
                sonic.var_y = 0
                sonic.dir = 0
            if event.type == pygame.QUIT:
                fin = True
#====================================Colision de Sonic Con Goomba=============================================
        for j in vida:
            ls_col1 = pygame.sprite.spritecollide(sonic,EneGoomba, True)
            for elem in ls_col1:
                vida.remove(j)
                general.remove(j)
                ptos-=1
#======================================Colision balas enemigas Nivel 1 con Sonic  ============================
        for j in vida:
            ls_col2 = pygame.sprite.spritecollide(sonic,balasRival1, True)
            for elem in ls_col2:
                vida.remove(j)
                general.remove(j)
                ptos-=1
#==========================================Colision de balas enemigas Nivel 1 con linea en X==================
        ls_col3 = pygame.sprite.spritecollide(ln, balasRival1, True)
        for elem in ls_col3:
            for i in range(0,1):
                balasRival1.remove(elem)
                general.remove(elem)
#=============================================Colision de balasSonic con rivales Nivel 1 ======================
        for b in balasSonic:
            ls_col4 = pygame.sprite.spritecollide(b,EneGoomba,True)
            for e in ls_col4:
                puntaje+=1
                EneGoomba.remove(e)
                balasSonic.remove(b)
                general.remove(b)
            ls_col5 = pygame.sprite.spritecollide(b,EneLakitu,True)
            for e in ls_col5:
                puntaje+=1
                EneLakitu.remove(e)
                balasSonic.remove(b)
                general.remove(b)
#=============================================================================================================
        fuente1 = pygame.font.SysFont('Comic Sans MS', 80) #Crea una fuente con tipo y tamaño
        fuente2 = pygame.font.SysFont('Comic Sans MS', 30) #Crea una fuente con tipo y tamaño
#=============================================================================================================
        if ptos == 0:
            Fin_Juego = True
        if ptos == 5:
            Inicio = True
        if puntaje == 5:
            Nivel2 = True
        if  Inicio == True and not Siguiente:
            pantalla.fill(NEGRO)
            texto1 = fuente2.render("SONIC.............Presione Enter para Continuar ", True, BLANCO)
            pantalla.blit(texto1,[280,300])
            pygame.display.flip()
            reloj.tick(60)
        elif not Fin_Juego and not Pausa and not Nivel2:
            general.update()
            pantalla.fill(NEGRO)
            general.draw(pantalla)
            texto1 = fuente2.render("LIVES: ", True, BLANCO)
            pantalla.blit(texto1,[10,650])
            texto5=fuente2.render(str(ptos), True, BLANCO)
            pantalla.blit(texto5,[95,650])
            texto3 = fuente2.render("POINTS: ", True, BLANCO)
            pantalla.blit(texto3,[850,650])
            texto4=fuente2.render(str(puntaje), True, BLANCO)
            pantalla.blit(texto4,[950,650])
            texto3 = fuente2.render("LEVEL 1", True, BLANCO)
            pantalla.blit(texto3,[470,650])
            pygame.display.flip()
            reloj.tick(12)
        elif Pausa == True:
            pantalla.fill(NEGRO)
            pause = pygame.image.load ('pause.png')
            pantalla.blit(pause,[372,100])
            texto6 = fuente1.render("GAME IN PAUSE", True, BLANCO)
            pantalla.blit(texto6,[270,400])
            texto1 = fuente2.render("Press P to continue ", True, BLANCO)
            pantalla.blit(texto1,[410,500])
            pygame.display.flip()
            reloj.tick(60)
        elif Nivel2 == True and not Continuar:  #Presione espacio para continuar a nivel 2
            pantalla.fill(NEGRO)
            levelc = pygame.image.load ('level.png')
            pantalla.blit(levelc,[208,100])
            textop = fuente2.render("Your current score:", True, BLANCO)
            pantalla.blit(textop,[300,340])
            textopp=fuente2.render(str(puntaje), True, BLANCO)
            pantalla.blit(textopp,[500,340])
            textoppp = fuente2.render("Press Space to continue ", True, BLANCO)
            pantalla.blit(textoppp,[280,400])
            pygame.display.flip()
            reloj.tick(60)
        elif Continuar == True:
            general2.update()
            pantalla.fill(NEGRO)
            general2.draw(pantalla)
            texto1 = fuente2.render("LIVES: ", True, BLANCO)
            pantalla.blit(texto1,[20,650])
            texto3 = fuente2.render("POINTS: ", True, BLANCO)
            pantalla.blit(texto3,[850,650])
            texto4=fuente2.render(str(puntaje), True, NEGRO)
            pantalla.blit(texto4,[950,650])
            texto3 = fuente2.render("LEVEL 2", True, BLANCO)
            pantalla.blit(texto3,[470,650])
            pygame.display.flip()
            reloj.tick(20)
        else:
            pantalla.fill(NEGRO)
            fondo = pygame.image.load ('game1.png')
            pantalla.blit(fondo,[306,200])
            pygame.display.flip()
            reloj.tick(60)
