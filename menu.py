import pygame
import os
import recursos
from juego import iniciar_juego
from mostrarEstadisticas import mirarEstadisticas


pygame.init()

screen = pygame.display.set_mode((recursos.anchura, recursos.altura))
pygame.display.set_caption(recursos.nombre_ventana)

clock = pygame.time.Clock()

estadisticas = open("estadisticas.txt", "r")
ganadas = estadisticas.readline().strip()
perdidas = estadisticas.readline().strip()

estadisticas.close()

inicio_tiempo = 0
ganar = False
active = True
texto = ["Jugar"]
listoParaJugar = True
color_texto = [0, 0, 0]
color_boton = [200, 200, 200]
elegir_nivel = False

boton_estadisticas = recursos.Boton("Estadisticas",(recursos.anchura//2, 270), (200, 200, 200), (230, 230, 230), (0, 0, 0) )
boton_salir = recursos.Boton("Salir",(recursos.anchura//2, 340), (200, 200, 200), (230, 230, 230), (0, 0, 0) )
boton_menu = recursos.Boton("Jugar",(recursos.anchura//2, 200), (200, 200, 200), (230, 230, 230), (0, 0, 0) )
boton_facil = recursos.Boton("Facil", (recursos.anchura//2, 200), (200, 200, 200), (230, 230, 230), (0, 0, 0) )
boton_medio = recursos.Boton("Medio", (recursos.anchura//2, 275), (200, 200, 200), (230, 230, 230), (0, 0, 0) )
boton_dificil = recursos.Boton("Dificil", (recursos.anchura//2, 350), (200, 200, 200), (230, 230, 230), (0, 0, 0) )

while active:

    screen.blit(recursos.fondo, (0, 0))


    for i, linea in enumerate(texto):
        texto_menu = recursos.font_grande.render(linea, True, (color_texto[0], color_texto[1], color_texto[2]))
        rectTexto = texto_menu.get_rect(center=(recursos.anchura//2, 200 + i * 40 ))
        screen.blit(texto_menu, rectTexto)

    if listoParaJugar and not elegir_nivel:
        boton_estadisticas.dibujar(screen)
        boton_menu.dibujar(screen)
        boton_salir.dibujar(screen)

    if elegir_nivel == True:
        boton_facil.dibujar(screen)
        boton_medio.dibujar(screen)
        boton_dificil.dibujar(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT or boton_salir.click():
            active = False

        if boton_estadisticas.click() and not elegir_nivel:
            valor = mirarEstadisticas(ganadas, perdidas)
            if valor is None:
                active = False


        if boton_menu.click() and listoParaJugar and not elegir_nivel:
            elegir_nivel = True
            inicio_tiempo = pygame.time.get_ticks()

        if boton_facil.click() and elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 500:
            listoParaJugar = False
            ganar = iniciar_juego(7) #Iniciamos el juego que se situa en otro codigo
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]
                ganadas = int(ganadas) + 1

            else:
                texto = ["Te has quedado sin intentos,", "has perdido"]
                color_texto = [255, 0, 0]
                perdidas = int(perdidas) + 1
            inicio_tiempo = pygame.time.get_ticks()

        if boton_medio.click() and elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 500:
            listoParaJugar = False
            ganar = iniciar_juego(5)
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]
                ganadas = int(ganadas) + 1

            else:
                texto = ["Te has quedado sin intentos,", "has perdido"]
                color_texto = [255, 0, 0]
                perdidas = int(perdidas) + 1
            inicio_tiempo = pygame.time.get_ticks()


        if boton_dificil.click() and elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 500:
            listoParaJugar = False
            ganar = iniciar_juego(3)
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]
                ganadas = int(ganadas) + 1

            else:
                texto = ["Te has quedado sin intentos,", "has perdido"]
                color_texto = [255, 0, 0]
                perdidas = int(perdidas) + 1
            inicio_tiempo = pygame.time.get_ticks()



    if pygame.time.get_ticks() - inicio_tiempo > 3000:
        texto = ["Jugar"]
        listoParaJugar = True

    pygame.display.flip()
    clock.tick(60)

with open("estadisticas.txt", "w") as estadisticas:
    estadisticas.write(str(ganadas) + "\n")
    estadisticas.write(str(perdidas))

pygame.quit()