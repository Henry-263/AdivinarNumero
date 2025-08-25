import pygame
import recursos
from recursos import Boton


def mirarEstadisticas(ganadas, perdidas):
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((recursos.anchura, recursos.altura))
    pygame.display.set_caption(recursos.nombre_ventana)

    porcentaje = int(ganadas) / (int(ganadas) + int(perdidas)) * 100
    porcentaje = round(porcentaje, 2)
    run = True
    texto = ("Ganadas: " + str(ganadas), "Perdidas: " + str(perdidas), "Porcentaje de victorias: " + str(porcentaje) + "%")


    boton_volver = Boton("Volver",(recursos.anchura//2, 350), (200, 200, 200), (230, 230, 230), (0, 0, 0) )

    while run:
        screen.blit(recursos.fondo, (0, 0))

        for i, linea in enumerate(texto):
            texto_menu = recursos.font_grande.render(linea, True, (0, 0, 0))
            rectTexto = texto_menu.get_rect(center=(recursos.anchura // 2, 200 + i * 40))
            screen.blit(texto_menu, rectTexto)

        boton_volver.dibujar(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return None

            if boton_volver.click():
                run = False
                return 1

        pygame.display.flip()
        clock.tick(60)