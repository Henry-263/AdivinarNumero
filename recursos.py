import pygame
import os

pygame.init()

altura = 600
anchura = 800

nombre_ventana = "Juego de adivinar un numero"

ruta_fuente = os.path.join("Assets", "Fonts", "GODOFWAR.ttf")

font_normal = pygame.font.Font(ruta_fuente, 20)
font_grande = pygame.font.Font(ruta_fuente, 38)

ruta_fondo = os.path.join("Assets", "Fondo.png")
fondo = pygame.image.load(ruta_fondo)
fondo = pygame.transform.scale(fondo, (anchura, altura))

class Boton:
    def __init__(self, texto, pos, color_normal=(200, 200, 200), color_hover=(230, 230, 230), color_texto=(0, 0, 0)):
        self.texto = texto
        self.pos = pos
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.color_texto = color_texto
        self.font = font_grande

        self.texto_render = self.font.render(self.texto, True, self.color_texto)
        self.rect = self.texto_render.get_rect(center=pos)

    def dibujar(self, screen):

        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            color_fondo = self.color_hover
        else:
            color_fondo = self.color_normal

        pygame.draw.rect(screen, color_fondo, self.rect.inflate(20, 20), border_radius=10)
        screen.blit(self.texto_render, self.rect)

    def click(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        return self.rect.collidepoint(mouse) and click[0]

