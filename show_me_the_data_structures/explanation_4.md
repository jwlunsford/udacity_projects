### Problem 4 - Active Directory

#### Reasoning:
For this problem, I chose to implement the solution using a custom object called a TreeSearch().  This object is used to store the initial state (found=False), then updates this state if the username is found in the directory.  This uses a recursive approach by calling search_users() to move through the subgroups to the end of the tree.


#### Efficiency:
* Time efficiency - O(n) worst case, becuase all groups, subgroups and usernames in the structure must be accessed to check if username is equal to the search term.
* Space efficiency - O(n) worst case, because each group or username must be stored as an item in a list.


