def insertSort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j, arr[i])  # 首先碰到第一个比自己大的数字，赶紧刹车，停在那，所以选择insert
                arr.pop(i + 1)  # 因为前面的insert操作，所以后面位数+1，这个位置的数已经insert到前面去了，所以pop弹出
                break
    return arr


print(insertSort([1, 5, 2, 6, 9, 3]))
