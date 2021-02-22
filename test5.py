import pygame, random

# Tamaño de pantalla
ANCHO = 800
ALTO = 600

# FPS
FPS = 30

# Paleta de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
H_FA2F2F = (250, 47, 47)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
H_50D2FE = (94, 210, 254)


class Jugador(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load("principal/nave.png").convert()
        self.image.set_colorkey(BLANCO)
        self.image.set_colorkey(NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (ANCHO // 2, ALTO // 2)
        #self.rect.center = (400, 700)
        # Velocidad inicial del personaje
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        # Velocidad predeterminada cada vuelta del bucle si no pulsas nada
        self.velocidad_x = 0
        self.velocidad_y = 0

        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()

        # Mueve el personaje a la izquierda
        if teclas[pygame.K_a]:
            self.velocidad_x = -10
        # Mueve el personaje a la derecha
        if teclas[pygame.K_d]:
            self.velocidad_x = 10
        # Mueve el personaje arriba
        if teclas[pygame.K_w]:
            self.velocidad_y = -10
        # Mueve el personaje abajo
        if teclas[pygame.K_s]:
            self.velocidad_y = 10


        # Actualiza la velocida/posición del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y


        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        # Limita el margen de arriba
        if self.rect.top < 0:
            self.rect.top = 0
        # Limita el margen de abajo
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (enemigo)
        self.image = pygame.image.load("principal/enemigo.png").convert()
        self.image.set_colorkey(NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # Velocidad inicial del enemigo
        self.velocidad_x = random.randrange(-10, 10)
        self.velocidad_y = random.randrange(-10, 10)

    def update(self):
        # Actualiza la velocida/posición del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # Limita el margen de arriba
        if self.rect.top < 0:
            self.velocidad_y += 1
        # Limita el margen de abajo
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1


# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()

# Grupo de sprites, instanciación del objeto jugador.
sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

# for x in range(random.randrange(5) + 1):
#     enemigo = Enemigos()
#     enemigos.add(enemigo)

enemigo = Enemigos()
enemigos.add(enemigo)

jugador = Jugador()
sprites.add(jugador)

# Bucle de juego
ejecutando = True
while ejecutando:
    # Es lo que especifica la velocidad del bucle de juego
    clock.tick(FPS)
    # Eventos
    for event in pygame.event.get():
        # Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False

    # Actualización de sprites
    sprites.update()
    enemigos.update()

    colision = pygame.sprite.spritecollide(jugador, enemigos, False)

    if colision:
        enemigo.image = pygame.image.load("principal/meteorito.png")
        enemigo.velocidad_y += 6
        enemigo.velocidad_x -= 12
    elif enemigo.rect.top > ALTO:
        enemigo.kill()

    # Fondo de pantalla, dibujo de sprites y formas geométricas.
    pantalla.fill(NEGRO)
    sprites.draw(pantalla)
    enemigos.draw(pantalla)
    pygame.draw.line(pantalla, H_50D2FE, (400, 0), (400, 800), 1)
    pygame.draw.line(pantalla, AZUL, (0, 300), (800, 300), 1)
    # Actualiza el contenido de la pantalla.
    pygame.display.flip()

pygame.quit()
