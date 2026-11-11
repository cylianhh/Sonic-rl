import stable_retro as retro
import time

env = retro.make(
    game="SonicTheHedgehog2-Genesis-v0",
    render_mode="human"
)

observation, info = env.reset()

print("Sonic 2 est lancé !")
print("Dimensions de l'image :", observation.shape)
print("Actions disponibles :", env.action_space)

for i in range(300):
    # Aucune touche pressée
    action = [0] * 12

    observation, reward, terminated, truncated, info = env.step(action)

    # Attendre 1/60 de seconde
    time.sleep(1 / 60)

    if terminated or truncated:
        observation, info = env.reset()

env.close()