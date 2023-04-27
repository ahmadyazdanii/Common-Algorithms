# MergeSort Algorithm

MergeSort is a popular sorting algorithm that follows the divide-and-conquer approach to sorting. It works by dividing the input array into two halves, sorting each half recursively using MergeSort, and then merging the two sorted halves to produce the final sorted array.

Here are the main steps of the MergeSort algorithm:

1. Divide the input array into two halves.
2. Recursively sort each half using MergeSort.
3. Merge the two sorted halves into a single sorted array.

## Time Complexity

The time complexity of MergeSort is O(nlog(n)) in all cases. This is because MergeSort always divides the array into two halves, and each division takes O(log(n)) time. The merging step takes O(n) time, as each element in the array must be compared and placed in the correct order.

## Memory Complexity

MergeSort has a memory complexity of O(n) due to the temporary arrays used in the merging step. During the merging step, a temporary array is created to store the sorted elements before they are placed back into the original array. This requires additional memory proportional to the size of the input array. In the worst case, when the recursion depth is at its maximum, there may be up to log(n) temporary arrays in memory.

Overall, MergeSort is a reliable and efficient sorting algorithm that performs well on both small and large input sizes. Its consistent time complexity and memory complexity make it a popular choice for many applications.
