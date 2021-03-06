# Funciona las modulos importados
import pygame
from pygame.locals import QUIT
import random

# Constantes para la inicializanción de la superficie de dibujo
VENTANA_HORI = 800
VENTANA_VERTI = 600
FPS = 60
BLANCO = (255, 255, 255)
NEGRO = (0,0,0) #Color del texto negro (RGB)

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

        #Puntuación de la pelota
        self.puntuacion = 0
        self.puntuacion_ia = 0

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

        print('------------ MOVIMIENTO PELOTA ---------------')
        print('x: {} + dirx: {} = {} '.format(self.x,self.dir_x,(self.x+self.dir_x)))
        print('y: {} + diry: {} = {} '.format(self.y,self.dir_y,(self.y+self.dir_y)))
        print('-------------------------------------------')

    def rebotar(self):

        if self.x <= 0:
            self.puntuacion_ia += 1
            print('Rebote X <= 0')
            print('Posición x: ',self.x)
            print('direccion x: ',self.dir_x)
            print('Luego del reinicio')
            self.reiniciar()
            print('Posición x: ',self.x)
            print('direccion x: ',self.dir_x)

        if self.x + self.ancho >= VENTANA_HORI:
            self.puntuacion += 1
            print('Rebote X >= VENTANA_HORI')
            print('Posición x: ',self.x)
            print('direccion x: ',self.dir_x)
            print('Luego del reinicio')
            self.reiniciar()
            print('Posición x: ',self.x)
            print('direccion x: ',self.dir_x)

        if self.y <= 0:
            self.dir_y = -self.dir_y
            print('Rebote Y <= 0')
            print('Posición y: ',self.y)
            print('direccion y: ',self.dir_y)

        if self.y + self.alto >= VENTANA_VERTI:
            self.dir_y = -self.dir_y
            print('Rebote Y  >= VENTANA_VERTI')
            print('Posición y: ',self.y)
            print('direccion y: ',self.dir_y)
    
    def reiniciar(self):
        #Posición de la pelota en el medio
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERTI / 2 - self.alto / 2

        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5,5])

class RaquetaPong:
    def __init__(self):
        self.image = pygame.image.load('raqueta.jpg').convert_alpha()
        print('Image raqueta: ',self.image)
        #-------------- Atributos de la raqueta ------------------

        #Dimensiones de la raqueta
        self.ancho , self.alto = self.image.get_size()
        
        #Ancho 14
        print('ancho raqueta: ',self.ancho)

        #Largo 77
        print('alto raqueta: ',self.alto)

        #Posición de la raqueta
        self.x = 0

        #El valor de self.y es 261.5
        self.y = VENTANA_VERTI / 2 - self.alto / 2

        #Dirección de movimiento de la raqueta
        self.dir_y = 0


    def mover_raqueta(self):
        print(' ----------------------------- ')
        print('Función mover raqueta')
        print('Y: ',self.y)
        print('Dir Y: ',self.dir_y)
        self.y += self.dir_y
        print('Suma de movimiento: Y: {} + Y_dir: {} = {}'.format(self.y,self.dir_y,(self.y+self.dir_y)))
        print(' ----------------------------- ')
        if self.y <= 0:
            print('Dentro de la condición')
            self.y = 0
            print(self.y)
        
        if self.y + self.alto >= VENTANA_VERTI:
            self.y = VENTANA_VERTI - self.alto
    
    def golpear_raqueta(self,pelota):
        '''
        Metodo que se encarga de que la pelota sea golpeada por la raqueta
        parametros:

        Devuelve:

        '''
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto 
            ):
            print('------------- CONDICION DE GOLPE ---------')
            print('SE CUMPLIO 1------------------------')
            print('Pelota X: ',pelota.x)
            print('raqueta X: ',self.x)
            print('Ancho: ',self.ancho)
            print('SE CUMPLIO 2------------------------')
            print('Pelota X: ',pelota.x)
            print('raqueta X: ',self.x)
            print('SE CUMPLIO 3------------------------')
            print('Pelota Y: ',pelota.y)
            print('Alto Pelota: ',pelota.alto)
            print('Raqueta Y: ',self.y)
            print('SE CUMPLIO 4------------------------')
            print('Pelota Y: ',pelota.y)
            print('Raqueta Y: ',self.y)
            print('Alto raqueta: ',self.alto)

            pelota.dir_x = -pelota.dir_x
            pelota.x =  self.x + self.ancho
    
    def mover_ia(self,pelota):
        print('---------------------- Mover IA ---------------------- ')
        if self.y > pelota.y:
            print('Primera condición')
            self.dir_y = -4
            print('self.y > pelota.y')
        
        elif self.y < pelota.y:
            print('Segunda condición')
            self.dir_y = 4
            print('self.y < pelota.y')
        else:
            print('Tercera condición')
            self.dir_y = 0
            print('Ninguna condición se cumple')

        self.y += self.dir_y
        print('Movimiento de la raqueta IA: ',self.y)
        print('---------------------------------- ')
    
    def golpear_raqueta_ia(self, pelota):
        if (

            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y 
            and pelota.y < self.y + self.alto 
        ):

            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho

def main():

    # Inicialización de Pygame
    pygame.init()

    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERTI))
    pygame.display.set_caption('Pong 1')

    #Se crea un nuevo objeto del Tipo PelotaPong
    pelota = PelotaPong('pelota_roja.jpg')

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60
    print(' ----------------------------- ')
    print('Creación del objeto')
    print('X: ',raqueta_1.x)
    print('Y: ',raqueta_1.y)
    
    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    jugando = True

    # Bucle principal
    while jugando:

        pelota.mover()
        pelota.rebotar()

        raqueta_1.mover_raqueta()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear_raqueta(pelota)
        raqueta_2.golpear_raqueta_ia(pelota)
        

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        ventana.blit(raqueta_1.image, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.image, (raqueta_2.x, raqueta_2.y))

        fuente = pygame.font.Font(None, 60)

        #Codigo para mostrar la puntuación en pantalla
        texto = '{} : {} '.format(pelota.puntuacion, pelota.puntuacion_ia)
        letrero = fuente.render(texto, False, NEGRO)

        #El metodo blint dibuja en pantalla 
        #Recibe dos parametros, lo que se va a dibujar y la posición que tendrá el objeto en pantalla
        ventana.blit(letrero, (VENTANA_HORI / 2 - fuente.size(texto)[0] / 2, 50))


        # Bucle que va detectando los eventos en pantalla
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False
                print('Se termino el juego')
            
            #Detecta que se ha pulsado una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5
            
            #Detecta que se ha soltado la tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
