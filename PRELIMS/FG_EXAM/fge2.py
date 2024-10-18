print("Array before insertion sort:")
arr1=[1,2,21,33,45,65,12]
print(arr1)

for i in range(1,len(arr1)):
    key=arr1[i]
    j=i-1
    while j>=0 and key>arr1[j]:
        arr1[j+1]=arr1[j]
        j-=1
    arr1[j+1]=key

print("Array after insertion sort:")
print(arr1)



print("\nArray before selection sort:")
arr=[1,2,21,33,45,65,12]
print(arr)

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx=j
    arr[i],arr[min_idx] = arr[min_idx],arr[i]

print("Array before selection sort:")
print(arr)



