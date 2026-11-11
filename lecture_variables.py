import stable_retro as retro
import time

env = retro.make(
    game="SonicTheHedgehog2-Genesis-v0",
    render_mode="human"
)

observation, info = env.reset()

for i in range(300):

    # Sonic avance vers la droite
    action = [0] * 12
    action[7] = 1

    observation, reward, terminated, truncated, info = env.step(action)

    # Lire les variables internes
    # x = env.get_ram()[0]  # À remplacer : on utilisera env.data

    if i % 30 == 0:
        print("Position :", env.data.lookup_value("x"))
        print("Position Y :", env.data.lookup_value("y"))
        print("Caméra X :", env.data.lookup_value("screen_x"))
        print("Anneaux :", env.data.lookup_value("rings"))
        print("Score :", env.data.lookup_value("score"))
        print("----------------------")

    time.sleep(1 / 60)

    if terminated or truncated:
        break

env.close()