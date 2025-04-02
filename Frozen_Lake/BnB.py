import gymnasium as gym

env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True)
state,info = env.reset()

print(state,info)
new_state, reward, done, truncated, info = env.step(2)

print("New State:", new_state)
print("Reward:", reward)
print("Game Over?", done)
print("Info:", info)