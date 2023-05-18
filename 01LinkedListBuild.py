class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        nn = Node(value)
        self.head = nn
        self.tail = nn
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        nn = Node(value)
        if self.head is None:
            self.head = nn
            self.tail = nn
        else:
            self.tail.next = nn
            self.tail = nn
        self.length += 1
        return True

    def pop(self):
        # Check if LL is empty
        if self.length == 0:
            return None
        # Walk LL
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # Check if LL is empty and reset properties
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        nn = Node(value)
        # check if LL is empty
        if self.length == 0:
            self.head = nn
            self.tail = nn
        else:
            nn.next = self.head
            self.head = nn
        # Increase length regardless if LL was empty of not
        self.length += 1
        return True


ll = LinkedList(3)
ll.append(4)
ll.append(10)
ll.prepend(5)
ll.print_list()
print("\n")
ll.pop()
ll.print_list()
