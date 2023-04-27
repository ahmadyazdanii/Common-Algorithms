from random import sample, seed
import timeit
import math
import tracemalloc
import humanize
from algorithms.sort.merge_sort import mergeSort
from algorithms.sort.quick_sort import quickSort
from algorithms.search.binary_search import binarySearch

seed(100)

def estimateBigO(func, input_sizes, type):
    times = []
    for size in input_sizes:
        if type == "search":
            input_data = list(range(1, size))
            time = timeit.timeit(lambda: func(input_data, size - 5), number=100) / 100
        else:
            input_data = sample(range(1, input_sizes[-1] + 1), size)
            time = timeit.timeit(lambda: func(input_data), number=100) / 100 
        times.append((size, time))

    # Calculate the slopes of the log-log plot of the times vs. the input sizes
    slopes = []
    for i in range(1, len(times)):
        x1, y1 = math.log(times[i-1][0]), math.log(times[i-1][1])
        x2, y2 = math.log(times[i][0]), math.log(times[i][1])
        slope = (y2 - y1) / (x2 - x1)
        slopes.append(slope)

    # Determine the average slope
    avg_slope = sum(slopes) / len(slopes)

    # Estimate the big-O time complexity based on the average slope
    if avg_slope < 0.1:
        big_O = "O(1)"
    elif avg_slope < 0.475:
        big_O = "O(log n)"
    elif avg_slope < 0.75:
        big_O = "O(n)"
    elif avg_slope < 1.5:
        big_O = "O(n log n)"
    else:
        big_O = "O(n^2) or worse"

    return big_O, round(avg_slope, 4)


def estimateComplexity(*algorithms):
    input_sizes = [10, 100, 1000, 10000]

    for algorithm in algorithms:
        algo_name = algorithm["func"].__name__
        tracemalloc.start()
        
        big_o_estimate, avg_slope = estimateBigO(
            algorithm["func"], input_sizes, algorithm["type"])

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')

        print(f"---- Algorithm {algo_name} ----")
        print("Estimated big-O time complexity:", big_o_estimate)
        print("Average slope:", avg_slope)

        max_memory_allocated = 0
        for stat in top_stats:
            if algorithm["type"] in str(stat.traceback):
                max_memory_allocated = stat.size
                break

        print(
            f"Max Memory allocated: {humanize.naturalsize(max_memory_allocated)}\n")


if __name__ == "__main__":
    estimateComplexity({"func": quickSort, "type": "sort"},
                     {"func": mergeSort, "type": "sort"},
                     {"func": binarySearch, "type": "search"})
