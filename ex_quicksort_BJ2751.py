N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

def quicksort(arr):
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
            if low <= high:     # arr[low]와 arr[high]가 둘 다 pivot 까지 오지 않은 이상 이 조건문에 걸림
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        return low

    return sort(0, len(arr) - 1)

quicksort(nums)
for num in nums:
    print(num)