import pygame
from juego import iniciar_juego


pygame.init()

altura = 600
anchura = 800

screen = pygame.display.set_mode((anchura, altura))
pygame.display.set_caption("Menu")

font_normal = pygame.font.SysFont('Comic Sans MS', 20)
font_grande = pygame.font.SysFont('Comic Sans MS', 36)

clock = pygame.time.Clock()

inicio_tiempo = 0
ganar = False
active = True
texto = ["Dale enter para jugar"]
listoParaJugar = True
while active:

    screen.fill((30, 30, 30))

    for i, linea in enumerate(texto):
        texto_menu = font_grande.render(linea, True, (255, 255, 255))
        screen.blit(texto_menu, (200, 200 + i * 40))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and listoParaJugar:
                listoParaJugar = False
                ganar = iniciar_juego() #Iniciamos el juego que se situa en otro codigo
                if ganar:
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