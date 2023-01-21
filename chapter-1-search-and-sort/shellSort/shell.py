

def ShellSort(data):
    distance = len(data) // 2
    while distance > 0:
        for i in range(distance, len(data)):
            temp = data[i]
            j = i
            while j >= distance and data[j - distance] > temp:
                data[j] = data[j - distance]
                j = j - distance
            data[j] = temp
        distance = distance // 2
    return data