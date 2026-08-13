from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            area_size = width * min(height[left], height[right])

            if area_size > max_area:
                max_area = area_size

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))

#TC: O(n)
#SC: O(1)