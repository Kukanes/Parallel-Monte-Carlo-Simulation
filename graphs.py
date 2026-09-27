import csv
import matplotlib.pyplot as plt


processes = []
execution_times = []
speedups = []
efficiencies = []

with open("results.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        processes.append(int(row["Processes"]))
        execution_times.append(float(row["Average Time"]))
        speedups.append(float(row["Speedup"]))
        efficiencies.append(float(row["Efficiency"]))


# Execution Time Graph

plt.figure()

plt.plot(processes, execution_times, marker="o")

plt.xlabel("Number of Processes")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Execution Time vs Number of Processes")

plt.xticks(processes)
plt.grid(True)

plt.savefig("execution_time.png", dpi=300, bbox_inches="tight")

plt.show()


# Speedup Graph

plt.figure()

plt.plot(processes, speedups, marker="o")

plt.xlabel("Number of Processes")
plt.ylabel("Speedup")
plt.title("Speedup vs Number of Processes")

plt.xticks(processes)
plt.grid(True)

plt.savefig("speedup.png", dpi=300, bbox_inches="tight")

plt.show()


# Efficiency Graph

plt.figure()

plt.plot(processes, efficiencies, marker="o")

plt.xlabel("Number of Processes")
plt.ylabel("Efficiency")
plt.title("Efficiency vs Number of Processes")

plt.xticks(processes)
plt.grid(True)

plt.savefig("efficiency.png", dpi=300, bbox_inches="tight")

plt.show()