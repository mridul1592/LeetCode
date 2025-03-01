# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root:
                if not root.left and not root.right:
                    yield root.val
                else:
                    if root.left:
                        yield from dfs(root.left)
                    if root.right:
                        yield from dfs(root.right)
        
        l1 = list(dfs(root1))
        l2 = list(dfs(root2))
        
        return l1 == l2