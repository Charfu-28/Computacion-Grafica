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
        self.lista_plataformas=[]
        self.lista_Objeto=[]
        self.dir=0
        self.x=0
        self.var_x = 0
        self.var_y = 0
        self.inmune=False
        self.contador_inmune=0
        self.image = so[self.x+3][self.dir+0]
        self.rect = self.image.get_rect()
        self.abismo=False
    def saltar(self):
        self.var_y=-35
    def gravedad(self):
        if self.var_y==0:
            self.var_y=1
        else:
            self.var_y+=2
    def update(self):
        if self.inmune==True:
            self.contador_inmune+=1
        if self.contador_inmune==100:
            self.inmune=False
            self.contador_inmune=0
        self.gravedad()
        if self.x < 1:
            self.x+=1
        else:
            self.x=0
        self.image = so[self.x+3][self.dir+0]
        self.rect.x += self.var_x
        if self.rect.right>ANCHO:
            self.rect.right=ANCHO
        if self.rect.left<0:
            self.rect.left=0
        self.rect.y += self.var_y
        if self.rect.bottom>ALTO-35 and self.abismo==False:
            self.rect.bottom=ALTO-35
            self.var_y=0
        if self.rect.top<0:
            self.rect.top=0
        lista_colisiones = pygame.sprite.spritecollide(self,self.lista_plataformas,False)
        for bloque in lista_colisiones:
            if self.var_x > 0 and self.var_y<=0:
                self.rect.right = bloque.rect.left

            elif self.var_x < 0 and self.var_y<=0:
                self.rect.left = bloque.rect.right

        lista_colisiones = pygame.sprite.spritecollide(self,self.lista_plataformas,False)
        for bloque in lista_colisiones:
            if self.var_y > 0:
                self.rect.bottom = bloque.rect.top
                self.var_y=0
            elif self.var_y < 0:
                self.rect.top = bloque.rect.bottom
                self.var_y=0
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
        self.var_y = 0
        self.var_x = 5
        self.rangodisparo = 2
        self.temporizador = random.randrange (300)
    def update(self):
        if self.x < 2:
            self.x+=1
        else:
            self.x=0
        self.image = la[self.x+0][self.dir+0]
        if(randint(0,120) < self.rangodisparo):
            be = BalaLakitu(ba)
            be.rect.x = self.rect.x
            be.rect.y = self.rect.y
            balasRival1.add(be)
            general.add(be)
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.rect.x>=ANCHO-self.rect.width:
            self.var_x = -5
        elif (self.rect.x <= 0):
            self.var_x = 5
        if self.rect.y>=180-self.rect.height:
            self.var_y = -5
        elif (self.rect.y <= 0):
            self.var_y = 5
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
        self.x=3
        self.image = ka[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_x = -5
        self.var_y = 0
        self.rangodisparo = 2
        self.temporizador = random.randint(0,500)
    def update(self):
        if self.x < 3:
            self.x+=1
        else:
            self.x=0
        if(randint(0,200) < self.rangodisparo):
            be = BalaKamek(bk)
            be.rect.x = self.rect.x
            be.rect.y = self.rect.y + 25
            balasRival2.add(be)
            general2.add(be)
        self.image = ka[self.x][self.dir]
        if self.rect.y>=630-self.rect.height:
            self.rect.y=630 - self.rect.height
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
        self.var_x = -40
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
class Estacionario(pygame.sprite.Sprite):
    def __init__(self,Es):
        pygame.sprite.Sprite.__init__(self)
        self.Es = Es
        self.dir = 0
        self.x = 0
        self.image = Es[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.var_y = 0
        self.rangodisparo = 2
#==============================================Jefe Nivel 3=================================================
class Bowser(pygame.sprite.Sprite):
    def __init__(self,bo):
        pygame.sprite.Sprite.__init__(self)
        self.bo = bo
        self.dir = 0
        self.x = 7
        self.image = bo[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.var_x = -3
        self.var_y = 0
        self.contador = 0
        self.ciclos=0
        self.t_inicial=30
        self.segundos = 30
        self.rangodisparo = 3
        self.temporizador = random.randrange (300)
    def update(self):
        if self.x < 2:
            self.x+=1
        else:
            self.x=0
        self.image = bo[self.x+0][self.dir+0]
        self.rect.x += self.var_x
        self.rect.y += self.var_y
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
        self.var_y = -1
        self.var_x = 30
    def update(self):
        self.rect.y+=self.var_y
        self.rect.x+=self.var_x
#=============================Funcion Para Recorrer Etapas del Juego========================================
class parteJuego:
    def __init__(self):
        self.booleanos=[True, False, False, False, False, False, False, False]
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
#==========================================================================================================
class Plataforma (pygame.sprite.Sprite):
    def __init__(self, pl):
        pygame.sprite.Sprite.__init__(self)
        self.pl = pl
        self.x=0
        self.image = pl[0][0]
        self.rect = self.image.get_rect()
#===========================================================================================================
class Num_Plataformas(pygame.sprite.Sprite):
    def __init__(self, pl, Num_plata):
        pygame.sprite.Sprite.__init__(self)
        for p in Num_plata:
            bloque = Plataforma(pl)
            bloque.rect.x = p[0]
            bloque.rect.y = p[1]
            lista_plataformas.add(bloque)
#===========================================================================================================
class Num_ObjetoDanino(pygame.sprite.Sprite):
    def __init__(self, Ob, Num_Object):
        pygame.sprite.Sprite.__init__(self)
        for p in Num_Object:
            d = Plataforma(Ob)
            d.rect.x = p[0]
            d.rect.y = p[1]
            lista_plataformas.add(d)
#=============================================================================================================
class Modificador(pygame.sprite.Sprite):
    def __init__(self,im,X_,Y_):
        pygame.sprite.Sprite.__init__(self)
        self.im=im
        self.dir=0
        self.x=0
        self.ini=X_
        self.image = self.im[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.rect.x=self.ini
        self.rect.y=Y_
    def update(self):
        if self.dir <= 2:
            self.dir = 0
        else:
            self.dir += 1
        self.image = self.im[self.x][self.dir]
        if f_x != 0:
            self.rect.x = self.ini+ f_x
#==============================================================================================================
class Modificador2(pygame.sprite.Sprite):
    def __init__(self,im,X_,Y_):
        pygame.sprite.Sprite.__init__(self)
        self.im=im
        self.dir=0
        self.x=0
        self.ini=X_
        self.image = self.im[self.x][self.dir]
        self.rect = self.image.get_rect()
        self.rect.x=self.ini
        self.rect.y=Y_
    def update(self):
        if self.dir <= 2:
            self.dir = 0
        else:
            self.dir += 1
        self.image = self.im[self.x][self.dir]
        if f_x2 != 0:
            self.rect.x = self.ini+ f_x2
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
    bas = Recortar('bala_sonic.png',1,1)
    ka = Recortar('Kamek.png',8,3)
    bi = Recortar('Bill_Bala.png',26,1)
    bk = Recortar('bala_kamek.png',1,1)
    bo = Recortar('Bowser.png',10,3)
    pl = Recortar('plataforma1.png',1,1)
    di = Recortar('diamantes.png',3,1)
    es = Recortar('gemas.png',3,1)
    Ob = Recortar('trampa2.png',1,1)
    Es = Recortar('Estacionario.png',1,1)
    ro = Recortar('roca.png',1,1)
#========================================== FONDO NIVEL 1=================================================
    fondo = pygame.image.load ('FondoNivel1.jpg')
    pantalla.blit(fondo,[0,0])
    info= fondo.get_size()
    fondo_ancho=info[0]
    fondo_alto=info[1]
    f_x=0
#========================================== FONDO NIVEL 2=================================================
    fondo2 = pygame.image.load ('FondoNivel2 (2).jpg')
    pantalla.blit(fondo2,[0,0])
    info2= fondo2.get_size()
    fondo2_ancho=info2[0]
    fondo2_alto=info2[1]
    f_x2=0
#========================================== FONDO NIVEL 3=================================================
    fondo3 = pygame.image.load ('FondoNivel3.jpg')
    pantalla.blit(fondo3,[0,0])
    info3= fondo2.get_size()
    fondo3_ancho=info3[0]
    fondo3_alto=info3[1]
    f_x3=0
#========================================== FONDO DIALOGO FINAL==============================================
    fondo4 = pygame.image.load ('DialogoFinal.jpg')
    pantalla.blit(fondo4,[0,0])
    info4= fondo2.get_size()
    fondo4_ancho=info4[0]
    fondo4_alto=info4[1]
    f_x4=0
#============================================Sonic============================================================
    general = pygame.sprite.Group()
    general2 = pygame.sprite.Group()
    general3 = pygame.sprite.Group()
    sonic = Sonic(so)
    general.add(sonic)
    general2.add(sonic)
    general3.add(sonic)
    sonic.rect.x=370
    sonic.rect.y=645
#============================================Goomba============================================================
    EneGoomba = pygame.sprite.Group()
    n = 5
    if (f_x%700==0):
        for i in range(n):
            g = Goomba(go)
            g.rect.y = 640
            g.rect.x = random.randint(1000,1500)
            EneGoomba.add(g)
            general.add(g)
#===========================================Lakitu=============================================================
    EneLakitu = pygame.sprite.Group()
    n=3
    for i in range(n):
        l = Lakitu(la)
        l.rect.x=random.randrange(40, ANCHO - 40)
        l.rect.y=random.randrange(0, ALTO-460)
        EneLakitu.add(l)
        general.add(l)
#============================================Enemigo Estacionario===============================================
    EnemigoEsta = pygame.sprite.Group()
    E = Estacionario(Es)
    E.rect.x=500
    E.rect.y=30
    EnemigoEsta.add(E)
    general2.add(E)
#============================================Kamek============================================================
    EneKamek = pygame.sprite.Group()
    n = 3
    if (f_x2%700==0):
        for i in range(n):
            k = Kamek(ka)
            k.rect.y = 630
            k.rect.x = random.randint(1000,1400)
            EneKamek.add(k)
            general2.add(k)
    if (f_x3 <= -2000 and f_x3 >= -3000):
        n = 3
        for i in range(n):
            k = Kamek(ka)
            k.rect.y = 630
            k.rect.x = random.randint(1000,1400)
            EneKamek.add(k)
            general3.add(k)
#===========================================Bill_Bala===========================================================
    EneBill = pygame.sprite.Group()
    n=4
    if (f_x2%700==0):
        for i in range(n):
            bb = BillBala(bi)
            bb.rect.x=random.randrange(1000,1500)
            bb.rect.y=random.randint(450,570)
            EneBill.add(bb)
            general2.add(bb)
    if (f_x3 <= 0 and f_x3 >= -1000):
        n=4
        for i in range(n):
            bb = BillBala(bi)
            bb.rect.x=random.randrange(1000,1500)
            bb.rect.y=random.randint(450,570)
            EneBill.add(bb)
            general3.add(bb)
#===========================================Jefe_ Bowser=======================================================
    JefeBowser = pygame.sprite.Group()
    bw = Bowser(bo)
    bw.rect.x = random.randrange(1000,1200)
    bw.rect.y = 540
    JefeBowser.add(bw)
#==========================================Linea De Division en X=============================================
    ln = DivisionPantalla(1000,0.2)
    general.add(ln)
    general2.add(ln)
    general3.add(ln)
    ln.rect.x = 0
    ln.rect.y = 640
#============================================MODIFICADOR NIVEL 1===============================================
    ModificadorNivel1 = pygame.sprite.Group()
    x=1300
    y=300
    mo = Modificador(di,x,y)
    ModificadorNivel1.add(mo)
    general.add(mo)
#============================================MODIFICADOR NIVEL 2===============================================
    ModificadorNivel2 = pygame.sprite.Group()
    x=random.randrange(1000,1600)
    y=200
    ge = Modificador2(es, x, y)
    ModificadorNivel2.add(ge)
    general2.add(ge)
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
#==========================================Vida_Nivel 2========================================================
    vida2 = pygame.sprite.Group()
    tempx2 = 120
    tempy2 = 640
    for p in range(5):
        vid2 = Vida(vi)
        vid2.rect.x = tempx2
        vid2.rect.y = tempy2
        tempx2 += 28
        vida2.add(vid2)
        general2.add(vid2)
#==========================================Vida_Nivel 3========================================================
    vida3 = pygame.sprite.Group()
    tempx3 = 120
    tempy3 = 640
    for p in range(5):
        vid3 = Vida(vi)
        vid3.rect.x = tempx3
        vid3.rect.y = tempy3
        tempx3 += 28
        vida3.add(vid3)
#==========================================Balas==============================================================
    balasSonic = pygame.sprite.Group()              # Balas Sonic
    balasRival1 = pygame.sprite.Group()             # Balas de enemigos Nivel1
    balasRival2 = pygame.sprite.Group()             # Balas de enemigos Nivel2
    lista_Objeto = pygame.sprite.Group()
#=========================================Gestion de Eventos==================================================
    f_con=0
    puntaje = 0
    ptos  = 1000
    ptos2 = 500
    ptos3 = 5
    Pausa = False
    Fin_Juego = False
    partJuego=parteJuego()
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
#=========================================Implmentacion Abismo==================================================
        if partJuego.level3() and f_x2<=-984 and f_x2>=-1250 and sonic.rect.x>=420 and sonic.rect.x<442 and sonic.rect.bottom==645:
            sonic.abismo=True
            sonic.var_y+=1
        if sonic.rect.y >= 700:
            Fin_Juego=True
#=================================Gommba en Todo el Recorrido===================================================
        n = 5
        if (f_x%700==0 and f_x!=0):
            for i in range(n):
                g = Goomba(go)
                g.rect.y = 640
                g.rect.x = random.randint(1000,1500)
                EneGoomba.add(g)
                general.add(g)
#================================BillBala en Todo el Recorrido====================================================
        n=4
        if (f_x2%700 == 0 and f_x2!=0):
            for i in range(n):
                bb = BillBala(bi)
                bb.rect.x=random.randrange(1000,1500)
                bb.rect.y=random.randint(450,570)
                EneBill.add(bb)
                general2.add(bb)
#====================================Kamek en Todo el Recorrido====================================================
        n = 3
        if (f_x2%700==0 and f_x2!=0):
            for i in range(n):
                k = Kamek(ka)
                k.rect.y = 630
                k.rect.x = random.randint(1000,1400)
                EneKamek.add(k)
                general2.add(k)
#==========================================Generando Gomba_Lakitu Nivel 3============================================
        if (f_x3 == -1000):
            n=3
            for i in range(n):
                g = Goomba(go)
                g.rect.y = 640
                g.rect.x = random.randint(1000,1100)
                EneGoomba.add(g)
                general3.add(g)
                '''l = Lakitu(la)
                l.rect.x=random.randrange(40, ANCHO - 40)
                l.rect.y=random.randrange(0, ALTO-460)
                EneLakitu.add(l)
                general3.add(l)'''
#==========================================Generando Kamek Nivel 3============================================

#======================================Eventos================================================================
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sonic.var_x = -20
                    sonic.dir = 3
                if event.key == pygame.K_RIGHT:
                    sonic.var_x = 20
                    sonic.dir = 1
                if event.key == pygame.K_DOWN and sonic.rect.bottom!=640:
                    sonic.var_y = 5
                    sonic.dir = 2
                if sonic.var_y==0:
                    if event.key == pygame.K_UP and sonic.var_y==0:
                        sonic.saltar()
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
                        sonic.rect.x=370
                        partJuego.sigParte()
                if event.key == pygame.K_t:
                    Fin_Juego = not Fin_Juego
                    var_global=0
                if event.key == pygame.K_v:
                    Fin_Juego  = not Fin_Juego
                    var_global=1
                if event.key == pygame.K_r:
                    Fin_Juego = not Fin_Juego
                    var_global=2
                if event.key == pygame.K_i:
                    Fin_Juego  = not Fin_Juego
                    var_global=3
                if event.key == pygame.K_p:
                    Pausa = not Pausa
            if event.type == pygame.KEYUP:
                sonic.var_x = 0
                sonic.var_y = 0
                sonic.dir = 0
            if event.type == pygame.QUIT:
                fin = True
#====================================Colision de Sonic con Modificador 1======================================
        ls_col14 = pygame.sprite.spritecollide(sonic,ModificadorNivel1, True)
        for elem in ls_col14:
            elem.kill()
            sonic.inmune=True
#====================================Colision de Sonic con Modificador 2======================================
        ls_col15 = pygame.sprite.spritecollide(sonic,ModificadorNivel2, True)
        for elem in ls_col15:
            elem.kill()
            ptos2 +=1
            v = Vida(vi)
            v.rect.x = tempx2
            v.rect.y = tempy2
            tempx2 += 28
            vida2.add(v)
            general2.add(v)
#====================================Colision de Sonic Con Goomba============================================
        for j in vida:
            ls_col1 = pygame.sprite.spritecollide(sonic,EneGoomba, True)
            for elem in ls_col1:
                if sonic.inmune==False:
                    vida.remove(j)
                    general.remove(j)
                    ptos-=1
#====================================Colision de Sonic Con Kamek ============================================
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
                if sonic.inmune==False:
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
                b.kill()
            ls_col5 = pygame.sprite.spritecollide(b,EneLakitu,True)
            for e in ls_col5:
                puntaje+=1
                EneLakitu.remove(e)
                b.kill()
#=====================================Colision de balasSonic con rivale Kamek de Nivel 2 =====================
        for b in balasSonic:
            ls_col8 = pygame.sprite.spritecollide(b,EneKamek,True)
            for e in ls_col8:
                puntaje+=1
                EneKamek.remove(e)
                b.kill()
#====================================Colision de balasSonic con rivale Bill_Bala de Nivel 2 ====================
        for b in balasSonic:
            ls_col9 = pygame.sprite.spritecollide(b,EneBill,True)
            for e in ls_col9:
                puntaje+=1
                EneBill.remove(e)
                b.kill()
#=========================================== Fuentes =======================================================
        fuente1 = pygame.font.SysFont('Comic Sans MS', 80) #Crea una fuente con tipo y tamaño
        fuente2 = pygame.font.SysFont('Comic Sans MS', 30) #Crea una fuente con tipo y tamaño
        fuente3 = pygame.font.SysFont('Comic Sans MS', 45) #Crea una fuente con tipo y tamaños
#======================================Condicion de Derrota Nivel 1=========================================
        if ptos == 0:
            Fin_Juego = True
            var_global = 0
#======================================Condicion de Derrota Nivel 2=========================================
        if ptos2 == 0:
            Fin_Juego = True
            var_global = 0
#======================================Condicion de Derrota Nivel 3=========================================
        if ptos3 == -500:
            Fin_Juego = True #POR EL MOMEMNTO NO FUNCIONA
            var_global = 0
#======================================Condicion de Victoria Nivel 2========================================
        if partJuego.level1() and sonic.rect.x>=830 and sonic.rect.y<=896 and f_x==-3000:
            sonic.rect.x=370
            partJuego.sigParte()
#======================================Condicion de Victoria Nivel 3=========================================
        if partJuego.level3() and sonic.rect.x>=740 and sonic.rect.y<=876 and f_x2==-4000:
            sonic.rect.x=370
            partJuego.sigParte()
#============================================================================================================
        if  partJuego.texto_inicia() and not Fin_Juego:
            pantalla.fill(NEGRO)
            panini = pygame.image.load ('FondoInicio.png')
            pantalla.blit(panini,[0,0])
            texto1 = fuente3.render("CREDITOS(R)", True, NEGRO)
            pantalla.blit(texto1,[30,620])
            texto2 = fuente3.render("INSTRUCIONES(I)", True, NEGRO)
            pantalla.blit(texto2,[340,620])
            texto3 = fuente3.render("INICIO JUEGO(X)", True, NEGRO)
            pantalla.blit(texto3,[720,620])
            pygame.display.flip()

        elif partJuego.inicia() and not Fin_Juego:
            pantalla.fill(NEGRO)
            dialogo = pygame.image.load ('DialogoInicio.png')
            pantalla.blit(dialogo,[0,0])
            pres3 = fuente3.render("Presione X para Continuar", True,NEGRO)
            pantalla.blit(pres3,[320,630])
            pygame.display.flip()

        elif not Fin_Juego and not Pausa and partJuego.level1():
            pantalla.blit(fondo, [f_x, 0])
            general.update()
            lista_plataformas = pygame.sprite.Group()
            Num_plata = [[1545+f_x,580],[800+f_x,500], [1300+f_x,400],[1780+f_x,400],[2000+f_x,500], [2500+f_x,520],[2900+f_x,490],[3520+f_x,560]]
            Num_Object =[[600+f_x,620]]
            Num_ObjetoDanino(Ob,Num_Object)
            Num_Plataformas(pl, Num_plata)
            sonic.lista_plataformas=lista_plataformas
            sonic.lista_Objeto=lista_Objeto
            texto1 = fuente2.render("VIDAS: ", True, NEGRO)
            texto5=fuente2.render(str(ptos), True, NEGRO)
            texto3 = fuente2.render("PUNTOS: ", True, NEGRO)
            texto4=fuente2.render(str(puntaje), True, NEGRO)
            textoe = fuente2.render("NIVEL 1", True, NEGRO)
            if sonic.rect.x>=ANCHO/2+200-sonic.rect.width and f_x+fondo_ancho>ANCHO and sonic.var_x!=0:
                sonic.rect.x=ANCHO/2+200-sonic.rect.width
                f_x -= 4
            if sonic.rect.x<=ANCHO/2-200-sonic.rect.width and f_x<0 and sonic.var_x!=0:
                sonic.rect.x=ANCHO/2-200-sonic.rect.width
                f_x += 4
            pantalla.blit(texto1,[10,650])
            pantalla.blit(texto5,[95,650])
            pantalla.blit(texto3,[850,650])
            pantalla.blit(texto4,[950,650])
            pantalla.blit(textoe,[470,650])
            general.draw(pantalla)
            lista_plataformas.draw(pantalla)
            lista_Objeto.draw(pantalla)
            pygame.display.flip()
            reloj.tick(15)

        elif not Fin_Juego and not Pausa and partJuego.level2():
            pantalla.fill(NEGRO)
            lev1 = pygame.image.load ('nivel2_historia1.png')
            pantalla.blit(lev1,[0,0])
            textop = fuente2.render("Puntos Acumulados:", True, NEGRO)
            pantalla.blit(textop,[60,460])
            textopp=fuente2.render(str(puntaje), True, NEGRO)
            pantalla.blit(textopp,[300,460])
            pres1 = fuente2.render("Presione X para Continuar", True, NEGRO)
            pantalla.blit(pres1,[60,520])
            pygame.display.flip()

        elif not Fin_Juego and not Pausa and partJuego.level3():
            general2.update()
            lista_plataformas = pygame.sprite.Group()
            Num_plata = [[1545+f_x2,540],[800+f_x2,500], [1300+f_x2,400],[1780+f_x2,400],[2000+f_x2,500], [2500+f_x2,520],[2900+f_x2,460],[3300+f_x2,470],
            [3800+f_x2,520],[4200+f_x2,480]]
            Num_Plataformas(pl, Num_plata)
            sonic.lista_plataformas=lista_plataformas
            texto1 = fuente2.render("VIDAS: ", True, BLANCO)
            puntos2 = fuente2.render(str(ptos2), True, BLANCO)
            texto3 = fuente2.render("PUNTOS: ", True, BLANCO)
            texto4=fuente2.render(str(puntaje), True, BLANCO)
            textol2 = fuente2.render("NIVEL 2", True, BLANCO)
            if sonic.rect.x>=ANCHO/2+4-sonic.rect.width and f_x2+fondo2_ancho>ANCHO and sonic.var_x!=0:
                sonic.rect.x=ANCHO/2+4-sonic.rect.width
                f_x2 -= 4
            if sonic.rect.x<=ANCHO/2-4-sonic.rect.width and f_x2<0 and sonic.var_x!=0:
                sonic.rect.x=ANCHO/2-4-sonic.rect.width
                f_x2 += 4
            pantalla.blit(fondo2, [f_x2, 0])
            pantalla.blit(texto1,[20,650])
            pantalla.blit(puntos2,[95,650])
            pantalla.blit(texto3,[850,650])
            pantalla.blit(texto4,[950,650])
            pantalla.blit(textol2,[470,650])
            general2.draw(pantalla)
            lista_plataformas.draw(pantalla)
            pygame.display.flip()
            reloj.tick(15)

        elif not Fin_Juego and not Pausa and partJuego.level4():
            pantalla.fill(NEGRO)
            lev2 = pygame.image.load ('nivel3_historia1.png')
            pantalla.blit(lev2,[0,0])
            textop = fuente2.render("Puntos Acumulados:", True, NEGRO)
            pantalla.blit(textop,[60,400])
            textopp=fuente2.render(str(puntaje), True, NEGRO)
            pantalla.blit(textopp,[300,400])
            pres2 = fuente2.render("Presione X para Continuar", True,NEGRO)
            pantalla.blit(pres2,[60,460])
            pygame.display.flip()

        elif not Fin_Juego and not Pausa and partJuego.level5():
            print(f_x3,sonic.rect.x)
            general3.update()
            vidass = fuente2.render("VIDAS: ", True, BLANCO)
            puntos2 = fuente2.render(str(ptos2), True, BLANCO)
            texto3 = fuente2.render("PUNTOS: ", True, BLANCO)
            texto4=fuente2.render(str(puntaje), True, BLANCO)
            textol2 = fuente2.render("NIVEL 3", True, BLANCO)
            if sonic.rect.x>=ANCHO/2+4-sonic.rect.width and f_x3+fondo3_ancho>ANCHO and sonic.var_x!=0:
                sonic.rect.x=ANCHO/2+4-sonic.rect.width
                f_x3 -= 4
            if sonic.rect.x<=ANCHO/2-4-sonic.rect.width and f_x3<0 and sonic.var_x!=0:
                sonic.rect.x=ANCHO/2-4-sonic.rect.width
                f_x3 += 4
            pantalla.blit(fondo3, [f_x3, 0])
            pantalla.blit(vidass,[20,650])
            pantalla.blit(puntos2,[95,650])
            pantalla.blit(texto3,[850,650])
            pantalla.blit(texto4,[950,650])
            pantalla.blit(textol2,[470,650])
            general3.draw(pantalla)
            pygame.display.flip()
            reloj.tick(15)

        elif not Fin_Juego and not Pausa and partJuego.level6():
            if sonic.rect.x>=ANCHO/2+4-sonic.rect.width and f_x4+fondo4_ancho>ANCHO and sonic.var_x!=0:
                sonic.rect.x=ANCHO/2+4-sonic.rect.width
                f_x4 -= 4
            if sonic.rect.x<=ANCHO/2-4-sonic.rect.width and f_x4<0 and sonic.var_x!=0:
                sonic.rect.x=ANCHO/2-4-sonic.rect.width
                f_x4 += 4
            pantalla.blit(fondo4, [f_x4, 0])
            pygame.display.flip()

        elif Fin_Juego == True:
            if var_global == 3:
                pantalla.fill(NEGRO)
                cred = pygame.image.load ('Instrucciones.png')
                pantalla.blit(cred,[0,0])
                pres4 = fuente3.render("Presione I para Continuar", True, NEGRO)
                pantalla.blit(pres4,[280,600])
                pygame.display.flip()
            if var_global == 2:
                pantalla.fill(NEGRO)
                cred = pygame.image.load ('creditos.png')
                pantalla.blit(cred,[0,0])
                pres5 = fuente2.render("Presione R para Continuar", True, NEGRO)
                pantalla.blit(pres5,[40,600])
                pygame.display.flip()
            if var_global == 1:
                pantalla.fill(NEGRO)
                textop = fuente2.render("Victory:", True, BLANCO)
                pantalla.blit(textop,[300,340])
                textopp=fuente2.render(str(puntaje), True, BLANCO)
                pantalla.blit(textopp,[500,340])
                pygame.display.flip()
            if var_global == 0:
                pantalla.fill(NEGRO)
                fondo = pygame.image.load ('game2.png')
                pantalla.blit(fondo,[0,0])
                pygame.display.flip()

        elif Pausa == True:
            pantalla.fill(NEGRO)
            pause = pygame.image.load ('pause.png')
            pantalla.blit(pause,[372,100])
            texto6 = fuente1.render("JUEGO EN PAUSA", True, BLANCO)
            pantalla.blit(texto6,[270,400])
            texto1 = fuente2.render("Presione P para Continuar", True, BLANCO)
            pantalla.blit(texto1,[410,500])
            pygame.display.flip()
            reloj.tick(60)
