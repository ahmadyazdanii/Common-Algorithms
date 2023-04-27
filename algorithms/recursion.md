# Recursion

Recursion is a programming technique where a function calls itself to solve a problem. In other words, it's a process where a function solves a problem by reducing it into smaller sub-problems until it reaches the base case (the problem size becomes small enough to be solved directly).

Recursion can be used to solve problems that can be divided into sub-problems of the same type. Examples of problems that can be solved using recursion include computing the factorial of a number, computing the nth Fibonacci number, and traversing a tree or graph.

Recursion can be implemented using either the top-down approach or the bottom-up approach. In the top-down approach, we start with the original problem and divide it into smaller sub-problems until we reach the base case. In the bottom-up approach, we start with the base case and build up to the original problem by solving larger sub-problems.

## Time Complexity

The time complexity of a recursive algorithm is typically expressed in terms of the number of recursive calls that are made. The time complexity can be analyzed using a recurrence relation, which describes the running time of a function in terms of its input size and the running time of its sub-problems.

The time complexity of a recursive algorithm can be determined using the Master Theorem or by solving the recurrence relation using mathematical techniques.

## Memory Complexity

The memory complexity of a recursive algorithm is typically proportional to the depth of the recursion tree, which is the maximum number of active function calls in the call stack at any given time. The memory complexity can be analyzed using the space required to store the parameters and local variables of each function call on the call stack.

If the recursion depth is O(log n), then the memory complexity is O(log n). If the recursion depth is O(n), then the memory complexity is O(n).
