import pygame
import os
import recursos
from juego import iniciar_juego
from mostrarEstadisticas import mirarEstadisticas


pygame.init()

screen = pygame.display.set_mode((recursos.anchura, recursos.altura))
pygame.display.set_caption(recursos.nombre_ventana)

clock = pygame.time.Clock()

if not os.path.exists("estadisticas.txt"):
    with open("estadisticas.txt", "w") as f:
        f.write("0\n0")

with open("estadisticas.txt", "r") as estadisticas:
    ganadas = estadisticas.readline().strip()
    perdidas = estadisticas.readline().strip()

inicio_tiempo = 0
ganar = False
active = True
texto = [""]
listoParaJugar = True
color_texto = [0, 0, 0]
color_boton = [200, 200, 200]
elegir_nivel = False
num = 0

boton_estadisticas = recursos.Boton("Estadisticas",(recursos.anchura//2, recursos.altura/2.2), (173, 216, 230), (230, 230, 230), (0, 0, 0) )
boton_salir = recursos.Boton("Salir",(recursos.anchura//2, recursos.altura/1.76), (173, 216, 230), (230, 230, 230), (0, 0, 0) )
boton_menu = recursos.Boton("Jugar",(recursos.anchura//2, recursos.altura/3), (173, 216, 230), (230, 230, 230), (0, 0, 0) )
boton_facil = recursos.Boton("Facil", (recursos.anchura//2, recursos.altura/3), (173, 216, 230), (230, 230, 230), (0, 0, 0) )
boton_medio = recursos.Boton("Medio", (recursos.anchura//2, recursos.altura/2.18), (173, 216, 230), (230, 230, 230), (0, 0, 0) )
boton_dificil = recursos.Boton("Dificil", (recursos.anchura//2, recursos.altura/1.71), (173, 216, 230), (230, 230, 230), (0, 0, 0) )
boton_volver = recursos.Boton("Volver", (recursos.anchura//2, recursos.altura/1.41), (173, 216, 230), (230, 230, 230), (0, 0, 0))

while active:

    screen.blit(recursos.fondo, (0, 0))


    for i, linea in enumerate(texto):
        texto_menu = recursos.font_grande.render(linea, True, (color_texto[0], color_texto[1], color_texto[2]))
        rectTexto = texto_menu.get_rect(center=(recursos.anchura//2, recursos.altura/3 + i * (recursos.altura/15) ))
        screen.blit(texto_menu, rectTexto)

    if listoParaJugar and not elegir_nivel:
        boton_estadisticas.dibujar(screen)
        boton_menu.dibujar(screen)
        boton_salir.dibujar(screen)

    if elegir_nivel == True:
        boton_volver.dibujar(screen)
        boton_facil.dibujar(screen)
        boton_medio.dibujar(screen)
        boton_dificil.dibujar(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            active = False

        if boton_salir.click() and not elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 100:
            recursos.mouse_sound.play()
            pygame.time.delay(200)
            active = False

        if boton_estadisticas.click() and not elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 100:
            recursos.mouse_sound.play()
            valor = mirarEstadisticas(ganadas, perdidas)
            pygame.event.clear()
            inicio_tiempo = pygame.time.get_ticks()
            if valor is None:
                active = False


        if boton_menu.click() and listoParaJugar and not elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 100:
            recursos.mouse_sound.play()
            elegir_nivel = True
            inicio_tiempo = pygame.time.get_ticks()

        if boton_volver.click() and elegir_nivel:
            recursos.mouse_sound.play()
            elegir_nivel = False
            listoParaJugar = True
            pygame.time.delay(100)

        if boton_facil.click() and elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 100:
            recursos.mouse_sound.play()
            listoParaJugar = False
            ganar, num = iniciar_juego(7) #Iniciamos el juego que se situa en otro codigo
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]
                ganadas = int(ganadas) + 1

            else:
                texto = ["Te has quedado sin intentos,", "has perdido", "El numero era: " + str(num)]
                color_texto = [255, 0, 0]
                perdidas = int(perdidas) + 1
            inicio_tiempo = pygame.time.get_ticks()

        if boton_medio.click() and elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 100:
            recursos.mouse_sound.play()
            listoParaJugar = False
            ganar, num = iniciar_juego(5)
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]
                ganadas = int(ganadas) + 1

            else:
                texto = ["Te has quedado sin intentos,", "has perdido", "El numero era: " + str(num)]
                color_texto = [255, 0, 0]
                perdidas = int(perdidas) + 1
            inicio_tiempo = pygame.time.get_ticks()


        if boton_dificil.click() and elegir_nivel and pygame.time.get_ticks() - inicio_tiempo > 100:
            recursos.mouse_sound.play()
            listoParaJugar = False
            ganar, num = iniciar_juego(3)
            elegir_nivel = False
            if ganar is None:
                active = False
            elif ganar:
                texto = ["Felicidades has ganado"]
                color_texto = [0, 143, 57]
                ganadas = int(ganadas) + 1

            else:
                texto = ["Te has quedado sin intentos,", "has perdido", "El numero era: " + str(num)]
                color_texto = [255, 0, 0]
                perdidas = int(perdidas) + 1
            inicio_tiempo = pygame.time.get_ticks()



    if pygame.time.get_ticks() - inicio_tiempo > 3000:
        texto = [""]
        listoParaJugar = True

    pygame.display.flip()
    clock.tick(60)

with open("estadisticas.txt", "w") as estadisticas:
    estadisticas.write(str(ganadas) + "\n")
    estadisticas.write(str(perdidas))

pygame.quit()