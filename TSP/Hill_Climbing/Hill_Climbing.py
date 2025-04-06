import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from gym_vrp.envs import VRPEnv

def total_distance(tour, node_list):
    distance = 0
    for i in range(len(tour)):
        a = node_list[tour[i]]
        b = node_list[tour[(i + 1) % len(tour)]]
        distance += np.linalg.norm(np.array(a) - np.array(b))
    return distance

history = []

def hill_climbing_steepest(env, node_list, time_limit=5):
    start_time = time.time()
    current = list(range(env.num_nodes))
    np.random.shuffle(current)
    best_distance = total_distance(current, node_list)
    history.append(current[:])

    while time.time() - start_time < time_limit:
        best_neighbor = None
        best_neighbor_distance = best_distance

        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                neighbor = current[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbor_distance = total_distance(neighbor, node_list)

                if neighbor_distance < best_neighbor_distance:
                    best_neighbor = neighbor
                    best_neighbor_distance = neighbor_distance

        if best_neighbor is not None:
            current = best_neighbor
            best_distance = best_neighbor_distance
            history.append(current[:])
        else:
            break

    total_time = time.time() - start_time
    print(f"Finished in {total_time:.6f} seconds. Best Distance: {best_distance:.2f}")
    return current, best_distance, total_time



def animate_tour(node_list, tour_history):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        tour = tour_history[frame]
        coords = node_list[tour + [tour[0]]] 
        ax.plot(coords[:, 0], coords[:, 1], marker='o', linestyle='-', color='blue')
        for idx, coord in enumerate(node_list):
            x, y = coord[0], coord[1]
            ax.text(x, y, str(idx), fontsize=9, ha='right', va='bottom')
        ax.set_title(f"Step {frame + 1}/{len(tour_history)}")
        if frame == len(tour_history) - 1:
            ax.plot(coords[:, 0], coords[:, 1], marker='o', linestyle='-', color='red', linewidth=2)
    ani = FuncAnimation(fig, update, frames=len(tour_history), interval=500)
    if len(tour_history) > 0:
        ani.save("hill_climbing_tsp.gif", writer="pillow")
    else:
        print("No valid frames to animate.")
    plt.show()

# if __name__ == "__main__":
#     env = VRPEnv(num_nodes=10, batch_size=1, num_draw=1)
#     graph = env.reset()
#     node_list = np.array(graph[0])

#     tour, distance, duration = hill_climbing_once(env, node_list, time_limit=30)
#     animate_tour(node_list, history)
