# Common Algorithms
In the repository I have created, I grouped common algorithms that can be used in many use cases. In the following sections, I mention the documentation file of each algorithm. Additionally, I have created a script that can estimate the time and memory complexity of these algorithms or your algorithms.

## Sorting Algorithms
* [Merge Sort](./algorithms/sort/merge_sort.md)
* [Quick Sort](./algorithms/sort/quick_sort.md)

## Searching Algorithms
* [Binary Search](./algorithms/search/binary_search.md)

## Other
* [recursion technique](./algorithms/recursion.md)

## Estimate time and memory complexity
The `estimate_complexity` Python script estimates the time and memory complexities of different algorithms. It uses the `timeit` and `tracemalloc` libraries to measure the time and memory usage of the algorithms.

### Install requirements
```shell
python -m pip install -r requirements.txt
```
### Run
```shell
python estimate_complexity.py
```