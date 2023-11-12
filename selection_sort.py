def selection_sort(arr):
    le = len(arr)
    
    for i in range(le):
        min_index = i
        for j in range(i + 1, le):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


num = list(map(int, input("Enter list numbers: ").split()))
    
selection_sort(num)

print("Sorted list:", num)