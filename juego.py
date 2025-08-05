import pygame
import random
import recursos


def iniciar_juego():
    pygame.init()



    screen = pygame.display.set_mode((recursos.anchura, recursos.altura))
    pygame.display.set_caption(recursos.nombre_ventana)



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
        screen.blit(recursos.fondo, (0, 0))
        #Bucle donde miramos si ha habido algun evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return None


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
                respuesta_txt = recursos.font_grande.render(linea, True, (0, 0, 0))
                screen.blit(respuesta_txt, (recursos.anchura // 2 - respuesta_txt.get_width() // 2, 200+i*40))

        if pygame.time.get_ticks()-inicio_tiempo >= espera_entre_respuestas:
            mostrarTexto = False

        #Texto de pregunta
        pregunta_txt = recursos.font_normal.render(pregunta, True, (0, 0, 0))
        screen.blit(pregunta_txt, (recursos.anchura // 2 - pregunta_txt.get_width() // 2, 100))

        input_txt = recursos.font_normal.render(texto, True, (0, 0, 0))
        screen.blit(input_txt, (recursos.anchura // 2 - input_txt.get_width() // 2, 130))

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