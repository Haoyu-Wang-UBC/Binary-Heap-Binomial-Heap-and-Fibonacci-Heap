# Binary-Heap-Binomial-Heap-and-Fibonacci-Heap
This is a repo for COSC 520 Assignment 2
# Overview
This repository compare the time and space complexity of benchmark operations of three heaps.
1. Binary Heap.
2. Binomial Heap.
3. Fibonacci Heap.

The theoretical time and space complexity of these heaps are shown as follow.

| Operation          | Binary Heap        | Binomial Heap       | Fibonacci Heap     |
|--------------------|-------------------|---------------------|--------------------|
| Insert (worst case) | $O(\log n)$       | $O(\log n)$        | $O(1)$            |
| Delete Min        | $O(\log n)$        | $O(\log n)$        | $O(\log n)$       |
| Build Heap        | $O(n \log n)$      | $O(n \log n)$      | $O(n)$            |
| Space Complexity  | $O(n)$             | $O(n)$             | $O(n)$            |

Here, `n` is the number of elements in the heap.

# How to use
## Step 1
Run `data_generate.py` to generate datasets containing different numbers of positive integers.
Or download the dataset from https://drive.google.com/drive/folders/1-8q1dNP_ppQM8yCCku2elAQZBU9RNaQr?usp=drive_link.
## Step 2
Run `main.py` to test the run time of insertions and deleting minimums, and record the build time.
You can change the `DATA_PATH` in the `main.py` to choose different data sets to build heaps.
If you want to edit these three heaps' function, you can edit `binary_heap.py`, `binomial_heap.py`, and `fibonacci_heap.py`.
## Step 3
After getting all the run time data, fill these data into `plot.py` and run to get the figure.

# Results
Here are the results of our experiments.

