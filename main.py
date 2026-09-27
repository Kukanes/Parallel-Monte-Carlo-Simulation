import subprocess


print("========================================")
print("   PARALLEL MONTE CARLO SIMULATION")
print("========================================")

print("\nRunning performance benchmark...")
print("----------------------------------------")

subprocess.run(["python", "benchmark.py"])

print("\nBenchmark completed.")

print("\nGenerating performance graphs...")
print("----------------------------------------")

subprocess.run(["python", "graphs.py"])

print("\nAll tasks completed.")
print("Results saved to results.csv")
print("Graphs saved as PNG files.")