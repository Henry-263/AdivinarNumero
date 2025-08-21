import pygame
import os
import recursos
from juego import iniciar_juego


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

while active:

    screen.blit(recursos.fondo, (0, 0))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for i, linea in enumerate(texto):
        texto_menu = recursos.font_grande.render(linea, True, (color_texto[0], color_texto[1], color_texto[2]))
        boton_menu = texto_menu.get_rect(center=(recursos.anchura//2, 200 + i * 40 ))

        if listoParaJugar == True:
            pygame.draw.rect(screen, (color_boton[0], color_boton[1], color_boton[2]), boton_menu.inflate(20, 20), border_radius=10)
        screen.blit(texto_menu, boton_menu)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            active = False


        if boton_menu.collidepoint(mouse) and listoParaJugar and click[0]:
            listoParaJugar = False
            ganar = iniciar_juego() #Iniciamos el juego que se situa en otro codigo
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