from linked_list import LinkedList
from Node import Node
import copy

list = LinkedList()

#Testing addNode
print("Testing addNode and get functions")
n1 = Node("t1","d1","s1","f1")
n2 = Node("t2","d2","s2","f2")
n3 = Node("t3","d3","s3","f3")
list.addNode(n1)
list.addNode(n2)
list.addNode(n3,1)
list.addNode

#Deep copy of list for resetting list after tests
list2 = copy.deepcopy(list)

if "t1" == list.get(0).title and "t2" == list.get(2).title and "t3" == list.get(1).title:
    print("TEST 1: PASSED")
    list = copy.deepcopy(list2)
else:
    print("TEST 1: FAILED ")
    list = copy.deepcopy(list2)


print("Testing remove Function")
#TEST 2: Test default delete, last object
list.delete()
try:
    if list.get(2).title == "t2":
        print ("TEST 4: FAILED")
        list = copy.deepcopy(list2)
except:
    print ("TEST 4: PASSED")
    list = copy.deepcopy(list2)

#TEST 3: Test deleting index 0, first object
list.delete(0)
if list.get(0).title == "t1":
    print("TEST 3: FAILED ")
    list = copy.deepcopy(list2)
else:
    print("TEST 3: PASSED")
    list = copy.deepcopy(list2)

#TEST 4: Test deleting index, last object using index
list.delete(2)
try:
    if list.get(2).title == "t2":
        print ("TEST 4: FAILED")
        list = copy.deepcopy(list2)
except:
    print ("TEST 4: PASSED")
    list = copy.deepcopy(list2)

#TEST 5: Test deleting index, middle of list
list.delete(1)
if list.get(1).title == "t3":
    print("TEST 5: FAILED ")
    list = copy.deepcopy(list2)
else:
    print("TEST 5: PASSED")
    list = copy.deepcopy(list2)

