import random
import time
import multiprocessing
import csv


def monte_carlo(points):
    inside = 0

    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y <= 1:
            inside += 1

    return inside


def run_sequential(points):

    start_time = time.perf_counter()

    inside = monte_carlo(points)

    pi = 4 * inside / points

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return pi, execution_time


def run_parallel(points, processes):

    points_per_process = points // processes

    start_time = time.perf_counter()

    with multiprocessing.Pool(processes) as pool:
        results = pool.map(
            monte_carlo,
            [points_per_process] * processes
        )

    total_inside = sum(results)

    pi = 4 * total_inside / points

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return pi, execution_time


if __name__ == "__main__":

    points = 10_000_000
    process_counts = [2, 4, 8]
    repetitions = 5

    results = []

    print("Monte Carlo Performance Test")
    print("----------------------------")
    print(f"Number of points: {points:,}")
    print(f"Repetitions per configuration: {repetitions}")
    print()

    # Sequential test

    sequential_times = []
    sequential_pi_values = []

    print("SEQUENTIAL")

    for run in range(repetitions):

        pi, execution_time = run_sequential(points)

        sequential_times.append(execution_time)
        sequential_pi_values.append(pi)

        print(
            f"Run {run + 1}: "
            f"{execution_time:.4f} seconds | "
            f"Pi: {pi}"
        )

    average_sequential_time = sum(sequential_times) / repetitions
    average_sequential_pi = sum(sequential_pi_values) / repetitions

    print(f"Average Time: {average_sequential_time:.4f} seconds")
    print(f"Average Pi: {average_sequential_pi}")
    print("--------------------------------")
    print()

    results.append([
        "Sequential",
        1,
        average_sequential_time,
        average_sequential_pi,
        1.0,
        1.0
    ])

    # Parallel tests

    for processes in process_counts:

        times = []
        pi_values = []

        print(f"PARALLEL - {processes} PROCESSES")

        for run in range(repetitions):

            pi, execution_time = run_parallel(
                points,
                processes
            )

            times.append(execution_time)
            pi_values.append(pi)

            print(
                f"Run {run + 1}: "
                f"{execution_time:.4f} seconds | "
                f"Pi: {pi}"
            )

        average_time = sum(times) / repetitions
        average_pi = sum(pi_values) / repetitions

        speedup = average_sequential_time / average_time

        efficiency = speedup / processes

        print(f"Average Time: {average_time:.4f} seconds")
        print(f"Average Pi: {average_pi}")
        print(f"Speedup: {speedup:.4f}x")
        print(f"Efficiency: {efficiency:.4f}")
        print("--------------------------------")
        print()

        results.append([
            "Parallel",
            processes,
            average_time,
            average_pi,
            speedup,
            efficiency
        ])

    # Save results to CSV

    with open("results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Type",
            "Processes",
            "Average Time",
            "Average Pi",
            "Speedup",
            "Efficiency"
        ])

        writer.writerows(results)

    print("Results saved to results.csv")