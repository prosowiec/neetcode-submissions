class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Each stack frame stores: [node, state, left_height, right_height]
        # state 0: visit left child
        # state 1: visit right child
        # state 2: both children done, check balance and return height to parent
        stack = [[root, 0, 0, 0]]
        last_returned_height = 0
        
        while stack:
            frame = stack[-1]
            node, state, left_h, right_h = frame
            
            if state == 0:
                frame[1] = 1  # Next time we see this frame, move to state 1
                if node.left:
                    stack.append([node.left, 0, 0, 0])
                else:
                    last_returned_height = 0
                    
            elif state == 1:
                frame[2] = last_returned_height  # Capture height returned by left subtree
                frame[1] = 2  # Next time, move to state 2
                if node.right:
                    stack.append([node.right, 0, 0, 0])
                else:
                    last_returned_height = 0
                    
            else:  # state == 2
                frame[3] = last_returned_height  # Capture height returned by right subtree
                left_h, right_h = frame[2], frame[3]
                
                if abs(left_h - right_h) > 1:
                    return False
                
                # Pop current frame and pass its height up to the parent frame
                last_returned_height = 1 + max(left_h, right_h)
                stack.pop()
                
        return True
