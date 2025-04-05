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
        distance += np.linalg.norm(np.array(a[:2]) - np.array(b[:2]))
    return distance

def get_neighbor(tour):
    a, b = np.random.choice(len(tour), 2, replace=False)
    neighbor = tour[:]
    neighbor[a], neighbor[b] = neighbor[b], neighbor[a]
    return neighbor

def simulated_annealing(node_list, t_start=100, t_end=1e-3, alpha=0.995, max_iter=10000, epsilon=1e-6):
    current = list(range(len(node_list)))
    np.random.shuffle(current)
    current_distance = total_distance(current, node_list)
    best = current[:]
    best_distance = current_distance

    t = t_start
    iteration = 0
    history = [current[:]]

    start_time = time.time()

    while t > t_end and iteration < max_iter:
        neighbor = get_neighbor(current)
        neighbor_distance = total_distance(neighbor, node_list)

        delta_e = neighbor_distance - current_distance

        if abs(delta_e) < epsilon or delta_e < 0 or np.random.rand() < np.exp(-delta_e / t):
            current = neighbor
            current_distance = neighbor_distance
            history.append(current[:])

            if current_distance < best_distance:
                best = current[:]
                best_distance = current_distance

        t *= alpha
        iteration += 1

    total_time = time.time() - start_time
    print(f"SA Finished in {total_time:.2f}s | Iterations: {iteration} | Best Distance: {best_distance:.2f}")
    return best, best_distance, total_time, history

def animate_tour(node_list, tour_history, filename="simulated_annealing_tsp.gif"):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        tour = tour_history[frame]
        coords = node_list[tour + [tour[0]], :2]

        color = 'blue'
        linewidth = 1.5
        if frame == len(tour_history) - 1:
            color = 'red'
            linewidth = 2.5

        ax.plot(coords[:, 0], coords[:, 1], marker='o', linestyle='-', color=color, linewidth=linewidth)
        for idx, (x, y) in enumerate(node_list[:, :2]):
            ax.text(x, y, str(idx), fontsize=9, ha='right', va='bottom')
        ax.set_title(f"Step {frame + 1}/{len(tour_history)}")

    ani = FuncAnimation(fig, update, frames=len(tour_history), interval=100)

    if len(tour_history) > 0:
        ani.save(filename, writer="pillow")
        print(f"GIF saved as {filename}")
    else:
        print("No valid frames to animate.")

    plt.show()

# if __name__ == "__main__":
#     env = VRPEnv(num_nodes=15, batch_size=1, num_draw=1)
#     graph = env.reset()
#     node_list = np.array(graph[0])

#     best_tour, best_dist, time_taken, history = simulated_annealing(
#         node_list,
#         t_start=100,
#         t_end=1e-3,
#         alpha=0.995,
#         max_iter=10000,
#         epsilon=1e-6
#     )

#     animate_tour(node_list, history, filename="simulated_annealing_tsp.gif")
