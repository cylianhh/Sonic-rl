import stable_retro as retro
import time

env = retro.make(
    game="SonicTheHedgehog2-Genesis-v0",
    render_mode="human"
)

observation, info = env.reset()

def execute_action(env, action, frames):
    for _ in range(frames):
        observation, reward, terminated, truncated, info = env.step(action)
        time.sleep(1 / 60)

        if terminated or truncated:
            break

# Avancer
# action = [0] * 12
# action[7] = 1
# execute_action(env, action, 120)

# Avancer et sauter
# action = [0] * 12
# action[7] = 1
# action[1] = 1
# execute_action(env, action, 120)

# Sauter sur place
action = [0] * 12
action[1] = 1
execute_action(env, action, 120)

env.close()