
def MergeSort(data):
    if len(data) > 1:
        split_point = len(data) // 2
        left = data[:split_point]
        right = data[split_point:]
        sorted_left = MergeSort(left)
        sorted_right = MergeSort(right)

        merged = sorted_left + sorted_right
        merged.sort()

        data = merged

    return data
