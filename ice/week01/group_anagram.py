from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))

# TC：O(n × k log k)
# SC：O(n × k)