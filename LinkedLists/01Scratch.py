class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    .print_list(self, value)

    .append(self, value)

    .pop(self)

    .prepend(self, value)

    pop_first(self)

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
        nn = Node(value=value)
        # LL is empty
        if self.head is None:
            self.head = nn
            self.tail = nn
        else:
            # -----O-----O----O
            self.tail.next = nn
            self.tail = nn

        self.length += 1

        return True

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        nn = Node(value=value)
        if self.length == 0:
            self.head = nn
            self.tail = nn
        else:
            nn.next = self.head
            self.head = nn

        self.length += 1

        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
