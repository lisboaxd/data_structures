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
        """Exclua o primeiro node que contenha um valor determinado."""
        current = self.head
        previous = current
        while current.next:
            if current.value == value:
                previous.next = current.next
            previous = current
            current = current.next


if __name__ == "__main__":
    el1 = Element(1)
    el2 = Element(2)
    el3 = Element(3)
    el4 = Element(4)
    el5 = Element(5)

    ll = LinkedList(el1)
    ll.append(el2)
    ll.append(el3)
    ll.append(el4)

    print(ll.get_position(0))
    print(ll.get_position(1))
    print(ll.get_position(2))
    print(ll.get_position(3))
    print(ll.get_position(4))
    print("#" * 20)
    ll.insert(el5, 2)
    print(ll.get_position(0))
    print(ll.get_position(1))
    print(ll.get_position(2))
    print(ll.get_position(3))
    print(ll.get_position(4))
    print("#" * 20)
    ll.delete(5)
    print(ll.get_position(0))
    print(ll.get_position(1))
    print(ll.get_position(2))
    print(ll.get_position(3))
    print(ll.get_position(4))
