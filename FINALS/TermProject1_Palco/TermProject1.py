from TermProject1_Palco.LinkedStack import LinkedStack  # Import LinkedStack

class Deque:
    """Deque implementation using two LinkedStacks."""

    def __init__(self):
        """Initialize an empty deque."""
        self._front_stack = LinkedStack()  # Use LinkedStack instead of custom Stack
        self._back_stack = LinkedStack()   # Use LinkedStack instead of custom Stack

    def __len__(self) -> int:
        """Return the number of elements in the deque."""
        return len(self._front_stack) + len(self._back_stack)

    def is_empty(self) -> bool:
        """Check if the deque is empty."""
        return self.__len__() == 0

    def _rebalance(self) -> None:
        """Rebalance stacks to maintain efficient operations."""
        if len(self._front_stack) < len(self._back_stack) // 2:
            # Move elements from back to front
            while len(self._back_stack) > len(self._front_stack):
                self._front_stack.push(self._back_stack.pop())

        if len(self._back_stack) < len(self._front_stack) // 2:
            # Move elements from front to back
            temp = LinkedStack()
            while len(self._front_stack) > len(self._back_stack):
                temp.push(self._front_stack.pop())
            while not temp.is_empty():
                self._back_stack.push(temp.pop())

    def add_front(self, element: any) -> None:
        """Add an element to the front of the deque."""
        self._front_stack.push(element)
        self._rebalance()

    def add_back(self, element: any) -> None:
        """Add an element to the back of the deque."""
        self._back_stack.push(element)
        self._rebalance()

    def delete_front(self) -> any:
        """Remove and return the front element."""
        if self.is_empty():
            raise ValueError("Deque is empty")

        if self._front_stack.is_empty():
            # Transfer elements from back to front
            while not self._back_stack.is_empty():
                self._front_stack.push(self._back_stack.pop())

        result = self._front_stack.pop()
        self._rebalance()
        return result

    def delete_back(self) -> any:
        """Remove and return the back element."""
        if self.is_empty():
            raise ValueError("Deque is empty")

        if self._back_stack.is_empty():
            # Transfer elements from front to back
            while not self._front_stack.is_empty():
                self._back_stack.push(self._front_stack.pop())

        result = self._back_stack.pop()
        self._rebalance()
        return result

    def front(self) -> any:
        """Return the front element without removing it."""
        if self.is_empty():
            raise ValueError("Deque is empty")

        if self._front_stack.is_empty():
            while not self._back_stack.is_empty():
                self._front_stack.push(self._back_stack.pop())

        return self._front_stack.top()

    def back(self) -> any:
        """Return the back element without removing it."""
        if self.is_empty():
            raise ValueError("Deque is empty")

        if self._back_stack.is_empty():
            while not self._front_stack.is_empty():
                self._back_stack.push(self._front_stack.pop())

        return self._back_stack.top()

    def print_deque(self) -> None:
        """Print all elements in the deque from front to back."""
        temp_front = []
        temp_back = []

        # Collect elements from front_stack
        front = LinkedStack()
        while not self._front_stack.is_empty():
            element = self._front_stack.pop()
            temp_front.append(element)
            front.push(element)

        while not front.is_empty():
            self._front_stack.push(front.pop())

        # Collect elements from back_stack
        back = LinkedStack()
        while not self._back_stack.is_empty():
            element = self._back_stack.pop()
            temp_back.append(element)
            back.push(element)

        while not back.is_empty():
            self._back_stack.push(back.pop())

        # Combine and display
        print("Deque (front to back):", temp_front[::-1] + temp_back)


# Testing with printing
def test_deque_with_print():
    d = Deque()

    print("Initial Deque:")
    d.print_deque()

    print("\nAdding elements...")
    d.add_front(1)
    print("After add_front(1):")
    d.print_deque()

    d.add_back(2)
    print("After add_back(2):")
    d.print_deque()

    d.add_front(0)
    print("After add_front(0):")
    d.print_deque()

    d.add_back(3)
    print("After add_back(3):")
    d.print_deque()

    print("\nDeleting elements...")
    print(f"Deleted front: {d.delete_front()}")
    d.print_deque()

    print(f"Deleted back: {d.delete_back()}")
    d.print_deque()

    print(f"Deleted front: {d.delete_front()}")
    d.print_deque()

    print(f"Deleted back: {d.delete_back()}")
    d.print_deque()


# Run tests
if __name__ == "__main__":
    test_deque_with_print()
