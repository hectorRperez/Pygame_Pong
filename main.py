# Funciona las modulos importados
import pygame
from pygame.locals import QUIT
import random

# Constantes para la inicializanción de la superficie de dibujo
VENTANA_HORI = 800
VENTANA_VERTI = 600
FPS = 60
BLANCO = (255, 255, 255)

#TODO estamos entendiendo la clase Estamos en esta parte del codígo
class PelotaPong:
    def __init__(self, fichero_imagen):
        # ------------- Atributos de la clase ----------------

        # Imagen de la pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()
        print('image:',self.imagen)
        # Dimensiones de la pelota
        self.ancho, self.alto = self.imagen.get_size()
        print('Ancho: ',self.ancho)
        print('Alto: ',self.alto)

        # Posición de la pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERTI / 2 - self.alto / 2
        print('X:',self.x)
        print('Y:',self.y)

        # Direccion de movimiento de la pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

        print('x: {} + dirx: {} = {} '.format(self.x,self.dir_x,(self.x+self.dir_x)))
        print('y: {} + diry: {} = {} '.format(self.y,self.dir_y,(self.y+self.dir_y)))
        print('-------------------------------------------')

    def rebotar(self):

        if self.x <= 0:
            self.dir_x = -self.dir_x
            print('Rebote x: ',self.dir_x)
        if self.x + self.ancho >= VENTANA_HORI:
            self.dir_x = -self.dir_x
            print('Rebote x: ',self.dir_x)
        if self.y <= 0:
            self.dir_y = -self.dir_y
            print('Rebote Y: ',self.dir_y)
        if self.y + self.alto >= VENTANA_VERTI:
            self.dir_y = -self.dir_y
            print('Rebote Y: ',self.dir_y)


def main():

    # Inicialización de Pygame
    pygame.init()

    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERTI))
    pygame.display.set_caption('Pong 1')

    #Se crea un nuevo objeto del Tipo PelotaPong
    pelota = PelotaPong('pelota_roja.jpg')

    jugando = True

    # Bucle principal
    while jugando:

        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        # Bucle que va detectando los eventos en pantalla
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False
                print('Se termino el juego')

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
