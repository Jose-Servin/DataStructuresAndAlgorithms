class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Printing all Node values of a LinkedList
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # Linked List is empty
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        #  Linked List only had 1 Node
        # caught because length is decreased by 1 in pop invocation
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        # This is how the Node is removed from the list
        # Pointer for next is now pointing to None
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        # Cannot provide negative index
        # Cannot be an index that's not in our LL
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        #  Using the get() method
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


ll = LinkedList(0)
ll.append(1)
ll.append(2)
ll.print_list()
print("\n")
ll.set_value(2, 100)
ll.print_list()
