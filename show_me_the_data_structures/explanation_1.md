### Problem 1:  LRU Cache

#### Reasoning:
Not knowing much about an LRU cache, I had to do some research about what they are and how they are used.  Most of the articles I found said that LRU Cache's are typically implemented using a Doubly Linked List and and Hash Map.  I had to look further to find specific examples of how these two structures could be combined.  I found the simpliest approach was to use a Python Dictionary for the hash map, and a custom Node class that provides attributes for storing previous and next node pointers.  I must admit that without examples I don't think I would have been able to come up with the correct implementation.  I was stuck trying to combine a hash map that used an array and a hashing function that used buckets as demonstrated in previous lessons.  I found an article on LeetCode about how others have implemented this structure.  Also, I found this statement on interviewcake.com "In Python 3.6, hash tables are called dictionaries.", which helped steer me in the right direction.

#### Efficiency:

# doubly linked list

The worst case efficiency for the doubly linked list:
  * update is O(1)
  * delete is O(1)
  * insert is O(1)
  * with space efficiency of O(n).

# hash map

The worst case efficiency for the hash map:
  * update is O(1) - for a native hash map this could be O(n), but this implementation was written to avoid collisons by overwriting the node value in each call to set(), if the key existed previously.
  * insert is O(1)
  * delete is O(1)
  * with space efficincy of O(n)
