# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        helperStack = [root]
        maxDepth = 1
        curH = 1
        currH = [1]
        while helperStack:
            curr = helperStack.pop()
            curH = currH.pop()
            #print(curr.val, helperStack, curH)
            if curr.left:
                currH.append(curH + 1) 
                helperStack.append(curr.left)
            if curr.right:
                currH.append(curH + 1)
                helperStack.append(curr.right)
            
            #curH += 1
            maxDepth = max(maxDepth, curH)
        return maxDepth