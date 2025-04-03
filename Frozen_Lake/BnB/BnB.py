import gymnasium as gym
import time
from gymnasium.envs.toy_text.frozen_lake import generate_random_map

n = 16
env = gym.make('FrozenLake-v1', desc=generate_random_map(size=n), is_slippery=False)

state, info = env.reset()
# print("Starting State:", state)

GOAL = n * n - 1
ACTION_SPACE = [0, 1, 2, 3]
ACTION_NAMES = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}

best_depth = float('inf')   
best_path = None


def heuristic(pos):
    x1,y1 = pos//4, pos%4
    x2,y2 = GOAL//4, GOAL%4
    return abs(x1-x2) + abs(y1-y2)

def branch_and_bound():
    # start = time.time()
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

                if done and next_state != GOAL:
                    env.unwrapped.s = curr_state
                    continue
                
                if next_state not in visited:
                    if cost + 1 + heuristic(next_state) < best_depth:
                        stack.append((next_state, cost + 1, path + [action]))

                env.unwrapped.s = curr_state

        if not updated:
            # end = time.time()
            # print("grgs",end - start)
            print("Final Best Path:", [ACTION_NAMES[a] for a in best_path], "with Cost:", best_depth)
            break

# branch_and_bound()

# if best_path:
#     print("Final Best Path:", [ACTION_NAMES[a] for a in best_path], "with Cost:", best_depth)
# else:
#     print("No Path Found!")
