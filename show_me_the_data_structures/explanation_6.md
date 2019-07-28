### Problem 6 - Union and Intersection

#### Reasoning:
For this problem, I chose to implement the solution by creating a fuction that would extract the LinkedList values into a set.  By extracting the values of two LinkedLists, I could use the values in Python's Union and Intersection set operations.  The returned set could then be turned back into a LinkedList using the remaining values.


#### Efficiency:
* Time efficiency - O(n) worst case.  By using Python's native set methods, Union and Intersection, I was able to complete this in O(n) time where (n = s1 + s2).
* Space efficiency - O(n) worst case, because each node object is stored in memory.


#### Performance Analysis
I used Python's time module to calculate the number of seconds elapsed between the start and end of the test code.  The analysis is hardcoded to print when the problem_6.py module is run.

Also, I included a global count variable in both the union() and intersection() methods to count the number of executions of each.  These values are included in the analysis output.
