import stable_retro as retro

env = retro.make(game="SonicTheHedgehog2-Genesis-v0")

print("Action space :", env.action_space)
print("Boutons :", env.buttons)
print("Actions valides :", env.data.valid_actions())

env.close()