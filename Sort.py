'''
# 선택 정렬 (Selection Sort): O(N^2)
a = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(9):
    min = a[i]
    index = i
    for j in range(i, 10):
        if a[j] < min:
            min = a[j]
            index = j
    a[i], a[index] = a[index], a[i]
print(a)
'''

'''
# 버블 정렬 (Bubble Sort): O(N^2)
a = [10, 1, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(10):
    for j in range(9 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
'''

'''
# 삽입 정렬 (Insertion Sort): O(N^2)  하지만 데이터가 이미 거의 정렬된 상태에서는 굉장히 효율적인 알고리즘.
a = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(9):
    j = i
    while(a[j] > a[j + 1]):
        a[j], a[j + 1] = a[j + 1], a[j]
        j -= 1
print(a)
'''

'''
# 퀵 정렬 (Quick Sort): O(NlogN)     파이썬의 list.sort()함수나 자바의 Arrays.sort()에 쓰일 정도로 효율적인 알고리즘.
#                                   하지만 pivot 값을 기준으로 분할했을 때 값들이 한 편으로 치우치게되면 성능이 저하되며
#                                   최악의 경우 한 편으로만 모든 값들이 몰리게 되어 O(N^2)까지도 가능.
arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

def quickSort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:     # pivot 값보다 큰 값이 나올 때까지 (없다 해도 pivot 에서 반복문 끝남)
                low += 1
            while arr[high] > pivot:    # pivot 값보다 작은 값이 나올 때까지 (없다 해도 pivot 에서 반복문 끝남)
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        return low

    return sort(0, len(arr) - 1)

quickSort(arr)
print(arr)
'''

'''
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
a = [2, 4, 5, 1, 9, 8, 7, 3]
merge_sort(a)
print(a)
'''