import pygame
import random
from random import randint
#=============================================================================================================
NEGRO    = (   0,   0,   0)
BLANCO   = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO     = ( 255,   0,   0)
VERDE    = (   0, 255,   0)
var_global = 0
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
#======================================== RIVALES NIVEL 1 ====================================================
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
#=============================================================================================================
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
            be = BalaLakitu(ba)
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
#======================================== RIVALES NIVEL 2 ===================================================
#============================================================================================================
class Kamek(pygame.sprite.Sprite):
    def __init__(self,ka):
        pygame.sprite.Sprite.__init__(self)
        self.ka=ka
        self.dir=0
        self.x=2
        self.image = ka[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_x = -4
        self.var_y = 0
        self.rangodisparo = 2
        self.temporizador = random.randint(0,500)
    def update(self):
        if self.x < 3:
            self.x+=1
        else:
            self.x=0
        if(randint(0,150) < self.rangodisparo):
            be = BalaKamek(bk)
            be.rect.x = self.rect.x
            be.rect.y = self.rect.y + 25
            balasRival2.add(be)
            general2.add(be)
        self.image = ka[self.x][self.dir]
        if self.rect.y>=640-self.rect.height:
            self.rect.y=640 - self.rect.height
        if self.temporizador >= 0:
            self.temporizador -= 2
        else:
            self.rect.x += self.var_x
#=============================================================================================================
class BillBala(pygame.sprite.Sprite):
    def __init__(self,bi):
        pygame.sprite.Sprite.__init__(self)
        self.bi = bi
        self.dir = 0
        self.x = 10
        self.image = bi[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_x = -20
        self.temporizador = random.randint(0,400)
    def update(self):
        if self.x < 15:
            self.x+=1
        else:
            self.x=0
        self.image = bi[self.x+0][self.dir+0]
        if self.temporizador >= 0:
            self.temporizador -= 2
        else:
            self.rect.x += self.var_x
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
class BalaLakitu(pygame.sprite.Sprite):
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
class BalaKamek(pygame.sprite.Sprite):
    def __init__(self,bk):
        pygame.sprite.Sprite.__init__(self)
        self.bk=bk
        self.dir=0
        self.x=0
        self.image = bk[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_x = -6
    def update(self):
        self.rect.x+=self.var_x
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
#==============================================================================================================
class parteJuego:
    def __init__(self):
        self.booleanos=[True, False, False, False, False, False, False,False]
    def texto_inicia(self):
        return self.booleanos[0]
    def inicia(self):
        return self.booleanos[1]
    def level1(self):
        return self.booleanos[2]
    def level2(self):
        return self.booleanos[3]
    def level3(self):
        return self.booleanos[4]
    def level4(self):
        return self.booleanos[5]
    def level5(self):
        return self.booleanos[6]
    def level6(self):
        return self.booleanos[7]
    def sigParte(self):
        for b in range(len(self.booleanos)):
            if self.booleanos[b] and b!=len(self.booleanos)-1:
                self.booleanos[b]=False
                self.booleanos[b+1]=True
                return
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
    ka = Recortar('Kamek.png',8,3)
    bi = Recortar('Bill_Bala.png',26,1)
    bk = Recortar('bala_kamek.png',1,1)
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
#============================================Kamek============================================================
    EneKamek = pygame.sprite.Group()
    n = 5
    for i in range(n):
        k = Kamek(ka)
        k.rect.y = 640
        k.rect.x = random.randrange(1000,1200)
        EneKamek.add(k)
        general2.add(k)
#===========================================Bill_Bala===========================================================
    EneBill = pygame.sprite.Group()
    n=10
    for i in range(n):
        bb = BillBala(bi)
        bb.rect.x=random.randrange(1000,1500)
        bb.rect.y=random.randint(450,570)
        EneBill.add(bb)
        general2.add(bb)
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
    for p in range(3):
        vid = Vida(vi)
        vid.rect.x = tempx
        vid.rect.y = tempy
        tempx += 28
        vida.add(vid)
        general.add(vid)
#==========================================Vida_Nivel 2========================================================
    vida2 = pygame.sprite.Group()
    tempx = 120
    tempy = 640
    for p in range(3):
        vid2 = Vida(vi)
        vid2.rect.x = tempx
        vid2.rect.y = tempy
        tempx += 28
        vida2.add(vid2)
        general2.add(vid2)
#==========================================Balas==============================================================
    balasSonic = pygame.sprite.Group()              # Balas Sonic
    balasRival1 = pygame.sprite.Group()             # Balas de enemigos Nivel1
    balasRival2 = pygame.sprite.Group()             # Balas de enemigos Nivel2
#=========================================Gestion de Eventos==================================================
    puntaje = 0
    ptos = 3
    ptos2 = 3
    Pausa = False
    Fin_Juego = False
    partJuego=parteJuego()
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
                if event.key == pygame.K_x:
                    if True:
                        partJuego.sigParte()
                if event.key == pygame.K_t:
                    Fin_Juego = not Fin_Juego
                    var_global=0
                if event.key == pygame.K_v:
                    Fin_Juego  = not Fin_Juego
                    var_global=1

                if event.key == pygame.K_p:
                    Pausa = not Pausa

            if event.type == pygame.KEYUP:
                sonic.var_x = 0
                sonic.var_y = 0
                sonic.dir = 0
            if event.type == pygame.QUIT:
                fin = True
#====================================Colision de Sonic Con Goomba============================================
        for j in vida:
            ls_col1 = pygame.sprite.spritecollide(sonic,EneGoomba, True)
            for elem in ls_col1:
                vida.remove(j)
                general.remove(j)
                ptos-=1
#====================================Colision de Sonic Con Kamek=============================================
        for j in vida2:
            ls_col6 = pygame.sprite.spritecollide(sonic,EneKamek, True)
            for elem in ls_col6:
                vida2.remove(j)
                general2.remove(j)
                ptos2-=1
#====================================Colision de Sonic Con Bill_Bala=========================================
        for j in vida2:
            ls_col10 = pygame.sprite.spritecollide(sonic,EneBill, True)
            for elem in ls_col10:
                vida2.remove(j)
                general2.remove(j)
                ptos2-=1
#======================================Colision balas enemigas Nivel 1 con Sonic  ===========================
        for j in vida:
            ls_col2 = pygame.sprite.spritecollide(sonic,balasRival1, True)
            for elem in ls_col2:
                vida.remove(j)
                general.remove(j)
                ptos-=1
#======================================Colision balas enemigas Nivel 2 con Sonic  ============================
        for j in vida2:
            ls_col7 = pygame.sprite.spritecollide(sonic,balasRival2, True)
            for elem in ls_col7:
                vida2.remove(j)
                general2.remove(j)
                ptos2-=1
#==========================================Colision de balas enemigas Nivel 1 con linea en X==================
        ls_col3 = pygame.sprite.spritecollide(ln, balasRival1, True)
        for elem in ls_col3:
            for i in range(0,1):
                balasRival1.remove(elem)
                general.remove(elem)
#=============================================Colision de balasSonic con rivales de Nivel 1 ===================
        for b in balasSonic:
            ls_col4 = pygame.sprite.spritecollide(b,EneGoomba,True)
            for e in ls_col4:
                puntaje+=1
                EneGoomba.remove(e)
                balasSonic.remove()
                general.remove(b)
            ls_col5 = pygame.sprite.spritecollide(b,EneLakitu,True)
            for e in ls_col5:
                puntaje+=1
                EneLakitu.remove(e)
                b.kill()
                general.remove(b)
#=======================================Colision de balasSonic con rivale Kamek de Nivel 2 ======================
        for b in balasSonic:
            ls_col8 = pygame.sprite.spritecollide(b,EneKamek,True)
            for e in ls_col8:
                puntaje+=1
                EneKamek.remove(e)
                balasSonic.remove(b)
                general2.remove(b)
#====================================Colision de balasSonic con rivale Bill_Bala de Nivel 2 =====================
        for b in balasSonic:
            ls_col9 = pygame.sprite.spritecollide(b,EneBill,True)
            for e in ls_col9:
                puntaje+=1
                EneBill.remove(e)
                balasSonic.remove(b)
                general2.remove(b)
#=============================================================================================================
        fuente1 = pygame.font.SysFont('Comic Sans MS', 80) #Crea una fuente con tipo y tamaño
        fuente2 = pygame.font.SysFont('Comic Sans MS', 30) #Crea una fuente con tipo y tamaño
#=============================================================================================================
        if ptos == 0:
            Fin_Juego = True
            var_global = 0
        if ptos2 == 0:
            Fin_Juego = True
            var_global = 1
        if puntaje == 2:
            partJuego.sigParte()
            puntaje = 3

        if  partJuego.texto_inicia():
            pantalla.fill(NEGRO)
            texto1 = fuente2.render("SONIC......... ", True, BLANCO)
            pantalla.blit(texto1,[280,300])
            pygame.display.flip()

        elif partJuego.inicia():
            pantalla.fill(NEGRO)
            texto1 = fuente2.render(".dialogos ", True, BLANCO)
            pantalla.blit(texto1,[280,300])
            pygame.display.flip()


        elif not Fin_Juego and not Pausa and partJuego.level1():
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

        elif not Fin_Juego and not Pausa and partJuego.level2():  #Presione espacio para continuar a nivel 2
            pantalla.fill(NEGRO)
            levelc = pygame.image.load ('level.png')
            pantalla.blit(levelc,[208,100])
            textop = fuente2.render("Your current score:", True, BLANCO)
            pantalla.blit(textop,[300,340])
            textopp=fuente2.render(str(puntaje), True, BLANCO)
            pantalla.blit(textopp,[500,340])
            textoppp = fuente2.render("fin nivel 1 ", True, BLANCO)
            pantalla.blit(textoppp,[280,400])
            pygame.display.flip()

        elif not Fin_Juego and not Pausa and partJuego.level3():
            general2.update()
            pantalla.fill(NEGRO)
            general2.draw(pantalla)
            texto1 = fuente2.render("LIVES: ", True, BLANCO)
            pantalla.blit(texto1,[20,650])
            puntos2 = fuente2.render(str(ptos2), True, BLANCO)
            pantalla.blit(puntos2,[95,650])
            texto3 = fuente2.render("POINTS: ", True, BLANCO)
            pantalla.blit(texto3,[850,650])
            texto4=fuente2.render(str(puntaje), True, BLANCO)
            pantalla.blit(texto4,[950,650])
            texto3 = fuente2.render("LEVEL 2", True, BLANCO)
            pantalla.blit(texto3,[470,650])
            pygame.display.flip()
            reloj.tick(15)

        elif not Fin_Juego and not Pausa and partJuego.level4():  #Presione espacio para continuar a nivel 2
            pantalla.fill(NEGRO)
            levelc = pygame.image.load ('level.png')
            pantalla.blit(levelc,[208,100])
            textop = fuente2.render("Your current score:", True, BLANCO)
            pantalla.blit(textop,[300,340])
            textopp=fuente2.render(str(puntaje), True, BLANCO)
            pantalla.blit(textopp,[500,340])
            textoppp = fuente2.render("fin Nivel2 ", True, BLANCO)
            pantalla.blit(textoppp,[280,400])
            pygame.display.flip()

        elif not Fin_Juego and not Pausa and partJuego.level5():  #Presione espacio para continuar a nivel 2
            pantalla.fill(NEGRO)
            levelc = pygame.image.load ('level.png')
            pantalla.blit(levelc,[208,100])
            textop = fuente2.render("Your current score:", True, BLANCO)
            pantalla.blit(textop,[300,340])
            textopp=fuente2.render(str(puntaje), True, BLANCO)
            pantalla.blit(textopp,[500,340])
            textoppp = fuente2.render("dialogo con Princesa", True, BLANCO)
            pantalla.blit(textoppp,[280,400])
            pygame.display.flip()

        elif not Fin_Juego and not Pausa and partJuego.level6():  #Presione espacio para continuar a nivel 2
            pantalla.fill(NEGRO)
            levelc = pygame.image.load ('level.png')
            pantalla.blit(levelc,[208,100])
            textop = fuente2.render("Your current score:", True, BLANCO)
            pantalla.blit(textop,[300,340])
            textopp=fuente2.render(str(puntaje), True, BLANCO)
            pantalla.blit(textopp,[500,340])
            textoppp = fuente2.render("Nivel 3  ", True, BLANCO)
            pantalla.blit(textoppp,[280,400])
            pygame.display.flip()

        elif Fin_Juego == True:
            if var_global == 1:
                pantalla.fill(NEGRO)
                textop = fuente2.render("Victory:", True, BLANCO)
                pantalla.blit(textop,[300,340])
                textopp=fuente2.render(str(puntaje), True, BLANCO)
                pantalla.blit(textopp,[500,340])
                pygame.display.flip()
            if var_global == 0:
                pantalla.fill(NEGRO)
                fondo = pygame.image.load ('game1.png')
                pantalla.blit(fondo,[306,200])
                pygame.display.flip()

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
