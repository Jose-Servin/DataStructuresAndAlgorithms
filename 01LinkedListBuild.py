class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    .append(self)

    .pop(self)

    .prepend(self)

    .pop_first(self)

    .get(self, index)

    .set_value(self, index, value)

    .insert(self, index, value)

    .remove(self, index)

    .reverse(self)
    """

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

    def pop_first(self):
        # check if LL is empty
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # Check if LL is empty after removing node
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        # check index is valid
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        # check index is valid
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        # Check get() return values
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):

        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value=value)
        if index == self.length:
            return self.append(value=value)
        nn = Node(value=value)
        pre = self.get(index - 1)
        nn.next = pre.next
        pre.next = nn
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


ll = LinkedList(3)
ll.append(4)
ll.append(10)
ll.print_list()
print("\n")
ll.print_list()
