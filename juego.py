import pygame
import random


def iniciar_juego():
    pygame.init()

    altura = 600
    anchura = 800

    screen = pygame.display.set_mode((anchura, altura))
    pygame.display.set_caption("Juego de adivinar un numero")

    font_normal = pygame.font.SysFont('Comic Sans MS', 20)
    font_grande = pygame.font.SysFont('Comic Sans MS', 36)

    clock = pygame.time.Clock()

    num = random.randint(1, 100)
    pregunta = "Adivina un numero del 1 al 100: "
    texto = ""
    num_intentos = 5
    run = True
    respuesta = []
    enter = False
    mostrarTexto = False
    inicio_tiempo = 0
    espera_entre_respuestas = 2000
    ganar = False

    while run:
        screen.fill((30, 30, 30))
        #Bucle donde miramos si ha habido algun evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN and enter == False and mostrarTexto == False:
                if event.key == pygame.K_RETURN:
                    enter = True
                elif event.key == pygame.K_BACKSPACE:
                    if texto != "":
                        texto = texto[:-1]
                elif event.unicode.isdigit():
                    texto += event.unicode  #Añadimos si solo es un numero




        if mostrarTexto and pygame.time.get_ticks()-inicio_tiempo < espera_entre_respuestas:
            for i, linea in enumerate(respuesta):
                respuesta_txt = font_grande.render(linea, True, (255, 255, 255))
                screen.blit(respuesta_txt, (200, 200+i*40))

        if pygame.time.get_ticks()-inicio_tiempo >= espera_entre_respuestas:
            mostrarTexto = False

        #Texto de pregunta
        pregunta_txt = font_normal.render(pregunta, True, (255, 255, 255))
        screen.blit(pregunta_txt, (250, 0))

        input_txt = font_normal.render(texto, True, (255, 255, 255))
        screen.blit(input_txt, (250, 30))

        if enter == True and texto != "":
            if int(texto) == num:
                mostrarTexto = True
                texto = ""
                respuesta = ["Has acertado el numero"]
                inicio_tiempo = pygame.time.get_ticks()
                num_intentos = 0
                ganar = True
            else:
                num_intentos -= 1
                if int(texto) > num:
                    respuesta = ["No has acertado el numero,",  "te has pasado", "Te quedan " + str(num_intentos) + " intentos"]
                else:
                    respuesta = ["No has acertado el numero,",  "te has quedado corto", "Te quedan " + str(num_intentos) + " intentos"]
                mostrarTexto = True
                texto = ""
                inicio_tiempo = pygame.time.get_ticks()


        if num_intentos > 0:
            enter = False

        if num_intentos == 0 and pygame.time.get_ticks()-inicio_tiempo >= espera_entre_respuestas:
            run = False
            return ganar

        pygame.display.flip()
        clock.tick(60)