class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


class PositionalList(LinkedStack):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def __init__(self):
        super().__init__()
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        cursor = self._header
        while cursor._next != self._trailer:
            cursor = cursor._next
        return self._make_position(cursor)

    def after(self, p):
        node = self._validate(p)
        if node._next is self._trailer:
            return None
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_after(self, node, element):
        newest = self._Node(element, node._next)
        node._next = newest
        self._size += 1
        return newest

    def add_first(self, e):
        return self._make_position(self._insert_after(self._header, e))

    def add_last(self, e):
        cursor = self._header
        while cursor._next != self._trailer:
            cursor = cursor._next
        return self._make_position(self._insert_after(cursor, e))


def evaluate_postfix(expression):
    stack = LinkedStack()
    tokens = expression.strip().split()

    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
        else:
            stack.push(float(token))

    return stack.pop()


def sort_positional_list(numbers):
    asc_list = PositionalList()
    desc_list = PositionalList()

    for num in numbers:
        if asc_list.is_empty():
            asc_list.add_first(num)
            continue

        current = asc_list.first()
        inserted = False

        if num < current.element():
            asc_list.add_first(num)
            inserted = True

        while not inserted and current is not None:
            if current.element() <= num:
                next_pos = asc_list.after(current)
                if next_pos is None or next_pos.element() > num:
                    new_pos = asc_list.add_last(num)
                    inserted = True
                    break
            current = asc_list.after(current)

        if not inserted:
            asc_list.add_last(num)

    for num in numbers:
        if desc_list.is_empty():
            desc_list.add_first(num)
            continue

        current = desc_list.first()
        inserted = False

        if num > current.element():
            desc_list.add_first(num)
            inserted = True

        while not inserted and current is not None:
            if current.element() >= num:
                next_pos = desc_list.after(current)
                if next_pos is None or next_pos.element() < num:
                    new_pos = desc_list.add_last(num)
                    inserted = True
                    break
            current = desc_list.after(current)

        if not inserted:
            desc_list.add_last(num)

    return asc_list, desc_list


def main():
    expr = "5 2 + 8 3 - * 4 /"
    result = evaluate_postfix(expr)
    print(f"Postfix expression: {expr}")
    print(f"Result: {result}")

    numbers = [1, 72, 81, 25, 65, 91, 11]
    print("\nOriginal numbers:", numbers)

    asc_list, desc_list = sort_positional_list(numbers)

    print("Ascending order:", end=" ")
    for num in asc_list:
        print(num, end=" ")

    print("\nDescending order:", end=" ")
    for num in desc_list:
        print(num, end=" ")
    print()


if __name__ == "__main__":
    main()