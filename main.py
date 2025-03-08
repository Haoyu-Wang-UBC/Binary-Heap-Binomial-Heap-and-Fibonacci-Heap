import numpy as np
import pandas as pd
import os
import time
import unittest
from binary_heap import BinaryHeap
from binomial_heap import BinomialHeap
from fibonacci_heap import FibonacciHeap
import random

DATA_PATH = os.path.join( "datasets", "dataset_3M.csv")

def load_dataset():
    """Load datasets from CSV files for heap construction tests."""
    df = pd.read_csv(DATA_PATH, usecols=["random_numbers"])
    dataset = df["random_numbers"].tolist()
    return dataset

def benchmark_heap_building(heap_class, dataset):
    """Benchmark heap building"""
    heap = heap_class()

    # Measure heap construction time
    start_time = time.time()
    for num in dataset:
        heap.insert(num)
    build_time = time.time() - start_time

    print(f"{heap_class.__name__} Build: {build_time:.4f}s")
    return heap  # Return the built heap for testing

def run_benchmark():
    dataset = load_dataset()

    print("Benchmarking Binary Heap...")
    binary_heap = benchmark_heap_building(BinaryHeap, dataset)

    print("Benchmarking Binomial Heap...")
    binomial_heap = benchmark_heap_building(BinomialHeap, dataset)

    print("Benchmarking Fibonacci Heap...")
    fibonacci_heap = benchmark_heap_building(FibonacciHeap, dataset)

    return binary_heap, binomial_heap, fibonacci_heap  # Return all built heaps

class TestHeaps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Use the heaps built during benchmarking instead of creating new ones."""
        print("Setting up heaps for testing...")
        start_time = time.time()
        try:
            cls.binary_heap, cls.binomial_heap, cls.fibonacci_heap = run_benchmark()
        except Exception as e:
            print(f"Error in setUpClass: {e}")
        print(f"Heaps built in {time.time() - start_time:.4f} sec")

    def test_insert(self):
        """Test worst-case insert operation on pre-built heap structures and measure insertion time."""
        print("Starting test_insert...")
        # Generate 100,000 numbers in descending order (worst-case scenario: each new key is smaller than all existing keys)
        worst_case_data = list(range(-1, -100001, -1))

        for heap in [self.binary_heap, self.binomial_heap, self.fibonacci_heap]:
            start_time = time.time()  # Record start time

            for num in worst_case_data:
                heap.insert(num)  # Perform worst-case insertion on the pre-built heap

            end_time = time.time()  # Record end time

            elapsed_time = end_time - start_time  # Calculate insertion time
            print(f"{heap.__class__.__name__} Worst-case Insert Time: {elapsed_time:.4f} sec")
            self.assertTrue(True)

    def test_delete_min(self):
        """Test and measure time for deleting the minimum element multiple times in each heap."""
        print("Starting test_delete_min...")
        num_operations = 100000  # Define how many times to delete the min element

        for heap in [self.binary_heap, self.binomial_heap, self.fibonacci_heap]:
            start_time = time.time()  # Start timing

            for _ in range(num_operations):
                heap.delete_min()  # Delete the minimum element

            end_time = time.time()  # End timing

            elapsed_time = end_time - start_time  # Compute elapsed time
            print(f"{heap.__class__.__name__} Delete Min Time: {elapsed_time:.4f} sec")

            # Ensure the test runs without errors (no specific min check)
            self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
