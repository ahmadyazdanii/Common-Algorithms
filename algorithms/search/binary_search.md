# Binary Search Algorithm

Binary Search is a searching algorithm that works by repeatedly dividing the search interval in half. It begins by comparing the middle element of the array with the target value. If the middle element is equal to the target value, the search is successful. If the target value is less than the middle element, the search continues in the lower half of the array. If the target value is greater than the middle element, the search continues in the upper half of the array. The algorithm repeats this process until the target value is found or the search interval is empty.

Here are the main steps of the Binary Search algorithm:

1. Initialize variables to track the low and high indices of the search interval.
2. Compute the middle index of the search interval.
3. Compare the middle element with the target value.
4. If the middle element is equal to the target value, return its index.
5. If the target value is less than the middle element, update the high index to be one less than the middle index and repeat steps 2-4.
6. If the target value is greater than the middle element, update the low index to be one more than the middle index and repeat steps 2-4.
7. If the search interval is empty and the target value has not been found, return `None`.

## Time Complexity

The time complexity of Binary Search is O(log(n)), where n is the size of the input array. This is because the search interval is divided in half at each step, and the algorithm performs at most log(n) iterations.

## Memory Complexity

Binary Search has a memory complexity of O(1) because it only requires a few constant-sized variables to keep track of the search interval and the middle index. There is no need to create any additional data structures or allocate any memory during the search.

Overall, Binary Search is a fast and efficient searching algorithm that works well on sorted arrays. Its time complexity and memory complexity make it a popular choice for many applications, such as searching for a value in a database or finding a specific item in a sorted list.
