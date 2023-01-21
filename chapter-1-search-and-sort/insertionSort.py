def InsertionSort(data):
    for i in range(1, len(data)):
        j = i - 1
        current_elem = data[i]
        while current_elem < data[j] and j >= 0:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = current_elem
    return data
