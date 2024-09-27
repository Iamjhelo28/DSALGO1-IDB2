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
    S = Stack()

    print("\nS.push(5)")
    S.push(5)

    print("S.push(3)")
    S.push(3)

    print(f"len(S): {len(S)}")

    print(f"S.pop(): {S.pop()}")

    print(f"S.is_empty(): {S.is_empty()}")

    print(f"S.pop(): {S.pop()}")

    print(f"S.is_empty(): {S.is_empty()}")

    try:
        print("S.pop()")
        S.pop()
    except IndexError as e:
        print(f"Error: {e}")

    print("S.push(7)")
    S.push(7)

    print("S.push(9)")
    S.push(9)

    print(f"S.top(): {S.top()}")

    print("S.push(4)")
    S.push(4)

    print(f"len(S): {len(S)}")

    print(f"S.pop(): {S.pop()}")

    print("S.push(6)")
    S.push(6)

    print("S.push(8)")
    S.push(8)

    print(f"S.pop(): {S.pop()}\n")


simulate_stack_operations()
def extended_stack():
    S = Stack()
    operations = [
        "push(5)", "push(3)", "pop()", "push(2)", "push(8)", "pop()", "pop()",
        "push(9)", "push(1)", "pop()", "push(7)", "push(6)", "pop()", "pop()",
        "push(4)", "pop()", "pop()"]
    returned_values = []

    for op in operations:
        if op.startswith("push"):
            value = int(op[5:-1])
            S.push(value)
            print(f"Push {value}")
        elif op == "pop()":
            if not S.is_empty():
                value = S.pop()
                returned_values.append(value)
                print(f"Pop: {value}")
            else:
                print("Pop: Stack is empty")

    print("\nPop Values returned:")
    print(returned_values)

extended_stack()