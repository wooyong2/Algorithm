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
# 퀵 정렬 (Quick Sort): O(NlogN)    파이썬의 list.sort()함수나 자바의 Arrays.sort()에 쓰일 정도로 효율적인 알고리즘.
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
# 병합 정렬 (Merge Sort): O(NlogN)      Quick Sort와 다르게 어떤 경우에도 NlogN의 시간 복잡도를 가짐.
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

'''
# 힙 정렬 (Heap Sort): O(NlogN)

# 힙 정렬 코드 출처: 이수진님 블로그 (https://lsjsj92.tistory.com/472)
import random

# 최대 힙 성질을 만족하는지 확인하고 최대 힙 성질에 맞게 재정렬 해주는 함수
def heapify(unsorted, index, heap_size):
    # 정렬 과정 보고 싶다면 주석 처리 해제
    # print("unsorted:", unsorted)
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    # largest의 index가 바뀌었다는 것은 자식 노드의 값이 더 크다는 뜻이므로 부모 노드와 자식 노드의 값 변경하고
    # 변경되었으므로 부모 노드가 옮겨간 위치(원래 자식 노드의 위치)를 기준으로 다시 heapify 재귀 호출
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)
    # heapify의 경우 n개 노드 전체 다 할 필요 없이 n // 2 번째부터만 실행해도 heap의 구조를 갖춤.
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    # 위의 반복문을 거치고 나면 입력 받은 리스트는 최대 힙 구조로 되어 있음.

    # 최대 힙의 성질을 이용해서 루트 노드와 말단 노드의 값을 변경하는 방법으로 큰 순서대로 위치를 고정하며 오름차순 정렬을 하는 반복문
    for i in range(n - 1, 0, -1):
        # 가장 큰 값이 말단 노드로 가게 root 값과 말단 노드의 값을 변경 (최대 힙 구조이므로 원래 root에 가장 큰 값이 들어있었음)
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        # 가장 큰 값이 들어간 말단 노드를 제외하고 다시 최대 힙 만들어주기위해 heapify 함수 호출
        heapify(unsorted, 0, i)

    # 정렬이 완료된 리스트 반환 (이름은 unsorted지만 sorted...)
    return unsorted

test_list = [random.randint(1, 20) for i in range(20)]
print("original list:", test_list)
print("sorted list", heap_sort(test_list))
'''