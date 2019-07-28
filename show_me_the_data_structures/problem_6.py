class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def get_head(self):
        return self.head

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

count_union = 0

def union(llist_1, llist_2):
    global count_union
    # create two set objects from the linkedlists
    s1 = set_from_linkedlist(llist_1)
    s2 = set_from_linkedlist(llist_2)

    # create the union
    sUnion = s1.union(s2)
    # recreate the linkedlist from the union result
    newList = LinkedList()
    for i in sUnion:
        newList.append(i)
        count_union += 1
    return newList

count_intersection = 0

def intersection(llist_1, llist_2):
    global count_intersection

    # create two set objects from the linkedlists
    s1 = set_from_linkedlist(llist_1)
    s2 = set_from_linkedlist(llist_2)

    # create the intersection
    sIntersect = s1.intersection(s2)
    # recreate the linkedlist from the intersection result
    newList = LinkedList()
    for i in sIntersect:
        newList.append(i)
        count_intersection += 1
    return newList

def set_from_linkedlist(llist):
    # create a set from a linked list
    s = set()
    node = llist.get_head()
    while node:
        s.add(node.value)
        node = node.next
    return s



import time

start = time.time()

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))                  # returns 32->65->2->35->3->4->6->1->9->11->21->
print (intersection(linked_list_1,linked_list_2))           # returns 4->21->6

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [5,4,3,2,1,0]
element_2 = [1,2,3,4,5,0]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))                  # returns 0->1->2->3->4->5->
print (intersection(linked_list_3,linked_list_4))           # returns same as above, these sets are identical,
                                                            # therefore union = intersection


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [x for x in range(0, 1000, 1)]
element_6 = [x for x in range(0, 1000, 50)]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))                  # returns every number from 0 to 999
print(intersection(linked_list_5, linked_list_6))           # returns only numbers from 0 to 1000 that are multiples
                                                            # of 50

end = time.time()

# performance analysis
elapsed_time = end-start
print('\n********** Peformance Analysis **********')
print(f'runtime execution = {elapsed_time} seconds')  # run time in milliseconds
print(f'# of union() executions = {count_union}')
print(f'# of intersection() exectuions = {count_intersection}')