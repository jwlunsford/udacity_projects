### Problem 2 - File Recursion

#### Reasoning:
For this problem, I chose to implement a recursive function that would loop through files within subdirectories.  The initial problem lists all file and directories in the root path, then it iterates thorugh the list pulling out matching files.  The matching files are appended to a list, which is returned to the user.  The recursive call only happens when the file is a directory, so the base case is loop through each directory finding all files that match.

#### Efficiency:
* Time efficiency - O(n) worst case, based on the number of files in the root directory.  The solution must check each file to see if it is a match.
* Space efficiency - O(n) worst case, because each possible file could be a match that is stored in the list.


