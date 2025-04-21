import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Tamaño de la pantalla
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("🐍 Juego de la Serpiente")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tamaño del bloque de la serpiente
bloque = 20
velocidad = 10

# Fuente y reloj
fuente = pygame.font.SysFont("comicsansms", 25)
reloj = pygame.time.Clock()

def mostrar_puntaje(puntos):
    valor = fuente.render("Puntos: " + str(puntos), True, blanco)
    pantalla.blit(valor, [0, 0])
 
# Cargar imagen de la comida (manzana)
manzana_img = pygame.image.load("manzana.png")
manzana_img = pygame.transform.scale(manzana_img, (bloque, bloque))
    

def juego():
    game_over = False
    game_cerrar = False

    x = ancho / 2
    y = alto / 2
    dx = 0
    dy = 0

    cuerpo = []
    longitud = 1

    comida_x = round(random.randrange(0, ancho - bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto - bloque) / 20.0) * 20.0

    while not game_over:

        while game_cerrar:
            pantalla.fill(negro)
            mensaje = fuente.render("¡Perdiste! Presiona C para continuar o Q para salir", True, rojo)
            pantalla.blit(mensaje, [ancho / 10, alto / 2])
            mostrar_puntaje(longitud - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_cerrar = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -bloque
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = bloque
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -bloque
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = bloque
                    dx = 0

        if x >= ancho or x < 0 or y >= alto or y < 0:
            game_cerrar = True

        x += dx
        y += dy
        pantalla.fill(azul)
        pantalla.blit(manzana_img, (comida_x, comida_y))
        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        cuerpo.append(cabeza)

        if len(cuerpo) > longitud:
            del cuerpo[0]

        for parte in cuerpo[:-1]:
            if parte == cabeza:
                game_cerrar = True
                
        for parte in cuerpo:
            pygame.draw.rect(pantalla, negro, [parte[0], parte[1], bloque, bloque])

        mostrar_puntaje(longitud - 1)
        pygame.display.update()


        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ancho - bloque) / 20.0) * 20.0
            comida_y