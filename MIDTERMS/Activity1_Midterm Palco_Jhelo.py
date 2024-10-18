class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


def simulate_stack_operations():
    s = Stack()

    print("\ns.push(5)")
    s.push(5)

    print("s.push(3)")
    s.push(3)

    print(f"len(s): {len(s)}")

    print(f"s.pop(): {s.pop()}")

    print(f"s.is_empty(): {s.is_empty()}")

    print(f"s.pop(): {s.pop()}")

    print(f"s.is_empty(): {s.is_empty()}")

    try:
        print("s.pop()")
        s.pop()
    except IndexError as e:
        print(f"Error: {e}")

    print("s.push(7)")
    s.push(7)

    print("s.push(9)")
    s.push(9)

    print(f"s.top(): {s.top()}")

    print("s.push(4)")
    s.push(4)

    print(f"len(s): {len(s)}")

    print(f"s.pop(): {s.pop()}")

    print("s.push(6)")
    s.push(6)

    print("s.push(8)")
    s.push(8)

    print(f"s.pop(): {s.pop()}\n")


simulate_stack_operations()


def extended_stack():
    x = Stack()
    operations = [
        "push(5)", "push(3)", "pop()", "push(2)", "push(8)", "pop()", "pop()",
        "push(9)", "push(1)", "pop()", "push(7)", "push(6)", "pop()", "pop()",
        "push(4)", "pop()", "pop()"]
    returned_values = []

    for op in operations:
        if op.startswith("push"):
            value = int(op[5:-1])
            x.push(value)
            print(f"Push {value}")
        elif op == "pop()":
            if not x.is_empty():
                value = x.pop()
                returned_values.append(value)
                print(f"Pop: {value}")
            else:
                print("Pop: Stack is empty")

    print("\nPop Values returned:")
    print(returned_values)


extended_stack()
