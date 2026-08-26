class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:

        def dfs(node, low, high):
            if node is None:
                return True

            if not (low < node.val < high):
                return False

            return (dfs(node.left, low, node.val)
                    and
                    dfs(node.right, node.val, high))

        return dfs(root, float("-inf"), float("inf"))

# Test 1: 合法 BST
#     2
#    / \
#   1   3

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(Solution().isValidBST(root1))
# Expected: True


# Test 2: 非法 BST
#       5
#      / \
#     1   7
#        / \
#       4   8
#
# 4 虽然 < 7，但它在 5 的右子树里，所以必须 > 5

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(8)

print(Solution().isValidBST(root2))
# Expected: False


# Test 3: 合法 BST
#       5
#      / \
#     3   7
#    / \ / \
#   2  4 6  8

root3 = TreeNode(5)
root3.left = TreeNode(3)
root3.right = TreeNode(7)
root3.left.left = TreeNode(2)
root3.left.right = TreeNode(4)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(8)

print(Solution().isValidBST(root3))
# Expected: True

#TC: O(n)
#SC: O(h)