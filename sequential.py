import random
import time

def monte_carlo(points):
    inside = 0

    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y <= 1:
            inside += 1

    pi = 4 * inside / points
    return pi


points = 10_000_000

start_time = time.perf_counter()

pi = monte_carlo(points)

end_time = time.perf_counter()

execution_time = end_time - start_time

print("Sequential Monte Carlo Simulation")
print("---------------------------------")
print(f"Number of points: {points:,}")
print(f"Estimated Pi: {pi}")
print(f"Execution Time: {execution_time:.4f} seconds")