import pygame

ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    #pygame.display.flip()
    pantalla.fill(BLANCO)
    pygame.draw.line(pantalla, (ROJO),[100,100],[200,200],20)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
