import stable_retro as retro

env = retro.make(game="SonicTheHedgehog2-Genesis-v0")

print("Variables disponibles :")
print(env.data.list_variables())

env.close()