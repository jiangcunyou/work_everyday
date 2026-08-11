from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            add = numbers[left] + numbers[right]

            if add == target:
                return [left, right]
            elif add < target:
                left += 1
            else:
                right -= 1
        return []

numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))

#TC:O(n)
#SC:O(1)