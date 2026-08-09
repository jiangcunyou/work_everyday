from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_value = {}

        for index, value in enumerate(nums):
            complement = target - value

            if complement in index_by_value:
                return [index_by_value[complement], index]

            index_by_value[value] = index

        return []

# solution = Solution()
#
# input = [2,7,11,15]
# res = solution.twoSum(input, 9)
#
# print(res)

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

# nums = [1, 2, 3, 4]
#
# fun = Solution()
# print(fun.productExceptSelf(nums))


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for freq, num in count.items():
            buckets[freq].append(num)

        result = []

        for bucket in range(len(buckets) - 1, 0, -1):
            for num in buckets[bucket]:
                result.append(num)

                if len(result) == k:
                    return result
        return result

nums = [1, 1, 1, 2, 2, 3]

print(Solution().topKFrequent(nums, 3))


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

nums = [100, 4, 200, 1, 3, 2]

res = Solution().longestConsecutive(nums)
print(res)