from TermProject1_Palco.LinkedQueue import LinkedQueue
from TermProject1_Palco.LinkedStack import LinkedStack

class Deque:
    def __init__(self):
        '''Create an empty Deque'''
        self._stack = LinkedStack()
        self._queue = LinkedQueue()

    def __len__(self):
        '''Return the total number of elements in the deque'''
        return len(self._stack) + len(self._queue)

    def is_empty(self):
        '''Return True if the deque is empty'''
        return self._stack.is_empty() and self._queue.is_empty()

    def add_first(self, e):
        '''Add an element to the front of the deque'''
        self._stack.push(e)

    def add_last(self, e):
        '''Add an element to the back of the deque'''
        self._queue.enqueue(e)

    def remove_first(self):
        '''Remove and return the first element of the deque'''
        if self.is_empty():
            raise Exception('Deque is empty')
        if not self._stack.is_empty():
            return self._stack.pop()
        else:  # Transfer elements from queue to stack
            while not self._queue.is_empty():
                self._stack.push(self._queue.dequeue())
            return self._stack.pop()

    def remove_last(self):
        '''Remove and return the last element of the deque'''
        if self.is_empty():
            raise Exception('Deque is empty')
        if not self._queue.is_empty():
            return self._queue.dequeue()
        else:  # Transfer elements from stack to queue
            temp_stack = LinkedStack()
            while not self._stack.is_empty():
                temp_stack.push(self._stack.pop())
            last_element = temp_stack.pop()
            while not temp_stack.is_empty():
                self._queue.enqueue(temp_stack.pop())
            return last_element

    def first(self):
        '''Return (but do not remove) the first element of the deque'''
        if self.is_empty():
            raise Exception('Deque is empty')
        if not self._stack.is_empty():
            return self._stack.top()
        else:  # Peek the first element in the queue
            while not self._queue.is_empty():
                self._stack.push(self._queue.dequeue())
            first_element = self._stack.top()
            while not self._stack.is_empty():
                self._queue.enqueue(self._stack.pop())
            return first_element

    def last(self):
        '''Return (but do not remove) the last element of the deque'''
        if self.is_empty():
            raise Exception('Deque is empty')
        if not self._queue.is_empty():
            return self._queue.first()
        else:  # Peek the last element in the stack
            temp_stack = LinkedStack()
            while not self._stack.is_empty():
                temp_stack.push(self._stack.pop())
            last_element = temp_stack.top()
            while not temp_stack.is_empty():
                self._queue.enqueue(temp_stack.pop())
            return last_element

# Interactive Testing
def main():
    print("Deque Implementation with User Interaction")
    print("Name: Jhelo Palco | Date: 06-Dec-2024 | Assignment: Term Project 1 B")
    deque = Deque()

    while True:
        print("\nOptions:")
        print("1: Add First")
        print("2: Add Last")
        print("3: Remove First")
        print("4: Remove Last")
        print("5: View First Element")
        print("6: View Last Element")
        print("7: Check if Empty")
        print("8: Get Size")
        print("9: Exit")

        try:
            choice = int(input("Enter your choice (1-9): "))
            if choice == 1:
                value = input("Enter a value to add to the front: ")
                deque.add_first(value)
                print(f"Added {value} to the front.")
            elif choice == 2:
                value = input("Enter a value to add to the back: ")
                deque.add_last(value)
                print(f"Added {value} to the back.")
            elif choice == 3:
                removed = deque.remove_first()
                print(f"Removed {removed} from the front.")
            elif choice == 4:
                removed = deque.remove_last()
                print(f"Removed {removed} from the back.")
            elif choice == 5:
                print(f"First element: {deque.first()}")
            elif choice == 6:
                print(f"Last element: {deque.last()}")
            elif choice == 7:
                print("Deque is empty." if deque.is_empty() else "Deque is not empty.")
            elif choice == 8:
                print(f"Size of deque: {len(deque)}")
            elif choice == 9:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 9.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
