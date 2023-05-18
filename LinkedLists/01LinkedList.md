# AllThingsLinkedList

## Linked List Constructor

At a high level, a Linked List constructor will:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # Create new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self, value):
        # add node to end 
    def prepend(self,value):
        # add Node to end 
    def insert(self,index, value)
        # insert Node at provided index
```
