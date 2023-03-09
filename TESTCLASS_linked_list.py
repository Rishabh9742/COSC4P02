from linked_list import LinkedList
from Node import Node

list = LinkedList()

#Testing addNode
print("Testing addNode Function")
n1 = Node("t1","d1","s1","f1")
n2 = Node("t2","d2","s2","f2")
n3 = Node("t3","d3","s3","f3")
list.addNode(n1)
list.addNode(n2)
list.addNode(n3,1)
list.addNode
if n1 == list.get(0) and n2 == list.get(2) and n3 == list.get(1):
    print("TEST 1: PASSED")
else:
    print("TEST 1: FAILED ")
#list.addMode(n1,3)

#Testing remove
print("Testing remove Function")
#TEST 2: Test default delete, last object
list.delete()
if list.get(2) == n2:
    print("TEST 2: FAILED ")
else:
    print("TEST 2: PASSED")
    list.addNode(n2)
#TEST 3: Test deleting index 0, first object
list.delete(0) 
if list.get(0) == n1:
    print("TEST 3: FAILED ")
else:
    print("TEST 3: PASSED")
    list.addNode(n1,0)
#TEST 4: Test deleting index, last object
list.delete(2)
if list.get(2) == n2:
    print("TEST 4: FAILED ")
else:
    print("TEST 4: PASSED")
    list.addNode(n2)
#TEST 5: Test deleting index, middle of list
list.delete(1)
if list.get(1) == n3:
    print("TEST 5: FAILED ")
else:
    print("TEST 5: PASSED")
    list.addNode(n3,1)

