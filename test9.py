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

#Fuentes
consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')


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
        self.radius = 42
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

        # Dispara
        if teclas[pygame.K_SPACE]:
            #jugador.disparo()
            #jugador.disparo2()
            jugador.disparo3()


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

    # def disparo(self):
    #     bala = Disparos(self.rect.centerx - 30, self.rect.top + 45)
    #     balas.add(bala)
    #
    # def disparo2(self):
    #     bala = Disparos(self.rect.centerx + 30, self.rect.top + 45)
    #     balas.add(bala)

    def disparo3(self):
        bala = Disparos(self.rect.centerx, self.rect.top + 15)
        balas.add(bala)

class Enemigos1(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (enemigo)
        self.image = pygame.image.load("principal/enemigo.png").convert()
        self.image.set_colorkey(NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 23

        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # Velocidad inicial del enemigo
        self.velocidad_x = random.randrange(-3, 3)
        self.velocidad_y = random.randrange(-3, 3)

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


class Enemigos2(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (enemigo)
        self.image = pygame.transform.scale(pygame.image.load("principal/enemigo3.png").convert(), (55, 55))
        self.image.set_colorkey(NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 23

        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # Velocidad inicial del enemigo
        self.velocidad_x = random.randrange(4, 7)
        self.velocidad_y = random.randrange(4, 7)

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


class Enemigos3(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (enemigo)
        self.image = pygame.transform.scale(pygame.image.load("principal/enemigo2.png").convert(), (50, 55))
        self.image.set_colorkey(NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 23

        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # Velocidad inicial del enemigo
        self.velocidad_x = random.randrange(8, 11)
        self.velocidad_y = random.randrange(8, 11)

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


class Disparos (pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.transform.scale(pygame.image.load("principal/disparo.png").convert(), (10, 40))
        self.image.set_colorkey(BLANCO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()

        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 10

        if self.rect.bottom < 0:
            self.kill


class Meteoritos (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_aleatoria = random.randrange(3)

        if self.img_aleatoria == 0:
            self.image = pygame.transform.scale(pygame.image.load("principal/meteorito1.png").convert(), (50, 50))
            self.radius = 25
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load("principal/meteorito1.png").convert(), (75, 75))
            self.radius = 37
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load("principal/meteorito1.png").convert(), (90, 90))
            self.radius = 45

        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = -self.rect.height

        self.velocidad_y = random.randrange(1, 10)

    def update(self):
        self.rect.y += self.velocidad_y

        if self.rect.top > ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = -self.rect.height
            #ANCHO
            self.velocidad_y = random.randrange(1, 10)


# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()

#Sistema de puntuaciones
puntuacion = 0

def muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(fuente, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)

# Grupo de sprites, instanciación del objeto jugador.
sprites = pygame.sprite.Group()
enemigos_1 = pygame.sprite.Group()
enemigos_2 = pygame.sprite.Group()
enemigos_3 = pygame.sprite.Group()
balas = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()

#Instanciación de enemigos
# for x in range(random.randrange(5) + 1):
#     enemigo = Enemigos()
#     enemigos.add(enemigo)

#Instanciación de jugador principal
jugador = Jugador()
sprites.add(jugador)

#Instanciación de meteoritos
# for x in range(10):
#     meteorito = Meteoritos()
#     meteoritos.add(meteorito)

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
    enemigos_1.update()
    enemigos_2.update()
    enemigos_3.update()
    balas.update()
    meteoritos.update()

    # colision = pygame.sprite.spritecollide(jugador, enemigos, False, pygame.sprite.collide_circle)
    # if colision:
    #     enemigo.image = pygame.image.load("principal/meteorito.png")
    #     enemigo.velocidad_y += 6
    #     enemigo.velocidad_x -= 12
    # elif enemigo.rect.top > ALTO:
    #     enemigo.kill()
    #
    # colision_disparos = pygame.sprite.groupcollide(enemigos, balas, False, True)
    #
    # if colision_disparos:
    #     enemigo.image = pygame.image.load("principal/meteorito.png")
    #     enemigo.velocidad_y += 6
    #     enemigo.velocidad_x -= 12
    # elif enemigo.rect.top > ALTO:
    #     enemigo.kill()

    colision1 = pygame.sprite.groupcollide(enemigos_1, balas, True, True)
    colision2 = pygame.sprite.groupcollide(enemigos_2, balas, True, True)
    colision3 = pygame.sprite.groupcollide(enemigos_3, balas, True, True)

    if colision1:
        puntuacion += 10

    if colision2:
        puntuacion += 25

    if colision3:
        puntuacion += 50

    if not enemigos_1 and not enemigos_2 and not enemigos_3:
        enemigo1 = Enemigos1()
        enemigos_1.add(enemigo1)

        enemigo2 = Enemigos2()
        enemigos_2.add(enemigo2)

        enemigo3 = Enemigos3()
        enemigos_3.add(enemigo3)

    # Fondo de pantalla, dibujo de sprites y formas geométricas.
    pantalla.fill(NEGRO)
    meteoritos.draw(pantalla)
    enemigos_1.draw(pantalla)
    enemigos_2.draw(pantalla)
    enemigos_3.draw(pantalla)
    sprites.draw(pantalla)
    balas.draw(pantalla)

    #Dibuja los textos en la pantalla
    muestra_texto(pantalla, consolas, str(puntuacion).zfill(7), AZUL, 40, ANCHO - 100, 50)

    # Actualiza el contenido de la pantalla.
    pygame.display.flip()

pygame.quit()
