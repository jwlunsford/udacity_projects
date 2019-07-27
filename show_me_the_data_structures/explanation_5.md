### Problem 5 - Blockchain

#### Reasoning:
For this problem, I chose to implement the solution where the blocks are stored in the chain using a list data strucutre.  The methods for the Blockchain implementation are add_block(), get_blocks(), and get_block_by_index().  Technically in a real Blockchain implementation access to the blocks would be limited to add operations only.


#### Efficiency:
* Time efficiency - O(1) worst case, becuase blocks are appended to the chain (list) and are retrieved by index number.
* Space efficiency - O(n) worst case, because each group or username must be stored as an item in a list.


