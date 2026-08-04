from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = []
#
#         for i in range(len(nums)):
#             product = 1
#
#             for j in range(len(nums)):
#                 if i != j:
#                     product *= nums[j]
#
#             result.append(product)
#
#         return result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

nums = [1, 2, 3, 4]

fun = Solution()
print(fun.productExceptSelf(nums))

#TC: O(n)
#SC: O(n)