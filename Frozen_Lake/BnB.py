import gymnasium as gym

env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False)
state,info = env.reset()
print(state,info)

GOAL = 15
ACTION_SPACE = [0,1,2,3]  # Left, Down, Right, Up 
ACTION_NAMES = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}
DEPTH = float('inf')

def BnB(state, cost, DEPTH):
    if state == GOAL:
        DEPTH = min(cost,DEPTH)
        return cost
    if cost > DEPTH:
        return None
    ans = float('inf')
    for action in ACTION_SPACE:
        next_state,_,_,_,_ = env.step(action)
        if cost+1 <= DEPTH:
         ans = min(ans,BnB(next_state,cost+1,DEPTH))
    return ans

ans = 1
while DEPTH > 0:
    ans = BnB(state, 0, DEPTH)
print(ans)

    
    
    