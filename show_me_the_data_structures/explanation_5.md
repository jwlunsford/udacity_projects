### Problem 5 - Blockchain

#### Reasoning:
For this problem, I chose to implement the solution where the blocks are stored in the chain using a list data strucutre.  The methods for the Blockchain implementation are add_block(), get_blocks(), and get_block_by_index().  Technically in a real Blockchain implementation access to the blocks would be limited to add operations only.


#### Efficiency:
* Time efficiency - O(n) worst case.  Blocks are appended to the chain with O(1) constant time, and are retrieved by iterating through the chain starting with the first chain until the index is found.  Printing the blocks are also O(n) time.
* Space efficiency - O(n) worst case, because each block is stored in memory.


