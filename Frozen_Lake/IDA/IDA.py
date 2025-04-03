import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map

n = 16  # Grid size
env = gym.make('FrozenLake-v1', desc=generate_random_map(size=n), is_slippery=False)
state, info = env.reset()

GOAL = n * n - 1
ACTION_SPACE = [0, 1, 2, 3]
ACTION_NAMES = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}

def heuristic(pos):
    """Manhattan distance heuristic"""
    x1, y1 = pos // n, pos % n
    x2, y2 = GOAL // n, GOAL % n
    return abs(x1 - x2) + abs(y1 - y2)

def ida_star():
    
    def search(curr_state, cost, path, bound):
        env.unwrapped.s = curr_state
        
        
        if curr_state == GOAL:
            return True, path  

        min_threshold = float('inf')
        for action in ACTION_SPACE:
            next_state, _, done, _, _ = env.step(action)

            if done and next_state != GOAL:
                env.unwrapped.s = curr_state
                continue

            if next_state not in visited:
                if cost + 1 + heuristic(next_state) <= bound:
                    visited.add(next_state)
                    result, new_path = search(next_state, cost + 1, path + [action], bound)
                    visited.remove(next_state)
                    
                    if result is True:
                        return True, new_path  
                
                else: 
                 min_threshold = min(min_threshold, cost + 1 + heuristic(next_state))  

            env.unwrapped.s = curr_state  

        return min_threshold, None  


    global state
    bound = 0
    while True:
        visited = {state}
        # print(f'hi:',bound,flush=True)
        result, best_path = search(state, 0, [], bound)
        # print(bound,flush=True)
        if result is True:
            print("Final Best Path:", [ACTION_NAMES[a] for a in best_path], "with Cost:", len(best_path))
            return best_path

        if result == float('inf'):
            print("No Path Found!")
            return None 

        bound = result  

# ida_star()
