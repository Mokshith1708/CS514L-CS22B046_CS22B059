import time
import numpy as np
import matplotlib.pyplot as plt
from gym_vrp.envs import VRPEnv
from SA import simulated_annealing, animate_tour  

def run_sa_multiple_times(runs=5, tau=600):
    times = []
    distances = []

    best_overall_distance = float('inf')
    best_history = None
    best_node_list = None

    env = VRPEnv(num_nodes=15, batch_size=1, num_draw=1)
    graph = env.reset()
    node_list = np.array(graph[0])

    for i in range(runs):
        print(f"\nRun {i+1}/{runs}")
        start_time = time.time()

        best_tour, best_dist, time_taken, history = simulated_annealing(
            node_list,
            t_start=100,
            t_end=1e-3,
            alpha=0.995,
            max_iter=10000,
            epsilon=1e-6
        )

        if time_taken > tau:
            print(f"Terminated: Run {i+1} exceeded time limit τ = {tau} seconds")
            continue

        print(f"Completed: Distance = {best_dist:.2f}, Time = {time_taken:.2f}s")
        times.append(time_taken)
        distances.append(best_dist)

        if best_dist < best_overall_distance:
            best_overall_distance = best_dist
            best_history = history
            best_node_list = node_list.copy()

    if times:
        avg_time = np.mean(times)
        avg_dist = np.mean(distances)
        print(f"\nAverage Time: {avg_time:.2f}s")
        print(f"Average Distance: {avg_dist:.2f}")

        plt.figure(figsize=(8, 5))
        plt.plot(range(1, len(times)+1), times, marker='o', label='Time per Run (s)')
        plt.axhline(avg_time, color='red', linestyle='--', label=f'Avg Time: {avg_time:.2f}s')
        plt.xlabel("Run")
        plt.ylabel("Time Taken (s)")
        plt.title("Simulated Annealing – Time Taken per Run")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("sa_average_time_plot.png")
        print("Plot saved as 'sa_average_time_plot.png'")
        plt.show()

        # Animate best tour
        if best_history is not None:
            animate_tour(best_node_list, best_history, filename="simulated_annealing_tsp.gif")
    else:
        print("No successful runs under the time limit τ.")

if __name__ == "__main__":
    run_sa_multiple_times(runs=5, tau=600)
