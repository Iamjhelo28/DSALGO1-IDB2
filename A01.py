
#1

print("#1")
arr1 = [23,89,7,56,44]
print("Array before bubble sort:")
print(arr1)

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

BubbleSort(arr1)
print("Array after bubble sort:")
print(arr1)

#2
print("\n#2")
arr2 = [12, 78, 91, 34, 62]
print("Array before insertion sort:")
print(arr2)

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

InsertionSort(arr2)
print("Array after insertion sort:")
print(arr2)

#3
print("\n#3")
arr3 = [5, 99, 48, 15, 67]
print("Array before selection sort:")
print(arr3)

def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] < arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

SelectionSort(arr3)
print("Array after selection sort:")
print(arr3)

#4
print("\n#4")
arr4 = [10, 2, 3, 1, 1, 4, 89, 21]
print("Array before insertion sort in descending order:")
print(arr4)

def InsertionSortDescending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

InsertionSortDescending(arr4)
print("Array after insertion sort in descending order:")
print(arr4)


#5
print("\n#5")
values = [arr1[2], arr1[3],arr2[2], arr2[3],arr3[2], arr3[3],arr4[2], arr4[3]]
print("Values from second and third indices of each dataset:")
print(values)
def InsertionSortAscending(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
values_ascending = values.copy()
InsertionSortAscending(values_ascending)
print("Sorted in ascending order:")
print(values_ascending)
def InsertionSortDescending(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key > values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key

values_descending = values.copy()
InsertionSortDescending(values_descending)
print("Sorted in descending order:")
print(values_descending)

# Initial values array
values = [23, 89, 7, 56, 44, 12, 78, 91, 34, 62]

# 6. Create a new list/array with values from item number 1 to 4
print("\n#6")
new_list = values[1:5]

print("New list with values from item number 1 to 4:")
print(new_list)

def SelectionSortAscending(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

SelectionSortAscending(new_list)
print("New list after selection sort in ascending order:")
print(new_list)


print("\n#7")

even_values = [num for num in new_list if num % 2 == 0]
odd_values = [num for num in new_list if num % 2 != 0]

print("Even values in the new list:")
print(even_values)

print("Odd values in the new list:")
print(odd_values)
