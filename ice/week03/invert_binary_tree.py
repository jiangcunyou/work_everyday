from ice.week03.maximum_depth_of_binary_tree import TreeNode

class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

def print_preorder(root):
    if root is None:
        return

    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

result = Solution().invertTree(root)

print_preorder(result)
# Expected preorder:
# 4 7 9 6 2 3 1


#TC: O(n)
#SC: O(h)