import pygame
import os

pygame.init()

altura = 600
anchura = 800

nombre_ventana = "Juego de adivinar un numero"

ruta_fuente = os.path.join("Assets", "Fonts", "GODOFWAR.ttf")

font_normal = pygame.font.Font(ruta_fuente, 20)
font_grande = pygame.font.Font(ruta_fuente, 40)

ruta_fondo = os.path.join("Assets", "Fondo.png")
fondo = pygame.image.load(ruta_fondo)
fondo = pygame.transform.scale(fondo, (anchura, altura))

