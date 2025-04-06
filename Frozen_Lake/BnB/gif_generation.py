import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import imageio

n = 8
env = gym.make('FrozenLake-v1', desc=generate_random_map(size=n), is_slippery=False, render_mode='rgb_array')

state, _ = env.reset()
GOAL = n * n - 1
ACTION_SPACE = [0, 1, 2, 3]
ACTION_NAMES = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}

best_depth = float('inf')
best_path = None
frames = []  # Store all frames for GIF

def heuristic(pos):
    x1, y1 = divmod(pos, n)
    x2, y2 = divmod(GOAL, n)
    return abs(x1 - x2) + abs(y1 - y2)

def branch_and_bound():
    global best_depth, best_path
    while True:
        state, _ = env.reset()
        stack = [(state, 0, [])]
        updated = False
        visited = set()

        while stack:
            curr_state, cost, path = stack.pop()
            env.unwrapped.s = curr_state
            visited.add(curr_state)

            # Capture current node being explored
            frames.append(env.render())

            if curr_state == GOAL:
                if cost < best_depth:
                    best_depth = cost
                    best_path = path[:]
                    updated = True
                continue

            if cost >= best_depth:
                continue

            for action in ACTION_SPACE:
                next_state, _, done, _, _ = env.step(action)

                # Set to next state temporarily for visualization
                env.unwrapped.s = next_state
                frames.append(env.render())  # Capture attempted move

                if done and next_state != GOAL:
                    # Restore before continuing
                    env.unwrapped.s = curr_state
                    continue

                if next_state not in visited:
                    if cost + 1 + heuristic(next_state) < best_depth:
                        stack.append((next_state, cost + 1, path + [action]))

                # Always restore state after action to avoid stepping confusion
                env.unwrapped.s = curr_state

        if not updated:
            print("Final Best Path:", [ACTION_NAMES[a] for a in best_path], "with Cost:", best_depth)
            break

branch_and_bound()

# Save the exploration as a GIF
imageio.mimsave('bnb_frozenlake_full_exploration.gif', frames, fps=2)
print("GIF saved as 'bnb_frozenlake_full_exploration.gif'")
