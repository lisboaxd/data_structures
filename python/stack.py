class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Element -> {self.value}"


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        for i in range(position + 1):
            if i == position:
                return current
            if type(current.next) == Element:
                current = current.next
            else:
                break
        return None

    def insert(self, new_element, position):
        previous = self.get_position(position - 1)
        next_element = previous.next
        new_element.next = next_element
        previous.next = new_element

    def delete(self, value):
        current = self.head
        previous = current
        while current.next:
            if current.value == value:
                previous.next = current.next
            previous = current
            current = current.next

    def insert_first(self, element):
        current = self.head
        element.next = current
        self.head = element

    def delete_first(self):
        current = self.head
        if current:
            self.head = current.next
        return current


class Stack:
    """
    Stack data structure using linked list
    """

    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.append(new_element)

    def pop(self):
        node = self.ll.head
        previous = None
        while node.next:
            previous = node
            node = node.next
            if node.next is None:
                previous.next = None
        return node


if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    stack = Stack(e1)

    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)
