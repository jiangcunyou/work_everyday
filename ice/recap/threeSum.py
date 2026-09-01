from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                target = nums[i] + nums[left] + nums[right]

                if target == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif target < 0:
                    left += 1
                else:
                    right -= 1

        return res

nums = [-1, 0, 1, 2, -1, -4]

print(Solution().threeSum(nums))

#TC: O(n^2)
#SC: O(1)