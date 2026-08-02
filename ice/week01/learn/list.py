from typing import List

nums = [2,7,11,15]

nums.append(20)
last = nums.pop()

for num in nums:
    print(num)

for index, num in enumerate(nums):
    print(index, num)