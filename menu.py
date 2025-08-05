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
texto = ["Dale enter para jugar"]
listoParaJugar = True


while active:

    screen.blit(recursos.fondo, (0, 0))

    for i, linea in enumerate(texto):
        texto_menu = recursos.font_grande.render(linea, True, (0, 0, 0))
        screen.blit(texto_menu, (recursos.anchura // 2 - texto_menu.get_width() // 2, 200 + i * 40))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and listoParaJugar:
                listoParaJugar = False
                ganar = iniciar_juego() #Iniciamos el juego que se situa en otro codigo
                if  ganar is None:
                    active = False
                elif ganar:
                    texto = ["Felicidades has ganado"]
                else:
                    texto = ["Te has quedado sin intentos,", "has perdido"]
                inicio_tiempo = pygame.time.get_ticks()

    if pygame.time.get_ticks() - inicio_tiempo > 3000:
        texto = ["Dale enter para jugar"]
        listoParaJugar = True




    pygame.display.flip()
    clock.tick(60)

pygame.quit()