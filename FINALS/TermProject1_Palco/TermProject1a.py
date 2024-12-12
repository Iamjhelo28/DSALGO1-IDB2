from TermProject1_Palco.LinkedStack import LinkedStack

class Deque:
    """Deque implementation using two LinkedStacks with only push and pop operations."""

    def __init__(self):
        """Initialize an empty deque."""
        self._front_stack = LinkedStack()  # Stack for front operations
        self._back_stack = LinkedStack()   # Stack for back operations

    def is_empty(self) -> bool:
        """Check if the deque is empty."""
        return self._front_stack.is_empty() and self._back_stack.is_empty()

    def _move_all(self, source: LinkedStack, destination: LinkedStack) -> None:
        """Move all elements from one stack to another."""
        while not source.is_empty():
            destination.push(source.pop())

    def add_front(self, element: any) -> None:
        """Add an element to the front of the deque."""
        self._front_stack.push(element)

    def add_back(self, element: any) -> None:
        """Add an element to the back of the deque."""
        self._back_stack.push(element)

    def delete_front(self) -> any:
        """Remove and return the front element."""
        if self.is_empty():
            raise ValueError("Deque is empty")

        if self._front_stack.is_empty():
            # Move elements from back_stack to front_stack
            self._move_all(self._back_stack, self._front_stack)

        return self._front_stack.pop()

    def delete_back(self) -> any:
        """Remove and return the back element."""
        if self.is_empty():
            raise ValueError("Deque is empty")

        if self._back_stack.is_empty():
            # Move elements from front_stack to back_stack
            self._move_all(self._front_stack, self._back_stack)

        return self._back_stack.pop()

    def print_deque(self) -> None:
        """Print all elements in the deque from front to back."""
        temp_front = []
        temp_back = []

        # Collect elements from front_stack
        while not self._front_stack.is_empty():
            temp_front.append(self._front_stack.pop())

        # Restore elements to front_stack
        for item in reversed(temp_front):
            self._front_stack.push(item)

        # Collect elements from back_stack
        while not self._back_stack.is_empty():
            temp_back.append(self._back_stack.pop())

        # Restore elements to back_stack
        for item in reversed(temp_back):
            self._back_stack.push(item)

        # Combine and display
        print("Deque (front to back):", temp_front[::-1] + temp_back)


# Interactive Testing with Rubric Standards
def main():
    print("Deque Implementation - Interactive Testing")
    print("Name: Jhelo Palco| Date: 06-Dec-2024 | Assignment: Term Project Part A")
    deque = Deque()

    while True:
        print("\nOptions:")
        print("1: Add to Front")
        print("2: Add to Back")
        print("3: Delete from Front")
        print("4: Delete from Back")
        print("5: Print Deque")
        print("6: Check if Empty")
        print("7: Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice == 1:
                value = input("Enter a value to add to the front: ")
                deque.add_front(value)
                print(f"Added {value} to the front.")
            elif choice == 2:
                value = input("Enter a value to add to the back: ")
                deque.add_back(value)
                print(f"Added {value} to the back.")
            elif choice == 3:
                removed = deque.delete_front()
                print(f"Deleted front element: {removed}")
            elif choice == 4:
                removed = deque.delete_back()
                print(f"Deleted back element: {removed}")
            elif choice == 5:
                deque.print_deque()
            elif choice == 6:
                print("Deque is empty." if deque.is_empty() else "Deque is not empty.")
            elif choice == 7:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
