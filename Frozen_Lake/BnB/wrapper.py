import time
import matplotlib.pyplot as plt
from BnB import branch_and_bound  # Ensure BnB is correctly imported from your main file

def run_bnb_with_timing(runs=5, timeout=600):  # τ = 10 min (600 sec)
    times = []
    for i in range(runs):
        start_time = time.time()
        branch_and_bound()
        end_time = time.time()
        elapsed = end_time - start_time
        times.append(elapsed)
        print(f"Run {i+1}: {elapsed:.2f} seconds")
        if sum(times) > timeout:
            print("Timeout reached! Stopping further runs.")
            break
    
    plt.plot(range(1, len(times) + 1), times, marker='o', linestyle='-', color='b')
    plt.xlabel("Run Number")
    plt.ylabel("Time Taken (seconds)")
    plt.title("BnB Execution Time per Run")
    plt.savefig("BnB_execution_time.png")
    plt.show()

run_bnb_with_timing()
