# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxHeight(root):
            if not root:
                return [0, True]

            left, balancedL = maxHeight(root.left)
            right, balancedR  = maxHeight(root.right)
            
            balanced = balancedR and balancedL and abs(left-right)<=1

            return [1 + max(left, right), balanced]

        return maxHeight(root)[1]



