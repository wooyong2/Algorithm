# 선택 정렬 사용
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for i in range(N - 1):
    min = nums[i]
    index = i

    for j in range(i, N):
        if nums[j] < min:
            min = nums[j]
            index = j
    nums[i], nums[index] = nums[index], nums[i]

for num in nums:
    print(num)