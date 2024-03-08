def funcSort(inputList, num):
    start = sorted(inputList[:num])
    end = sorted(inputList[num:], reverse=True)
    start.extend(end)
    return start


x = [11, 7, 5, 10, 46, 23, 16, 8]
print(funcSort(x, 3))
