import numpy as np
import pandas as pd
import os


def generate_and_store_datasets():
    # Create a directory to store the datasets
    output_dir = "datasets"
    os.makedirs(output_dir, exist_ok=True)

    # Generate datasets
    for i, size in enumerate(range(1_000_000, 6_000_000, 1_000_000), start=1):
        dataset = np.random.choice(range(0, 10_000_000), size=size, replace=False)  # Generate unique random integers in the range [0, 10,000,000)
        df = pd.DataFrame(dataset, columns=["random_numbers"])
        file_path = os.path.join(output_dir, f"dataset_{i}M.csv")
        df.to_csv(file_path, index=False)
        print(f"Dataset {i} with {size} records saved to {file_path}")


if __name__ == "__main__":
    generate_and_store_datasets()
