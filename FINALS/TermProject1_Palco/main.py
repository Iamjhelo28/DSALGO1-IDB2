from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from CircularQueue import CircularQueue as CircularQueue
from LinkedDeque import LinkedDeque as Deque
from PositionalList import PositionalList as PositionalList
Q = Queue()
S = Stack()
CircQ = CircularQueue()
D = Deque()
P = PositionalList()
'''
#Adding elements to the stack
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)

#Removing elements from the stack
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())

#Adding elements to the Queue
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)

#Removing elements from the Queue
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
'''
'''
#adding elements to the Circular Queue
CircQ.enqueue(1)
CircQ.enqueue(2)
CircQ.enqueue(3)
#printing elements from the Circular Queue
CircQ.rotate()
print(CircQ.dequeue())
print(CircQ.dequeue())
print(CircQ.dequeue())
'''
'''
#adding elements to the Deque
D.insert_first(1)
D.insert_first(2)
D.insert_first(3)
#removing elements from the Deque
print(D.delete_last())
print(D.delete_last())
print(D.delete_last())
print(D.delete_last())
'''

#adding elements to the PositionalList
P.add_first(1)
P.add_first(2)
P.add_first(3)
P.add_first(4)
P.add_first(5)
P.add_first(6)
P.add_last(7)
#Print the elements from the PositionalList
for x in P:
    print(x)

# Define the bubble sort function
def bubble_sort(L):
    n = len(L)
    for i in range(n):
        swapped = False
        current = L.first()
        for j in range(n - i - 1):
            next = L.after(current)
            if current.element() > next.element():
                a = next.element()
                b = current.element()
                L.replace(current, a)
                L.replace(next, b)
                swapped = True
            current = next
        if not swapped:
            break

# Sort the PositionalList
#bubble_sort(P)
#print("The sorted list of elements are: ")
# Print the sorted elements
#for x in P:
#    print(x)

def insertion_sort(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value > marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort(P)
print("The sorted list of elements are: ")
# Print the sorted elements
for x in P:
    print(x)
#change the insertion sort to descending order
def insertion_sort_descending(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value < marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort_descending(P)
print("The sorted list of elements are: ")
# Print the sorted elements
for x in P:
    print(x)