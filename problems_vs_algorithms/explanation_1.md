### Square Root of an Integer

#### Design:
For this problem, I chose to implement the solution using a Binary Search algorithm.  The algorithm splits the search field by 1/2 each pass.  The mid value is found, then squared, and the search continues by incrementing or decrementing a pointer value based on the squared mid's relation to the initial value.

#### Time Complexity:
The time complexity of this problem is O(log(n)) because the algorithm uses a Binary Search method.  Each time through the search space is reduced by 1/2 n.

#### Space Compexity:
The solution uses an iterative approach with only one parameter and local variables, thus space complexity for Binary Search is O(1).
