# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#
# solution = Solution()
#
# input = [2,7,11,15]
# res = solution.twoSum(input, 9)
#
# print(res)

#TC:O(n^2)
#SC:O(1)

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dict:
                return [dict[complement], i]

            dict[nums[i]] = i
        return []

solution = Solution1()

input = [2,7,11,15]
res = solution.twoSum(input, 9)

print(res)

#TC:O(n)
#SC:O(n)

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_value = {}
        for index, value in enumerate(nums):
            complement = target - value

            if complement in index_by_value:
                return [index_by_value[complement], index]

            index_by_value[value] = index
        return []