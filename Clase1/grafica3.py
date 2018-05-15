import pygame

ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fin=False
    while not fin:
        pos = pygame.mouse.get_pos()
        #print pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print 'a'
            #if event.key ==pygame.K_ESCAPE:
                    #fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                btn = pygame.mouse.get_pressed()
                if btn[0]==1:
                    print 'click izq', pos
