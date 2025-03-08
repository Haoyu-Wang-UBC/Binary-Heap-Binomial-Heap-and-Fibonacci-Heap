import matplotlib.pyplot as plt

# Data placeholders: Fill in the correct values here
datasets = ["1M", "2M", "3M", "4M", "5M"]
heap_types = ["binary", "binomial", "fibonacci"]
operations = ["build", "insert", "delete min"]

# Example data structure (replace with actual values)
data = {
    "build": {
        "binary": [0.4102, 0.7999, 1.2285, 1.663, 2.0588],  # Fill in execution times for "build" operation with binary heap
        "binomial": [4.5271, 9.8568, 16.0711, 21.0547, 26.5345],  # Fill in execution times for "build" operation with binomial heap
        "fibonacci": [2.7428, 5.8066, 8.7498, 11.6188, 14.5112],  # Fill in execution times for "build" operation with fibonacci heap
    },
    "insert": {
        "binary": [0.2599, 0.2733, 0.2776, 0.2884, 0.3114],  # Fill in execution times for "insert" operation with binary heap
        "binomial": [0.2162, 0.2325, 0.2462, 0.2548, 0.276],  # Fill in execution times for "insert" operation with binomial heap
        "fibonacci": [0.1047, 0.1112, 0.1249, 0.127, 0.139],  # Fill in execution times for "insert" operation with fibonacci heap
    },
    "delete min": {
        "binary": [0.5898, 0.6047, 0.7577, 0.7253, 0.8008],  # Fill in execution times for "delete min" operation with binary heap
        "binomial": [1.3932, 1.4923, 1.6662, 1.6426, 1.846],  # Fill in execution times for "delete min" operation with binomial heap
        "fibonacci": [2.8642, 3.4084, 4.3186, 4.8126, 5.4126],  # Fill in execution times for "delete min" operation with fibonacci heap
    },
}

# Generate three separate plots
for op in operations:
    plt.figure(figsize=(8, 6))
    for heap in heap_types:
        plt.plot(datasets, data[op][heap], marker='o', label=heap)

    plt.title(f"Operation: {op}")
    plt.xlabel("Dataset Size (Million)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
