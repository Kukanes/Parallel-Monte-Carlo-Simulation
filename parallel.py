import random
import time
import multiprocessing


def monte_carlo(points):
    inside = 0

    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y <= 1:
            inside += 1

    return inside


if __name__ == "__main__":

    points = 10_000_000
    processes = 4

    points_per_process = points // processes

    start_time = time.perf_counter()

    with multiprocessing.Pool(processes) as pool:
        results = pool.map(monte_carlo, [points_per_process] * processes)

    total_inside = sum(results)

    pi = 4 * total_inside / points

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print("Parallel Monte Carlo Simulation")
    print("--------------------------------")
    print(f"Number of points: {points:,}")
    print(f"Number of processes: {processes}")
    print(f"Estimated Pi: {pi}")
    print(f"Execution Time: {execution_time:.4f} seconds")