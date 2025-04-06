import numpy as np
import matplotlib.pyplot as plt
from gym_vrp.envs import VRPEnv
from Hill_Climbing import hill_climbing_steepest, history, animate_tour

def run_multiple_hill_climbing(num_runs=5, tau=600, num_nodes=10):
    run_times = []
    run_distances = []

    best_overall_distance = float('inf')
    best_history = None
    best_node_list = None

    env = VRPEnv(num_nodes=num_nodes, batch_size=1, num_draw=1)
    graph = env.reset()
    node_list = np.array(graph[0])

    print(f"\n--- Running Hill Climbing {num_runs} times with τ = {tau} seconds ---\n")

    for i in range(num_runs):
        print(f"Run {i + 1}/{num_runs}")
        history.clear()
        tour, dist, time_taken = hill_climbing_steepest(env, node_list, time_limit=tau)

        run_times.append(time_taken)
        run_distances.append(dist)

        if dist < best_overall_distance:
            best_overall_distance = dist
            best_history = history.copy()
            best_node_list = node_list.copy()

    avg_time = sum(run_times) / num_runs
    avg_dist = sum(run_distances) / num_runs

    print(f"\nAverage Time: {avg_time:.6f}s")
    print(f"Average Distance: {avg_dist:.6f}")
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(range(1, num_runs + 1), run_times, color='skyblue', edgecolor='black')

    for bar, time_val in zip(bars, run_times):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height + 0.01, f"{time_val:.6f}s", 
                 ha='center', va='bottom', fontsize=8, rotation=45)

    plt.axhline(y=tau, color='gray', linestyle='--', label=f'Time Limit (τ = {tau}s)')
    plt.xlabel("Run Number")
    plt.ylabel("Time Taken (s)")
    plt.title("Hill Climbing – Time Taken Per Run")
    plt.legend()
    plt.tight_layout()
    plt.savefig("hill_climbing_time_plot.png")
    print("Plot saved as 'hill_climbing_time_plot.png'")
    plt.show()


    if best_history is not None:
        animate_tour(best_node_list, best_history)

if __name__ == "__main__":
    run_multiple_hill_climbing(num_runs=5, tau=30, num_nodes=30)
