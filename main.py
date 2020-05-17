import pygame
from pygame.locals import QUIT


#Constantes para la inicializanción de la superficie de dibujo
VENTANA_HORI = 800
VENTANA_VERTI = 600
FPS = 60
BLANCO = (255,255,255)


def main():

    #Inicialización de Pygame
    pygame.init()

    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERTI))
    pygame.display.set_caption('Pong 1')

    jugando = True

    #Bucle principal
    while jugando:
        ventana.fill(BLANCO)

        #Bucle que va detectando los eventos en pantalla
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False
                print('Se termino el juego')

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    
    pygame.quit()

if __name__ == '__main__':
    main()