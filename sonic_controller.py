import time
import pygame
import stable_retro as retro
import numpy as np


# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre (image originale : 320 x 224)
SCALE = 3
WIDTH = 320 * SCALE
GAME_HEIGHT = 224 * SCALE
INFO_HEIGHT = 40
HEIGHT = GAME_HEIGHT + INFO_HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonic 2 - Contrôle manuel / IA")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Initialisation de Sonic
env = retro.make(
    game="SonicTheHedgehog2-Genesis-v0",
    render_mode=None
)

observation, info = env.reset()

# Modes de contrôle
mode = "MANUEL"
running = True

# Indices des boutons dans Stable-Retro
LEFT = 6
RIGHT = 7
UP = 4
DOWN = 5
JUMP = 1
START = 3


def get_manual_action():
    """Construit l'action à partir des touches actuellement pressées."""

    keys = pygame.key.get_pressed()
    action = [0] * 12

    # Déplacements : flèches ou ZQSD
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        action[LEFT] = 1

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        action[RIGHT] = 1

    if keys[pygame.K_UP] or keys[pygame.K_z]:
        action[UP] = 1

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        action[DOWN] = 1

    # Saut
    if keys[pygame.K_SPACE]:
        action[JUMP] = 1

    # Démarrer
    if keys[pygame.K_RETURN]:
        action[START] = 1

    return action


def render_game(observation):

    image = pygame.surfarray.make_surface(
        np.transpose(observation, (1, 0, 2))
    )

    image = pygame.transform.scale(
        image, (WIDTH, GAME_HEIGHT)
    )

    screen.fill((0, 0, 0))
    screen.blit(image, (0, INFO_HEIGHT))

    text = font.render(
        f"Mode : {mode} | TAB : changer de mode | ESC : quitter",
        True,
        (255, 255, 255)
    )

    screen.blit(text, (10, 5))
    pygame.display.flip()


try:
    while running:

        # Gestion des événements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_TAB:
                    if mode == "MANUEL":
                        mode = "IA"
                    else:
                        mode = "MANUEL"

        if not running:
            break

        # Choix de l'action selon le mode
        if mode == "MANUEL":
            action = get_manual_action()

        else:
            # En attendant l'entraînement de l'IA,
            # Sonic reste immobile dans ce mode.
            action = [0] * 12

        # Exécution d'une action dans le jeu
        observation, reward, terminated, truncated, info = env.step(action)

        # Réinitialisation si la partie est terminée
        if terminated or truncated:
            observation, info = env.reset()

        # Affichage
        render_game(observation)

        # Limitation à environ 60 images par seconde
        clock.tick(60)

finally:
    env.close()
    pygame.quit()