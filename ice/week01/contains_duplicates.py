from typing import List

class Solution:
    def containsDuplicate(self  , nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True

        return False

nums = [1,2,3,4,1]

sol = Solution()
print(sol.containsDuplicate(nums))