from Node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self, node: Node, pos: int = -1) -> None:
        '''Add existing node in given pos(position). If admin don't pass position so by default new node will add to last of linked list'''
        if not self.head:
            self.head = node
            return
        if pos == -1:
            self.insertAtLast(node)
            return
        t = self.head
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        for x in range(pos-1):
            if not t.next:
                print("Given position is out of range")
                return
            t = t.next
        node.next = t.next
        t.next = node

    def addNewNode(self, title: str, date: str, summary: str, facts: str, pos: int = -1) -> None:
        '''Create new node with given data at position, added to end if no position provided'''
        node = Node(title,date,summary,facts)
        if not self.head:
            self.head = node
            return
        if pos == -1:
            self.insertAtLast(node)
            return
        t = self.head
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        for x in range(pos-1):
            if not t.next:
                print("Given position is out of range")
                return
            t = t.next
        node.next = t.next
        t.next = node

    def insertAtLast(self, node: Node) -> None:  # helper function
        '''Inserts at end of linked list'''
        t = self.head
        while t.next:
            t = t.next
        t.next = node

    def deleteLast(self) -> None:  # helper function
        '''Deletes last node in linkedlist'''
        t = self.head
        while t.next.next:
            t = t.next
        t.next = None

    def display(self) -> None:
        '''Displays info in nodes of linked list'''
        if not self.head:
            print("LinkedList is empty")
            return
        t = self.head
        while t:
            t.displayInfo()
            t = t.next

    def delete(self, pos: int = -1) -> None:
        '''Delete node from given pos(position). If admin don't pass position so by default last node will deleted.'''
        if not self.head:
            print("LinkedList is empty")
            return
        if pos == 0:
            self.head=self.head.next
            return
        if pos == -1:
            self.deleteLast()
            return
        t = self.head
        for x in range(pos-1):
            if not t.next:
                print("Given position is out of range")
                return
            t = t.next
        t.next = t.next.next if t.next else None

    def reorder(self, node, pos) -> None:
        '''Change position of given node'''
        if not self.head:
            print("LinkedList is empty")
            return
        t = self.head
        if t == node:
            self.head = t.next
            self.addNode(node, pos)
            return
        while t.next != node:
            if not t.next:
                print("Given Node is not found")
                return
            t = t.next
        t.next = t.next.next
        self.addNode(node, pos)

    def get(self,pos) -> Node:
        '''Returns node at given position'''
        if pos>=self.length():
            #print("Index out of bounds")
            return None
        curIndex=0
        cur=self.head
        while True:
            if curIndex==pos:
                return cur
            cur=cur.next
            curIndex+=1
    
    def length(self):
        '''Returns number of nodes in linkedlist'''
        cur = self.head
        total = 1
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
       
    def rate_node(node_name, rating):
        node_data[node_name]["ratings"].append(rating)
        return

    # Function to allow users to submit a review for a node
    def submit_review(node_name, review):
        node_data[node_name]["reviews"].append(review)
        #Example usage
        rate_node("item1", 4)
        submit_review("item1", "Good item!")
        return
