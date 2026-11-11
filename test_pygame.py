import pygame

pygame.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Test clavier Sonic")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            print("Touche pressée :", pygame.key.name(event.key))

            if event.key in (pygame.K_UP, pygame.K_z):
                print("HAUT")
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                print("BAS")
            elif event.key in (pygame.K_LEFT, pygame.K_q):
                print("GAUCHE")
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                print("DROITE")
            elif event.key == pygame.K_SPACE:
                print("SAUT")

pygame.quit()