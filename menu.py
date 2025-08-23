import pygame
import os
import recursos
from juego import iniciar_juego

class Boton:
    def __init__(self, texto, pos, color_normal=(200, 200, 200), color_hover=(230, 230, 230), color_texto=(0, 0, 0)):
        self.texto = texto
        self.pos = pos
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.color_texto = color_texto
        self.font = recursos.font_grande

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
        """Devuelve True si se hace click sobre el botón"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        return self.rect.collidepoint(mouse) and click[0]


pygame.init()

screen = pygame.display.set_mode((recursos.anchura, recursos.altura))
pygame.display.set_caption(recursos.nombre_ventana)

clock = pygame.time.Clock()

inicio_tiempo = 0
ganar = False
active = True
texto = ["Jugar"]
listoParaJugar = True
color_texto = [0, 0, 0]
color_boton = [200, 200, 200]
elegir_nivel = False

boton_facil = Boton("Facil", (recursos.anchura//2, 200), (200, 200, 200), (230, 230, 230), (0, 0, 0) )
boton_medio = Boton("Medio", (recursos.anchura//2, 250), (200, 200, 200), (230, 230, 230), (0, 0, 0) )
boton_dificil = Boton("Dificil", (recursos.anchura//2, 300), (200, 200, 200), (230, 230, 230), (0, 0, 0) )

while active:

    screen.blit(recursos.fondo, (0, 0))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for i, linea in enumerate(texto):
        texto_menu = recursos.font_grande.render(linea, True, (color_texto[0], color_texto[1], color_texto[2]))
        boton_menu = texto_menu.get_rect(center=(recursos.anchura//2, 200 + i * 40 ))

        if listoParaJugar == True and not elegir_nivel:
            pygame.draw.rect(screen, (color_boton[0], color_boton[1], color_boton[2]), boton_menu.inflate(20, 20), border_radius=10)
        screen.blit(texto_menu, boton_menu)

    if elegir_nivel == True:
        boton_facil.dibujar(screen)
        boton_medio.dibujar(screen)
        boton_dificil.dibujar(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            active = False


        if boton_menu.collidepoint(mouse) and listoParaJugar and click[0]:
            elegir_nivel = True


        if boton_facil.click() and elegir_nivel:
            listoParaJugar = False
            ganar = iniciar_juego(7) #Iniciamos el juego que se situa en otro codigo
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]

            else:
                texto = ["Te has quedado sin intentos,", "has perdido"]
                color_texto = [255, 0, 0]
            inicio_tiempo = pygame.time.get_ticks()

        if boton_medio.click() and elegir_nivel:
            listoParaJugar = False
            ganar = iniciar_juego(5) #Iniciamos el juego que se situa en otro codigo
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]

            else:
                texto = ["Te has quedado sin intentos,", "has perdido"]
                color_texto = [255, 0, 0]
            inicio_tiempo = pygame.time.get_ticks()


        if boton_dificil.click() and elegir_nivel:
            listoParaJugar = False
            ganar = iniciar_juego(3) #Iniciamos el juego que se situa en otro codigo
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]

            else:
                texto = ["Te has quedado sin intentos,", "has perdido"]
                color_texto = [255, 0, 0]
            inicio_tiempo = pygame.time.get_ticks()

        if listoParaJugar:
            if boton_menu.collidepoint(mouse):
                color_texto = [100, 100, 100]
                color_boton = [200, 160, 120]
            else:
                color_texto = [0, 0, 0]
                color_boton = [160, 120, 80]

    if pygame.time.get_ticks() - inicio_tiempo > 3000:
        texto = ["Jugar"]
        listoParaJugar = True




    pygame.display.flip()
    clock.tick(60)

pygame.quit()