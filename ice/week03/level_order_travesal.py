from collections import deque


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                cur = queue.popleft()
                level.append(cur.val)

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

            result.append(level)

        return result

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().levelOrder(root))
# Expected:
# [[3], [9, 20], [15, 7]]

#TC: O(n)
#SC: O(n)