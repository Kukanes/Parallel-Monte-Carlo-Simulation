# Parallel Monte Carlo Simulation Using Python Multiprocessing

## Project Description

This project implements a Monte Carlo simulation to estimate the mathematical constant Pi (π). The project compares sequential execution with parallel execution using Python multiprocessing.

The same workload of 10,000,000 random points is used for the experiments. The parallel implementation distributes the workload among multiple processes.

## Technologies Used

- Python 3.14.7
- Python Multiprocessing
- Random Number Generation
- Matplotlib
- CSV

## Project Files

- `main.py` - Runs the complete project workflow.
- `sequential.py` - Performs the Monte Carlo simulation sequentially.
- `parallel.py` - Performs the Monte Carlo simulation using multiple processes.
- `benchmark.py` - Compares sequential and parallel performance.
- `graphs.py` - Generates performance graphs.
- `results.csv` - Stores the benchmark results.
- `execution_time.png` - Execution time graph.
- `speedup.png` - Speedup graph.
- `efficiency.png` - Efficiency graph.

## How to Run

Run the complete project using:

    python main.py

The program performs the benchmark and generates the performance graphs.

Individual programs can also be executed using:

    python sequential.py

    python parallel.py

    python benchmark.py

    python graphs.py

## Performance Metrics

The project evaluates:

- Execution Time
- Speedup
- Efficiency
- Estimated Pi

Three parallel configurations are tested:

- 2 processes
- 4 processes
- 8 processes

Each configuration is tested five times and the average results are recorded.

## Results

The benchmark results are saved in `results.csv`.

The generated graphs show:

1. Execution Time vs Number of Processes
2. Speedup vs Number of Processes
3. Efficiency vs Number of Processes